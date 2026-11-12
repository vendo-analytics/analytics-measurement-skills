"""Portable package checks for the onboarding skill."""

import io
import unittest
import zipfile
from pathlib import Path

from scripts.package_skills import archive_bytes
from scripts.validate import validate_skill


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "onboarding"


class OnboardingPackageTests(unittest.TestCase):
    def test_standalone_skill_is_valid(self):
        self.assertEqual([], validate_skill(SKILL))

    def test_archive_contains_instructions_reference_and_license(self):
        with zipfile.ZipFile(io.BytesIO(archive_bytes(SKILL, ROOT / "LICENSE"))) as archive:
            self.assertEqual(set(archive.namelist()), {
                "onboarding/SKILL.md",
                "onboarding/references/workspace-format.md",
                "onboarding/LICENSE",
            })


if __name__ == "__main__":
    unittest.main()
