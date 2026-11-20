"""Integration tests for all 12 Linux/Bash reference labs."""
import sys
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from grade import TASKS, INDEX, grade


class LinuxLabTests(unittest.TestCase):
    def test_twelve_tasks(self):
        self.assertEqual(len(TASKS), 12)
        self.assertEqual(len(INDEX), 12)
        for level in ("basics", "intermediate", "advanced"):
            self.assertEqual(sum(t["level"] == level for t in TASKS), 4)

    def test_reference_solutions_pass(self):
        for id in INDEX:
            with self.subTest(lab=id):
                ok, message = grade(id, reference=True)
                self.assertTrue(ok, message)

    def test_starters_require_implementation(self):
        for id in INDEX:
            with self.subTest(lab=id):
                ok, _ = grade(id)
                self.assertFalse(ok)


if __name__ == "__main__":
    unittest.main()
