#!/usr/bin/env python3
"""Controlled crawler no-op/dry-run entrypoint."""
from __future__ import annotations
import argparse
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    print("CRAWLER DRY RUN PASS" if args.dry_run else "CRAWLER NO-OP PASS: network collection disabled by default")
    return 0
if __name__ == "__main__": raise SystemExit(main())
