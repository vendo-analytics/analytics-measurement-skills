"""Archive fidelity and drift checks independent of host upload behavior."""

import contextlib
import io
import os
import tempfile
import unittest
import zipfile
from pathlib import Path

from scripts.package_skills import archive_bytes, sync_archives


class ArchiveTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.skill = self.root / "skills" / "sample"
        (self.skill / "references").mkdir(parents=True)
        (self.skill / "SKILL.md").write_text("Instructions\n")
        (self.skill / "references" / "guide.md").write_text("Reference café\n")
        self.license = self.root / "LICENSE"
        self.license.write_text("License terms\n")

    def test_round_trip_contains_only_skill_and_license(self):
        (self.root / "README.md").write_text("Repository-only marketing")
        with zipfile.ZipFile(io.BytesIO(archive_bytes(self.skill, self.license))) as archive:
            self.assertEqual(set(archive.namelist()), {
                "sample/SKILL.md", "sample/references/guide.md", "sample/LICENSE"})
            archive.extractall(self.root / "extracted")
        for source in self.skill.rglob("*"):
            if source.is_file():
                self.assertEqual(source.read_bytes(),
                                 (self.root / "extracted/sample" / source.relative_to(self.skill)).read_bytes())
        self.assertEqual(self.license.read_bytes(),
                         (self.root / "extracted/sample/LICENSE").read_bytes())

    def test_build_does_not_depend_on_source_timestamps(self):
        before = archive_bytes(self.skill, self.license)
        os.utime(self.skill / "SKILL.md", (1700000000, 1700000000))
        self.assertEqual(before, archive_bytes(self.skill, self.license))

    def test_missing_stale_and_tampered_archives_are_detected(self):
        output = self.root / "downloads"
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(1, sync_archives(self.skill.parent, output, self.license, check=True))
            self.assertEqual(0, sync_archives(self.skill.parent, output, self.license))
            self.assertEqual(0, sync_archives(self.skill.parent, output, self.license, check=True))
            (self.skill / "references/guide.md").write_text("Changed reference")
            self.assertEqual(1, sync_archives(self.skill.parent, output, self.license, check=True))
            sync_archives(self.skill.parent, output, self.license)
            (output / "sample.zip").write_bytes(b"not a ZIP")
            self.assertEqual(1, sync_archives(self.skill.parent, output, self.license, check=True))

    def test_obsolete_archives_are_not_silently_distributed(self):
        output = self.root / "downloads"
        output.mkdir()
        (output / "removed-skill.zip").write_bytes(b"old")
        with self.assertRaises(ValueError):
            sync_archives(self.skill.parent, output, self.license, check=True)

    def test_symlinks_and_hidden_local_files_are_rejected(self):
        path = self.skill / "linked-license"
        path.symlink_to(self.license)
        with self.assertRaises(ValueError):
            archive_bytes(self.skill, self.license)
        path.unlink()
        (self.skill / ".env").write_text("local configuration")
        with self.assertRaises(ValueError):
            archive_bytes(self.skill, self.license)


if __name__ == "__main__":
    unittest.main()
