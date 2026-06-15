#!/usr/bin/env python3
"""Audit tracked/staged files for likely secret leaks without printing values."""
from __future__ import annotations
from datetime import date
from pathlib import Path
import json, os, re, subprocess
ROOT=Path(__file__).resolve().parents[1]
DOCS=ROOT/"docs"; REGISTRY=ROOT/"registry"
TOKEN_PATTERNS=[
    ("classic_github_token_prefix", re.compile(r"ghp_[A-Za-z0-9_]{20,}")),
    ("fine_grained_github_token_prefix", re.compile(r"github_pat_[A-Za-z0-9_]{20,}")),
    ("private_key_block", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("bearer_secret_like_value", re.compile(r"Bearer\s+[A-Za-z0-9._~+/=-]{20,}")),
]
ASSIGN=re.compile(r"(?im)^\s*(GITHUB_TOKEN|password|api_key|private_key)\s*=\s*([^\s#]+)?")
PLACEHOLDERS={"","<token>","<value>","placeholder","redacted","changeme","example","xxx","xxxx"}
SKIP={".git"}
BIN={".zip",".png",".jpg",".jpeg",".gif",".pdf",".ico",".pyc"}
def git_lines(args):
    proc=subprocess.run(["git",*args],cwd=ROOT,text=True,stdout=subprocess.PIPE,stderr=subprocess.DEVNULL)
    return {line.strip().replace("\\","/") for line in proc.stdout.splitlines() if line.strip()}
def ignored(rel):
    return subprocess.run(["git","check-ignore","-q","--",rel],cwd=ROOT).returncode==0
def main():
    tracked=git_lines(["ls-files"])
    staged=git_lines(["diff","--cached","--name-only"])
    findings=[]
    for path in ROOT.rglob("*"):
        if path.is_dir() or path.suffix.lower() in BIN: continue
        rel=path.relative_to(ROOT).as_posix()
        if any(part in SKIP for part in Path(rel).parts): continue
        try: text=path.read_text(encoding="utf-8")
        except UnicodeDecodeError: text=path.read_text(encoding="utf-8", errors="ignore")
        except Exception: continue
        path_ignored=ignored(rel)
        path_tracked=rel in tracked
        path_staged=rel in staged
        for name,rx in TOKEN_PATTERNS:
            for m in rx.finditer(text):
                findings.append({"path":rel,"line":text.count("\n",0,m.start())+1,"pattern":name,"tracked":path_tracked,"staged":path_staged,"ignored":path_ignored})
        for m in ASSIGN.finditer(text):
            value=(m.group(2) or "").strip().strip("'\"")
            if value.lower() not in PLACEHOLDERS:
                findings.append({"path":rel,"line":text.count("\n",0,m.start())+1,"pattern":m.group(1)+"_non_placeholder_value","tracked":path_tracked,"staged":path_staged,"ignored":path_ignored})
    blocking=[f for f in findings if f["tracked"] or f["staged"]]
    DOCS.mkdir(exist_ok=True); REGISTRY.mkdir(exist_ok=True)
    lines=["# Secret Leak Audit","",f"Generated: {date.today().isoformat()}","",f"- Passed: {not blocking}",f"- Findings: {len(findings)}",f"- Blocking findings: {len(blocking)}","","| Path | Line | Pattern | Tracked | Staged | Ignored |","| --- | ---: | --- | --- | --- | --- |"]
    lines.extend(f"| {f['path']} | {f['line']} | {f['pattern']} | {f['tracked']} | {f['staged']} | {f['ignored']} |" for f in findings)
    (DOCS/"SECRET_LEAK_AUDIT.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
    (REGISTRY/"secret-leak-audit.json").write_text(json.dumps({"generated":date.today().isoformat(),"passed":not blocking,"findings":findings,"blocking_findings":blocking},indent=2),encoding="utf-8")
    print(f"SECRET LEAK AUDIT {'PASSED' if not blocking else 'FAILED'} ({len(findings)} findings, {len(blocking)} blocking)")
    return 0 if not blocking else 1
if __name__ == "__main__": raise SystemExit(main())
