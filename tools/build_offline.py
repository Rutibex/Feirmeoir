#!/usr/bin/env python3
"""Create Feirmeoir.html and optionally a ready-to-upload offline ZIP.

Usage (repository root): python tools/build_offline.py --zip
No pip dependencies are required.
"""
import argparse
import base64
import json
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / 'docs'
VERSION = 'v0.1.0'


def data_url(path: Path, mime: str) -> str:
    return 'data:' + mime + ';base64,' + base64.b64encode(path.read_bytes()).decode('ascii')


def replace_once(document: str, original: str, replacement: str, name: str) -> str:
    if document.count(original) != 1:
        raise ValueError(f'Expected exactly one {name} in the website, found {document.count(original)}')
    return document.replace(original, replacement, 1)


def build(output: Path) -> None:
    cards = json.loads((SITE / 'cards.json').read_text(encoding='utf-8'))
    for card in cards:
        src = SITE / card['src']
        art = src.with_name(src.stem + '-art.jpg')
        if not src.is_file() or not art.is_file():
            raise FileNotFoundError(f'Missing artwork for {card["name"]}: {src} or {art}')
        card['art'] = data_url(art, 'image/jpeg')
        card['src'] = data_url(src, 'image/jpeg')

    index = (SITE / 'index.html').read_text(encoding='utf-8')
    css = (SITE / 'style.css').read_text(encoding='utf-8')
    engine = (SITE / 'engine.js').read_text(encoding='utf-8')
    app = (SITE / 'app.js').read_text(encoding='utf-8')
    fetch_cards = "fetch('cards.json').then(r=>{if(!r.ok)throw Error('Card data unavailable');return r.json()})"
    app = replace_once(app, fetch_cards, 'Promise.resolve(EMBEDDED_CARDS)', 'card fetch')
    index = replace_once(index, '<link rel="stylesheet" href="style.css">', '<style>\n' + css + '\n</style>', 'stylesheet')
    encoded = json.dumps(cards, separators=(',', ':'), ensure_ascii=True).replace('<', '\\u003c')
    script = '<script>const EMBEDDED_CARDS=' + encoded + ';\n' + engine + '\n' + app + '\n</script>'
    index = replace_once(index, '<script src="engine.js"></script><script src="app.js"></script>', script, 'script includes')
    index = replace_once(index, 'href="rules.pdf"', 'href="' + data_url(SITE / 'rules.pdf', 'application/pdf') + '"', 'rules PDF')
    index = replace_once(index, 'href="favicon.svg"', 'href="' + data_url(SITE / 'favicon.svg', 'image/svg+xml') + '"', 'favicon')
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(index, encoding='utf-8')
    print(f'Wrote {output} ({output.stat().st_size:,} bytes)')


def main():
    parser = argparse.ArgumentParser(description='Build Feirmeoir as a standalone offline browser game')
    parser.add_argument('--output', type=Path, default=ROOT / 'build' / 'Feirmeoir.html', help='Destination HTML file')
    parser.add_argument('--zip', action='store_true', help='Also create the offline release ZIP alongside the HTML')
    args = parser.parse_args()
    output = args.output.resolve()
    build(output)
    if args.zip:
        archive = output.parent / f'Feirmeoir-{VERSION}-Offline.zip'
        with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as z:
            z.write(output, 'Feirmeoir.html')
            z.writestr('PLAY.txt', (
                'FEIRMEOIR — A FAMILY, A FARM, A FUTURE\n'
                'Board game by Michael Robinson\n\n'
                '1. Unzip this archive.\n'
                '2. Double-click Feirmeoir.html in a modern desktop browser.\n'
                '3. Choose New game (or Begin your story), select 1–4 families, and play.\n\n'
                'No internet or installation is required. Rules and art are embedded.\n'
                'Save data lives in your browser storage, if local-file storage is supported.\n'
                'No AI opponents or online multiplayer.\n'
                'Copyright 2026 Michael Robinson. All rights reserved.\n'
            ))
            z.write(ROOT / 'LICENSE.md', 'LICENSE.md')
        print(f'Wrote {archive} ({archive.stat().st_size:,} bytes)')


if __name__ == '__main__':
    main()
