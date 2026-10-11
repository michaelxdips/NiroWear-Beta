"""Fail-closed public landing check. Stdlib only; never publishes or uploads."""
import hashlib
import json
import re
import struct
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCREENS = {'chat-home.png', 'real-response.png', 'streaming-stop.png', 'table-record.png', 'code-reader.png', 'history.png'}
LEGAL = {'ANDROIDX-NATIVE-NOTICES.txt', 'APACHE-HARMONY-NOTICE.txt', 'APACHE-HTTPCOMPONENTS-CORE-NOTICE.txt',
         'ATTRIBUTIONS.txt', 'AUTOLINK-MIT.txt', 'COMMONMARK-BSD-2-Clause.txt', 'COROUTINES-LICENSE.txt',
         'COROUTINES-NOTICE.txt', 'DATASTORE-PROTOBUF-BSD-3-Clause.txt', 'JETBRAINS-ANNOTATIONS-LICENSE.txt',
         'KOTLIN-BOOST-1.0.txt', 'KOTLIN-COPYRIGHT.txt', 'KOTLIN-LICENSE.txt', 'KOTLIN-THREETENBP-BSD-3-Clause.txt',
         'LICENSE-809fa1ed2145.txt', 'MATERIAL_ICONS_LICENSE.txt', 'MATERIAL_ICONS_NOTICE.txt', 'MPL-2.0.txt',
         'PROTOBUF-UPSTREAM-SUPPLEMENTAL.txt', 'PUBLIC_SUFFIX_LIST-NOTICE.txt', 'PUBLIC_SUFFIX_LIST.dat',
         'SERIALIZATION-LICENSE.txt', 'SERIALIZATION-NOTICE.txt'}
ALLOWED = {'README.md', 'PRIVACY.md', 'THIRD_PARTY_NOTICES.md', '.gitignore', 'CHANGELOG.md', 'SECURITY.md', 'COPYRIGHT.md', 'CONTRIBUTING.md',
           'docs/USER_GUIDE.md', 'docs/TROUBLESHOOTING.md',
           '.github/ISSUE_TEMPLATE/developer-collaboration.yml', '.github/ISSUE_TEMPLATE/device-feedback.yml', '.github/ISSUE_TEMPLATE/config.yml',
           '.github/ISSUE_TEMPLATE/bug-report.yml', '.github/ISSUE_TEMPLATE/feature-request.yml',
           '.github/check_public.py', '.github/public-assets.json', '.github/workflows/public-hygiene.yml'}
ALLOWED |= {'docs/screenshots/' + n for n in SCREENS} | {'docs/licenses/' + n for n in LEGAL}
BRAND = {'docs/branding/nirowear-icon.png', 'docs/branding/nirowear-mark.svg'}
ALLOWED |= BRAND | {'docs/branding/PROVENANCE.md'}

def check_text(name, data):
    text = data.decode('utf-8')
    # Pattern expressions in this checker are literals, not credential values.
    if name != '.github/check_public.py':
        assert not re.search(r'(?i)([A-Z]:\\(?:Users|Temp)\\|/Users/|/home/|docs/memory/|artifacts/|AGENTS\.md|-----BEGIN [A-Z ]*PRIVATE KEY-----|gh[pousr]_[A-Za-z0-9]{20,}|sk-[A-Za-z0-9]{20,}|AIza[A-Za-z0-9_-]{30,})', text), name
    assert not text.startswith('version https://git-lfs.github.com/spec/v1\n'), 'LFS pointer: ' + name
    if name.endswith('.md'):
        assert len(re.findall(r'<details(?:\s[^>]*)?>', text)) == len(re.findall(r'</details>', text)), 'Unclosed disclosure: ' + name
        for disclosure in re.findall(r'<details(?:\s[^>]*)?>(.*?)</details>', text, re.S):
            summary = re.search(r'<summary>(.*?)</summary>', disclosure, re.S)
            assert summary and re.sub(r'<[^>]+>', '', summary.group(1)).strip(), 'Missing disclosure summary: ' + name
        assert not re.search(r'(?im)^#{1,6}\s+(?:roadmap|upcoming features|coming soon|planned architecture|future integrations|internal priorities|unreleased)\b', text), 'Unpublished direction: ' + name
        assert not re.search(r'(?i)0\.\d+\.\d+-beta\.\d+-dev|docs/memory|internal backlog|release candidate', text), 'Private development disclosure: ' + name
        for pair in re.findall(r'\]\(([^)]+)\)|src="([^"]+)"', text):
            link = next(x for x in pair if x)
            target, _, anchor = link.partition('#')
            if not re.match(r'https?://', link):
                resolved = (ROOT / name).parent / target if target else ROOT / name
                assert resolved.resolve().is_relative_to(ROOT.resolve()) and resolved.is_file(), (name, target)
                if anchor and resolved.suffix == '.md':
                    headings = re.findall(r'^#{1,6}\s+(.+?)\s*#*$', resolved.read_text(encoding='utf-8'), re.M)
                    ids = set()
                    counts = {}
                    for heading in headings:
                        slug = re.sub(r'[^\w\- ]', '', heading.lower()).replace(' ', '-')
                        count = counts.get(slug, 0)
                        counts[slug] = count + 1
                        ids.add(slug + ('-' + str(count) if count else ''))
                    assert anchor in ids, (name, 'Broken anchor', link)
        for image in re.findall(r'!\[([^\]]*)\]\(', text):
            assert image.strip(), 'Missing image alt text: ' + name
        for tag in re.findall(r'<img\b[^>]*>', text):
            assert re.search(r'alt="[^"\s][^"]*"', tag), 'Missing image alt text: ' + name

