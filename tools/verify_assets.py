#!/usr/bin/env python3
"""Verify the complete static site assets and optional generated offline HTML."""
import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / 'docs'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--offline', type=Path, help='Validate generated standalone HTML exists and is self-contained')
    args = parser.parse_args()
    errors = []
    cards = json.loads((SITE / 'cards.json').read_text(encoding='utf-8'))
    sources = []
    for i, card in enumerate(cards, 1):
        name, rel = card.get('name'), card.get('src')
        if not name or not rel:
            errors.append(f'Card #{i} missing name or src')
            continue
        p = (SITE / rel).resolve()
        if not p.is_relative_to(SITE.resolve()):
            errors.append(f'Card #{i} image escapes the site: {rel}')
            continue
        sources.extend([p, p.with_name(p.stem + '-art.jpg')])
    for p in sources:
        if not p.is_file():
            errors.append(f'Missing referenced image: {p.relative_to(ROOT)}')
    for name in ('index.html', 'engine.js', 'app.js', 'style.css', 'rules.pdf', 'favicon.svg'):
        if not (SITE / name).is_file():
            errors.append(f'Missing website file: {name}')
    js = (SITE / 'app.js').read_text(encoding='utf-8')
    if "fetch('cards.json')" not in js:
        errors.append('Expected card-fetch contract changed: update the offline builder')
    if args.offline:
        if not args.offline.is_file():
            errors.append(f'Offline HTML is missing: {args.offline}')
        else:
            html = args.offline.read_text(encoding='utf-8')
            for needle in ('const EMBEDDED_CARDS=', 'data:image/jpeg;base64,', 'data:application/pdf;base64,', 'data:image/svg+xml;base64,'):
                if needle not in html:
                    errors.append(f'Offline HTML missing embedded resource: {needle}')
            for forbidden in ('<script src="engine.js"', 'href="style.css"', "await fetch('cards.json')"):
                if forbidden in html:
                    errors.append(f'Offline HTML contains external dependency: {forbidden}')
    if errors:
        print('FAIL — asset verification:')
        for e in errors: print(' -', e)
        return 1
    print(f'PASS — {len(cards)} cards, {len(sources)} card images, website files' + (', self-contained offline edition' if args.offline else ''))
    return 0


if __name__ == '__main__':
    sys.exit(main())
