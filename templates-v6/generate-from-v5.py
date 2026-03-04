#!/usr/bin/env python3
import json,re,sys
from pathlib import Path

ROOT=Path('/home/mike/.openclaw/workspace/missoulawebsite')
V5=ROOT/'templates-v5'
OUTROOT=ROOT/'templates-v6'/'generated-v5style'

MAP=[
    (['roof','hvac','plumb','repair','contractor'],'roofing-contractor'),
    (['law','legal','attorney'],'law-firm'),
    (['dental','clinic','med','spa'],'dental-clinic'),
    (['fitness','coach','trainer'],'fitness-coach'),
    (['clean','maid'],'home-cleaning')
]


def pick_template(bt):
    bt=(bt or '').lower()
    for keys,t in MAP:
        if any(k in bt for k in keys):
            return t
    return 'roofing-contractor'

def slug(s):
    return re.sub(r'[^a-z0-9]+','-',(s or 'site').lower()).strip('-') or 'site'

def apply_vars(html,i):
    # conservative replacements to preserve polished layout
    repls={
        'North Valley Roofing': i.get('businessName','Local Business'),
        'BrightPath Dental': i.get('businessName','Local Business'),
        'Granite Legal Group': i.get('businessName','Local Business'),
        'Peak Climate Systems': i.get('businessName','Local Business'),
        'Forge Method Coaching': i.get('businessName','Local Business'),
        'FreshNest Cleaning': i.get('businessName','Local Business')
    }
    for a,b in repls.items():
        html=html.replace(a,b)
    # contact channels
    phone=i.get('phone') or '406-555-0000'
    email=i.get('email') or 'hello@example.com'
    html=html.replace('(406) 555-0199', phone)
    html=html.replace('hello@summitshieldroofing.com', email)
    # generic CTA bias from features
    feats=[f.lower() for f in i.get('features',[])]
    if 'booking' in feats:
        html=html.replace('Request Dispatch','Book Now').replace('Request Estimate','Book Now')
    return html

if __name__=='__main__':
    if len(sys.argv)<2:
        print('usage: generate-from-v5.py intake.json [outdir]'); sys.exit(1)
    intake=json.loads(Path(sys.argv[1]).read_text())
    t=pick_template(intake.get('businessType',''))
    out=Path(sys.argv[2]) if len(sys.argv)>2 else OUTROOT/slug(intake.get('businessName','site'))
    out.mkdir(parents=True, exist_ok=True)
    src=V5/t
    for fn in ['index.html','services.html','about.html','contact.html']:
        h=(src/fn).read_text()
        h=apply_vars(h,intake)
        (out/fn).write_text(h)
    (out/'meta.json').write_text(json.dumps({'sourceTemplate':t,'method':'v5-polished-baseline'},indent=2))
    (out/'intake.json').write_text(json.dumps(intake,indent=2))
    print(str(out))
