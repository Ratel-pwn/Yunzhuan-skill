#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
from pathlib import Path


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Save proofread transcript safely.")
    p.add_argument("--source", required=True, type=Path, help="Original file path")
    p.add_argument("--text-file", required=True, type=Path, help="Path to corrected text content")
    p.add_argument(
        "--mode",
        choices=["local-copy", "overwrite", "save-as"],
        default="local-copy",
        help="Save mode: local-copy (same folder), overwrite, or save-as",
    )
    p.add_argument("--output", type=Path, default=None, help="Output file path for save-as mode")
    p.add_argument("--copy-suffix", default=".proofread", help="Suffix for local-copy mode")
    p.add_argument("--no-backup", action="store_true", help="Disable .bak backup when overwriting")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    if not args.source.exists():
        raise FileNotFoundError(f"source not found: {args.source}")
    if not args.text_file.exists():
        raise FileNotFoundError(f"text file not found: {args.text_file}")

    if args.mode == "save-as":
        if args.output is None:
            raise ValueError("--output is required when --mode save-as")
        out = args.output
    elif args.mode == "overwrite":
        out = args.source
    else:
        out = args.source.with_name(f"{args.source.stem}{args.copy_suffix}{args.source.suffix}")

    out.parent.mkdir(parents=True, exist_ok=True)
    corrected = args.text_file.read_text(encoding="utf-8")

    if args.mode == "overwrite" and not args.no_backup:
        backup = args.source.with_suffix(args.source.suffix + ".bak")
        shutil.copy2(args.source, backup)
        print(f"[OK] backup: {backup}")

    out.write_text(corrected, encoding="utf-8")
    print(f"[OK] wrote: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
