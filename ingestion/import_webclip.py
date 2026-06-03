#!/usr/bin/env python3
"""Placeholder ingestion utility."""
from pathlib import Path
import argparse
ROOT = Path(__file__).resolve().parents[1]
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source", nargs="?")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    print("INGESTION PLACEHOLDER PASS" + (" (dry-run)" if args.dry_run else ""))
    return 0
if __name__ == "__main__": raise SystemExit(main())
