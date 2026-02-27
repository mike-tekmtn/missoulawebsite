const http = require('http');
const fs = require('fs');
const path = require('path');
const { execFile } = require('child_process');

const PORT = Number(process.env.PORT || 3080);
const ROOT = __dirname;

function scoreRequest(body) {
  let score = 1;
  const features = Array.isArray(body.features) ? body.features : [];
  const pageCount = String(body.pageCount || '1-3');

  if (pageCount === '4-6') score += 1;
  if (pageCount === '7-10') score += 2;
  if (pageCount === '10+') score += 3;

  if (features.includes('booking')) score += 1;
  if (features.includes('payments')) score += 2;
  if (features.includes('ecommerce')) score += 3;
  if (features.includes('crm')) score += 2;
  if (features.includes('custom-design')) score += 1;
  if (String(body.copywriting || 'no') === 'yes') score += 1;

  let complexity = 'low';
  let feasibility = 'great fit for one-day build';
  if (score >= 4) complexity = 'medium';
  if (score >= 7) {
    complexity = 'high';
    feasibility = 'possible, but likely better as multi-day build';
  }

  return { score, complexity, feasibility };
}

function sendTelegramSummary(body, result) {
  const msg = [
    'New missoulawebsite intake submitted',
    `Business: ${body.businessName || '-'}`,
    `Contact: ${body.contactName || '-'} (${body.email || '-'})`,
    `Type: ${body.businessType || '-'}`,
    `Timeline: ${body.timeline || '-'}`,
    `Pages: ${body.pageCount || '-'}`,
    `Features: ${(body.features || []).join(', ') || 'none'}`,
    `Complexity: ${result.complexity} (score ${result.score})`,
    `Feasibility: ${result.feasibility}`,
    body.notes ? `Notes: ${String(body.notes).slice(0, 350)}` : null
  ].filter(Boolean).join('\n');

  execFile('openclaw', ['message', 'send', '--channel', 'telegram', '--target', '7178382755', '--message', msg], () => {});
}

function serveFile(res, pathname) {
  const filePath = path.join(ROOT, pathname === '/' ? '/index.html' : pathname);
  if (!filePath.startsWith(ROOT)) return res.writeHead(403).end('Forbidden');

  fs.readFile(filePath, (err, data) => {
    if (err) return res.writeHead(404).end('Not found');
    const ext = path.extname(filePath);
    const type = ({ '.html': 'text/html', '.css': 'text/css', '.js': 'application/javascript' })[ext] || 'text/plain';
    res.writeHead(200, { 'Content-Type': type });
    res.end(data);
  });
}

const server = http.createServer((req, res) => {
  if (req.method === 'POST' && req.url === '/api/intake') {
    let raw = '';
    req.on('data', chunk => raw += chunk);
    req.on('end', () => {
      try {
        const body = JSON.parse(raw || '{}');
        const result = scoreRequest(body);
        sendTelegramSummary(body, result);
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify(result));
      } catch {
        res.writeHead(400, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ error: 'Invalid payload' }));
      }
    });
    return;
  }

  if (req.method === 'GET') return serveFile(res, req.url.split('?')[0]);
  res.writeHead(405).end('Method not allowed');
});

server.listen(PORT, '0.0.0.0', () => {
  console.log(`missoulawebsite running on :${PORT}`);
});
