#!/usr/bin/env python3
"""Check tracked text for forbidden restricted-source locators; never prints contents.

This is an accidental-import guard, not a semantic DLP classifier. Review remains required.
"""
import re
import subprocess
import zipfile
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
REPO = "carrieros-ai/" + "carrier-os-cluster"
MODULE = "carrier" + "_cluster"
PATTERNS = [re.compile(re.escape(REPO) + r"(?:@[a-f0-9]{7,40}:|/(?:blob|tree)/)", re.I), re.compile(re.escape(MODULE) + r"(?:/|\.)[a-zA-Z_]")]
def restricted(text): return any(p.search(text) for p in PATTERNS)
def main():
    tracked = subprocess.check_output(["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard"],cwd=ROOT).decode().split("\0")
    failures = []
    for relative in sorted(set(tracked)):
        if not relative: continue
        p=ROOT/relative
        if p==Path(__file__).resolve(): continue
        if p.is_symlink():
            try: p.resolve().relative_to(ROOT)
            except ValueError: failures.append(relative); continue
        if not p.is_file(): continue
        if p.suffix.lower() in {'.zip','.docx','.xlsx','.pptx'}:
            try:
                with zipfile.ZipFile(p) as archive:
                    members=archive.infolist()
                    if len(members)>10000 or sum(m.file_size for m in members)>100_000_000: raise ValueError('archive exceeds bounded inspection')
                    if any(restricted(m.filename) or restricted(archive.read(m).decode('utf-8',errors='replace')) for m in members if not m.is_dir()): failures.append(relative)
            except (OSError,ValueError,RuntimeError,zipfile.BadZipFile): failures.append(relative)
        if p.suffix.lower() in {'.md','.txt','.json','.jsonl','.yaml','.yml','.html','.svg','.py','.js','.ts','.mjs'}:
            if restricted(p.read_text(encoding='utf-8',errors='replace')): failures.append(relative)
    if failures:
        print('FAIL: restricted source references found in ' + ', '.join(failures))
        return 1
    print('PASS: no forbidden restricted-source locators in tracked text; manual design-content review is still required')
    return 0
if __name__=='__main__': raise SystemExit(main())