def main():
    disk = {p.relative_to(ROOT).as_posix(): p for p in ROOT.rglob('*')
            if p.is_file() and '.git' not in p.relative_to(ROOT).parts}
    assert set(disk) == ALLOWED, {'unexpected': sorted(set(disk) - ALLOWED), 'missing': sorted(ALLOWED - set(disk))}
    immutable = json.loads((ROOT / '.github/public-assets.json').read_text())
    assert set(immutable) == {'docs/screenshots/' + n for n in SCREENS} | {'docs/licenses/' + n for n in LEGAL} | BRAND
    copyright_text = (ROOT / 'COPYRIGHT.md').read_text(encoding='utf-8')
    assert 'Copyright © 2026 Stephen Michael' in copyright_text and 'proprietary' in copyright_text
    assert 'COPYRIGHT.md' in (ROOT / 'README.md').read_text(encoding='utf-8')
    for name in ['README.md', 'COPYRIGHT.md', 'PRIVACY.md', 'SECURITY.md', 'CHANGELOG.md']:
        text = (ROOT / name).read_text(encoding='utf-8')
        assert not re.search(r'NiroWear\s*(?:®|™)|NiroWear.{0,30}registered trademark|legally certified|GDPR compliant|CCPA compliant|HIPAA compliant', text, re.I), name
    for name, p in disk.items():
        assert not p.is_symlink() and p.stat().st_size < 2_000_000, name
        data = p.read_bytes()
        if name in immutable:
            assert hashlib.sha256(data).hexdigest() == immutable[name], 'Approved asset changed: ' + name
        if name.endswith('.png'):
            size = (512, 512) if name in BRAND else (466, 466)
            assert data[:8] == b'\x89PNG\r\n\x1a\n' and struct.unpack('>II', data[16:24]) == size, name
        else:
            check_text(name, data)
    tracked = subprocess.check_output(['git', 'ls-files', '-z'], cwd=ROOT).decode().split('\0')
    assert set(filter(None, tracked)) == ALLOWED, 'Git index differs from allowlist'
    modes = subprocess.check_output(['git', 'ls-files', '--stage'], cwd=ROOT).decode()
    assert not re.search(r'^(160000|120000) ', modes, re.M), 'Submodule or symlink forbidden'
    for name, p in disk.items():
        staged = subprocess.check_output(['git', 'show', ':' + name], cwd=ROOT)
        assert staged == p.read_bytes(), 'Unreviewed index bytes: ' + name
    identities = subprocess.check_output(['git', 'log', '-1', '--format=%ae%n%ce'], cwd=ROOT).decode().splitlines()
    assert len(identities) == 2 and all(i.endswith('@users.noreply.github.com') for i in identities), 'Public commit must use GitHub no-reply metadata'
    print(f'PASS: {len(ALLOWED)} exact allowlisted files, approved screenshot/legal hashes, no source/APK/private files, relative links and bounded secret scan')

if __name__ == '__main__':
    main()
