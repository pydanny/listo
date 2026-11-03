import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path


MAKE = shutil.which("make")
ROOT = Path(__file__).resolve().parents[1]


@unittest.skipUnless(MAKE, "make is required to check the quality target")
class QualityCommandTests(unittest.TestCase):
    def test_qa_file_does_not_suppress_quality_checks(self):
        make = MAKE
        assert make is not None
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            shutil.copyfile(ROOT / "Makefile", directory / "Makefile")
            shutil.copyfile(ROOT / "pyproject.toml", directory / "pyproject.toml")

            def planned_commands():
                result = subprocess.run(
                    [make, "-n", "qa"],
                    cwd=directory,
                    env={"PATH": "/usr/bin:/bin", "LC_ALL": "C"},
                    capture_output=True,
                    text=True,
                    timeout=15,
                )
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(result.stderr, "")
                return result.stdout

            before = planned_commands()
            self.assertIn("ruff check", before)
            (directory / "qa").write_text("An unrelated local file\n")
            self.assertEqual(planned_commands(), before)
