"""Build deterministic, individually uploadable skill ZIPs or check for drift."""

import argparse
import io
import zipfile
from pathlib import Path


def archive_bytes(skill: Path, license_path: Path) -> bytes:
    if skill.is_symlink() or not (skill / "SKILL.md").is_file():
        raise ValueError(f"Invalid skill directory: {skill}")
    entries = {}
    for path in sorted(skill.rglob("*")):
        relative = path.relative_to(skill)
        if path.is_symlink():
            raise ValueError(f"Symlink cannot be packaged: {path}")
        if any(part.startswith(".") or part == "__pycache__" for part in relative.parts):
            raise ValueError(f"Unexpected local file in skill: {path}")
        if path.is_file():
            entries[f"{skill.name}/{relative.as_posix()}"] = path.read_bytes()
    license_name = f"{skill.name}/LICENSE"
    if license_name in entries:
        raise ValueError("Skill-local LICENSE conflicts with repository license")
    entries[license_name] = license_path.read_bytes()
    output = io.BytesIO()
    # Stored entries avoid compressor-version differences. These packages are small.
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_STORED) as archive:
        for name, content in sorted(entries.items()):
            info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            archive.writestr(info, content)
    return output.getvalue()


def sync_archives(skills: Path, output: Path, license_path: Path, check=False) -> int:
    roots = sorted(p.parent for p in skills.glob("*/SKILL.md"))
    if not roots:
        raise ValueError(f"No skills found in {skills}")
    expected = {f"{root.name}.zip": archive_bytes(root, license_path) for root in roots}
    existing = {p.name for p in output.glob("*.zip")}
    stale = existing - expected.keys()
    if stale:
        raise ValueError(f"Remove obsolete generated archives explicitly: {sorted(stale)}")
    if not check:
        output.mkdir(parents=True, exist_ok=True)
    problems = 0
    for name, data in expected.items():
        path = output / name
        if check:
            if not path.is_file() or path.read_bytes() != data:
                print(f"ERROR: missing or outdated archive: {name}")
                problems += 1
        else:
            path.write_bytes(data)
            print(f"Built {name} ({len(data)} bytes)")
    if check and not problems:
        print(f"OK: {len(expected)} archives match skill source and license")
    return int(problems > 0)


def main() -> int:
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("--check", action="store_true", help="Fail on missing or changed ZIPs")
    args = cli.parse_args()
    root = Path(__file__).resolve().parents[1]
    try:
        return sync_archives(root / "skills", root / "downloads", root / "LICENSE", args.check)
    except ValueError as error:
        print(f"ERROR: {error}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
