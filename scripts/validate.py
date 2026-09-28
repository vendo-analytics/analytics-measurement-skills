"""Validate portable skill metadata and local resource boundaries.

External URLs and Markdown fragments are not checked. Accept either a collection
directory or one skill directory, including a copy installed in another project.
"""

import argparse
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml
from markdown_it import MarkdownIt


def validate_skill(root: Path) -> list[str]:
    root = root.resolve()
    errors = []
    entry = root / "SKILL.md"
    if not entry.is_file():
        return ["SKILL.md is missing"]
    content = entry.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---(?:\n|$)", content, re.S)
    if not match:
        errors.append("SKILL.md needs YAML frontmatter")
    else:
        try:
            metadata = yaml.safe_load(match.group(1))
        except yaml.YAMLError:
            metadata = None
        if not isinstance(metadata, dict):
            errors.append("Frontmatter must be a YAML mapping")
        else:
            name = metadata.get("name")
            if (not isinstance(name, str) or len(name) > 64
                    or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name)
                    or name != root.name):
                errors.append("Name must match its folder and use lowercase hyphen-case")
            description = metadata.get("description")
            if (not isinstance(description, str) or not description.strip()
                    or len(description) > 1024 or "[TODO:" in description):
                errors.append("Description must be complete and between 1 and 1024 characters")
            if not content[match.end():].strip():
                errors.append("Skill instructions are empty")

    parser = MarkdownIt()
    for path in sorted(root.rglob("*")):
        if path.is_symlink():
            errors.append(f"{path.relative_to(root)}: package resources must be real files")
            continue
        if not path.is_file() or path.suffix != ".md":
            continue
        source = path.read_text(encoding="utf-8")
        if re.search(r"/Users/|/home/|\bVendo\b|vendodata|To Do/", source, re.I):
            errors.append(f"{path.relative_to(root)}: local-machine or maintainer content in skill")
        for token in parser.parse(source):
            for child in token.children or []:
                if child.type not in {"link_open", "image"}:
                    continue
                target = child.attrGet("href" if child.type == "link_open" else "src")
                url = urlsplit(target or "")
                if url.scheme in {"https", "http", "mailto"} or url.netloc:
                    continue
                if not url.path and not url.scheme:
                    continue
                resolved = (path.parent / unquote(url.path)).resolve()
                label = f"{path.relative_to(root)}: {target}"
                if url.scheme or not resolved.is_relative_to(root):
                    errors.append(f"{label}: resource escapes this skill")
                elif not resolved.is_file():
                    errors.append(f"{label}: resource file does not exist")
    return errors


def main() -> int:
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("path", nargs="?", type=Path,
                     default=Path(__file__).resolve().parents[1] / "skills")
    args = cli.parse_args()
    roots = ([args.path] if (args.path / "SKILL.md").exists()
             else sorted(p.parent for p in args.path.glob("*/SKILL.md")))
    if not roots:
        print(f"ERROR: no skills found in {args.path}")
        return 1
    count = 0
    for root in roots:
        errors = validate_skill(root)
        count += len(errors)
        for error in errors:
            print(f"ERROR {root.name}: {error}")
        if not errors:
            print(f"OK {root.name}")
    print(f"Checked {len(roots)} skills; {count} errors")
    return int(count > 0)


if __name__ == "__main__":
    raise SystemExit(main())
