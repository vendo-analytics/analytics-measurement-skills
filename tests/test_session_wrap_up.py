"""Portable package checks for the session-wrap-up skill."""

import io
import unittest
import zipfile
from pathlib import Path

from scripts.package_skills import archive_bytes
from scripts.validate import validate_skill


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "session-wrap-up"


class SessionWrapUpPackageTests(unittest.TestCase):
    def test_standalone_skill_is_valid(self):
        self.assertEqual([], validate_skill(SKILL))

    def test_archive_contains_instructions_reference_and_license(self):
        with zipfile.ZipFile(io.BytesIO(archive_bytes(SKILL, ROOT / "LICENSE"))) as archive:
            self.assertEqual(set(archive.namelist()), {
                "session-wrap-up/SKILL.md",
                "session-wrap-up/references/session-record-format.md",
                "session-wrap-up/LICENSE",
            })


if __name__ == "__main__":
    unittest.main()
