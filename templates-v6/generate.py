#!/usr/bin/env python3
import json, re, sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
RULES = json.loads((BASE/'rules-engine.json').read_text())


def pick_archetype(i):
    bt = (i.get('businessType') or '').lower()
    feats = [f.lower() for f in i.get('features', [])]
    pc = str(i.get('pageCount',''))
    for r in RULES['archetypeRules']:
        w = r['when']
        ok = True
        if 'businessTypeIncludes' in w:
            ok = any(k in bt for k in w['businessTypeIncludes'])
        if ok and 'featuresAny' in w:
            ok = any(f in feats for f in w['featuresAny'])
        if ok and 'pageCountAny' in w:
            ok = pc in w['pageCountAny']
        if ok:
            return r['archetype']
    return RULES['defaultArchetype']


def nav():
    return "<nav class='text-sm opacity-80 flex gap-4'><a href='index.html'>Home</a><a href='services.html'>Services</a><a href='about.html'>About</a><a href='contact.html'>Contact</a></nav>"


def layout(archetype, i):
    name=i.get('businessName','Local Business')
    bt=i.get('businessType','service business')
    cta='Request Quote' if 'booking' not in i.get('features',[]) else 'Book Now'
    hero=f"<h1 class='text-5xl font-extrabold leading-tight'>{name}: {bt.title()} Website</h1><p class='mt-4 text-slate-300'>Built from intake-driven archetype selection with conversion-focused structure.</p><div class='mt-6'><a class='px-5 py-3 rounded-lg bg-cyan-400 text-slate-900 font-bold'>{cta}</a></div>"
    if archetype=='utility-dashboard':
        main=f"<section class='rounded-2xl border p-6 bg-slate-900'>{hero}</section><section class='mt-4 grid grid-cols-2 md:grid-cols-4 gap-3'><div class='rounded-xl border p-4'><p class='text-xs opacity-70'>Avg Callback</p><p class='text-2xl font-bold'>9 min</p></div><div class='rounded-xl border p-4'><p class='text-xs opacity-70'>Jobs This Month</p><p class='text-2xl font-bold'>129</p></div><div class='rounded-xl border p-4'><p class='text-xs opacity-70'>Satisfaction</p><p class='text-2xl font-bold'>4.9★</p></div><div class='rounded-xl border p-4'><p class='text-xs opacity-70'>Service Radius</p><p class='text-2xl font-bold'>35 mi</p></div></section>"
    elif archetype=='editorial-story':
        main=f"<section class='rounded-2xl border p-8 bg-stone-50 text-stone-900'>{hero.replace('text-slate-300','text-stone-700').replace('bg-cyan-400 text-slate-900','bg-amber-600 text-white')}</section><section class='mt-4 space-y-3 text-stone-900'><article class='rounded-xl border bg-white p-5'><h2 class='text-2xl font-serif'>Chapter 1: Context</h2></article><article class='rounded-xl border bg-white p-5'><h2 class='text-2xl font-serif'>Chapter 2: Strategy</h2></article><article class='rounded-xl border bg-white p-5'><h2 class='text-2xl font-serif'>Chapter 3: Results</h2></article></section>"
    elif archetype=='offer-funnel':
        main=f"<section class='rounded-2xl border p-8 bg-neutral-900'>{hero}</section><section class='mt-4 space-y-3'><div class='rounded-xl border p-4'>✅ What’s included</div><div class='rounded-xl border p-4'>✅ Social proof</div><div class='rounded-xl border p-4'>✅ FAQ + objections</div></section>"
    elif archetype=='asymmetric-bento':
        main=f"<section class='mt-1 grid grid-cols-1 md:grid-cols-6 gap-3'><div class='md:col-span-4 rounded-xl p-6 bg-fuchsia-400 text-slate-900'>{hero}</div><div class='md:col-span-2 rounded-xl border p-6'>Context Card</div><div class='md:col-span-2 rounded-xl border p-4'>Reviews</div><div class='md:col-span-2 rounded-xl border p-4'>Services</div><div class='md:col-span-2 rounded-xl border p-4'>Trust</div></section>"
    else:
        main=f"<section class='grid md:grid-cols-2 gap-3'><article class='rounded-2xl border p-6 bg-slate-900'>{hero}</article><aside class='rounded-2xl border overflow-hidden'><img src='https://images.pexels.com/photos/3184291/pexels-photo-3184291.jpeg?auto=compress&cs=tinysrgb&w=1400' class='w-full h-full object-cover'></aside></section>"
    return main


def render(i):
    arche=pick_archetype(i)
    theme_bg = "bg-slate-950 text-slate-100"
    if arche=='editorial-story':
        theme_bg = "bg-stone-100 text-stone-900"
    if arche=='offer-funnel':
        theme_bg = "bg-neutral-950 text-neutral-100"
    name=i.get('businessName','Business')
    header=f"<header class='max-w-6xl mx-auto p-6 flex justify-between items-center gap-4'><div class='font-bold text-xl'>{name}</div>{nav()}</header>"
    main=layout(arche,i)
    footer="<footer class='max-w-6xl mx-auto p-6 border-t mt-8 text-sm opacity-75'>Links · About · Services · Contact · Social</footer>"
    skeleton=lambda body,title: f"<!doctype html><html><head><meta charset='utf-8'/><meta name='viewport' content='width=device-width,initial-scale=1'/><script src='https://cdn.tailwindcss.com'></script><title>{title}</title></head><body class='{theme_bg}'>{header}<main class='max-w-6xl mx-auto px-6 pb-10'>{body}</main>{footer}</body></html>"
    home=skeleton(main,f"{name} | Home")
    services=skeleton("<h1 class='text-4xl font-bold'>Services</h1><p class='mt-3 opacity-80'>Service content mapped from intake and business type.</p>",f"{name} | Services")
    about=skeleton("<h1 class='text-4xl font-bold'>About</h1><p class='mt-3 opacity-80'>Trust narrative and positioning mapped from intake notes.</p>",f"{name} | About")
    contact=skeleton(f"<h1 class='text-4xl font-bold'>Contact</h1><p class='mt-3 opacity-80'>Email: {i.get('email','-')} · Phone: {i.get('phone','-')}</p><form class='mt-5 grid gap-3 max-w-xl'><input class='border rounded px-3 py-2 bg-black/20' placeholder='Name'><input class='border rounded px-3 py-2 bg-black/20' placeholder='Email'><textarea class='border rounded px-3 py-2 bg-black/20' rows='4' placeholder='Project details'></textarea><button class='w-fit px-5 py-3 rounded bg-cyan-400 text-slate-900 font-bold'>Submit</button></form>",f"{name} | Contact")
    return arche, {'index.html':home,'services.html':services,'about.html':about,'contact.html':contact}


def slug(s):
    s=s.lower().strip()
    s=re.sub(r'[^a-z0-9]+','-',s).strip('-')
    return s or 'site'

if __name__=='__main__':
    if len(sys.argv)<2:
        print('usage: generate.py intake.json [outdir]'); sys.exit(1)
    intake_path=Path(sys.argv[1])
    intake=json.loads(intake_path.read_text())
    out=Path(sys.argv[2]) if len(sys.argv)>2 else BASE/'generated'/slug(intake.get('businessName','site'))
    out.mkdir(parents=True, exist_ok=True)
    arche, pages=render(intake)
    for fn,txt in pages.items():
        (out/fn).write_text(txt)
    (out/'intake.json').write_text(json.dumps(intake,indent=2))
    (out/'meta.json').write_text(json.dumps({'archetype':arche},indent=2))
    print(str(out))
