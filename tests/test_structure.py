"""Course structure checks: 36 lessons, 75 tasks, 60 Q&As, 3 projects."""
from pathlib import Path
import json
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


class CourseStructureTests(unittest.TestCase):
    def test_36_technical_lessons(self):
        for level in ("basics", "intermediate", "advanced"):
            docs = sorted((ROOT / level / "lessons").glob("*.md"))
            self.assertEqual(len(docs), 12, level)
            self.assertEqual([p.name[:2] for p in docs], [f"{i:02}" for i in range(12)])
            for path in docs:
                with self.subTest(path=path):
                    text = path.read_text(encoding="utf-8")
                    self.assertGreaterEqual(len(text.split()), 210)
                    self.assertEqual(len(re.findall(r"(?m)^### [1-4]\. ", text)), 4)
                    self.assertIn(chr(96) * 3 + "bash", text)
                    self.assertIn("## Interview", text)

    def test_75_practice_questions(self):
        for level in ("basics", "intermediate", "advanced"):
            text = (ROOT / "exercises" / f"{level}.md").read_text(encoding="utf-8")
            self.assertEqual(len(re.findall(r"(?m)^\d+\. ", text)), 25)

    def test_60_interview_questions(self):
        for level in ("basics", "intermediate", "advanced"):
            text = (ROOT / "interview" / f"{level}.md").read_text(encoding="utf-8")
            self.assertEqual(len(re.findall(r"(?m)^\d+\. \*\*", text)), 20)

    def test_project_examples(self):
        self.assertEqual(len(list((ROOT / "projects").glob("[0-9][0-9]_*.md"))), 3)
        self.assertEqual(len(list((ROOT / "projects/examples").glob("*.sh"))), 4)

    def test_twelve_labs(self):
        tasks = json.loads((ROOT / "labs/tasks.json").read_text(encoding="utf-8"))
        self.assertEqual(len(tasks), 12)
        for task in tasks:
            self.assertTrue((ROOT / "labs/starter" / task["script"]).is_file())
            self.assertTrue((ROOT / "labs/reference" / task["script"]).is_file())

    def test_core_docs(self):
        for file in ("README.md", "SAFETY.md", "GLOSSARY.md", "CHEATSHEET.md",
                     "ASSESSMENT.md", "CURRICULUM.md", "interview/MOCK_INTERVIEWS.md"):
            self.assertTrue((ROOT / file).is_file(), file)


if __name__ == "__main__":
    unittest.main()
