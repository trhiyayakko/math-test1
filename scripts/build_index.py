#!/usr/bin/env python3
import os, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTES = ROOT / "notes"
INDEX = {}

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)

def parse_frontmatter(text):
    m = FRONTMATTER_RE.match(text)
    if not m: return {}
    block = m.group(1)
    data = {}
    for line in block.splitlines():
        if not line.strip() or line.strip().startswith("#"): continue
        if ":" in line:
            k, v = line.split(":", 1)
            k = k.strip()
            v = v.strip()
            if v.startswith("[") and v.endswith("]"):
                try:
                    data[k] = json.loads(v.replace("'", '"'))
                except Exception:
                    data[k] = []
            else:
                data[k] = v
    # normalize lists
    for key in ("requires","authors","refs","tags"):
        data[key] = data.get(key, [])
        if isinstance(data[key], str):
            data[key] = [data[key]]
    return data

def main():
    errors = []
    for md in NOTES.rglob("*.md"):
        txt = md.read_text(encoding="utf-8", errors="ignore")
        fm = parse_frontmatter(txt)
        if not fm.get("id"):
            errors.append(f"[NO_ID] {md}")
            continue
        _id = fm["id"]
        if _id in INDEX:
            errors.append(f"[DUPLICATE_ID] {_id} in {md}")
        INDEX[_id] = {
            "path": str(md.relative_to(ROOT)),
            "title": fm.get("title",""),
            "kind": fm.get("kind",""),
            "requires": fm.get("requires",[]),
            "status": fm.get("status","draft"),
            "tags": fm.get("tags",[])
        }

    # 未定義参照をチェック
    for _id, info in INDEX.items():
        for dep in info["requires"]:
            if dep not in INDEX:
                errors.append(f"[UNDEFINED_REF] {info['path']} requires {dep}")

    # 保存
    (ROOT / "index.json").write_text(
        json.dumps(INDEX, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )

    if errors:
        print("::group::Validation errors")
        for e in errors: print(e)
        print("::endgroup::")
        print(f"Found {len(errors)} error(s).")
        sys.exit(1)
    else:
        print(f"Indexed {len(INDEX)} notes. OK.")

if __name__ == "__main__":
    main()
