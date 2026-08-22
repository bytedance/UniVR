import re
import unittest
from pathlib import Path


GAME_HTML = (
    Path(__file__).resolve().parents[1]
    / "examples"
    / "android_gui_cookbook"
    / "game_docker"
    / "number_game.html"
)


class NumberGameAccessibilityTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = GAME_HTML.read_text(encoding="utf-8")

    def test_number_cards_are_labeled_buttons(self):
        self.assertIn("document.createElement('button')", self.html)
        self.assertIn("card.type = 'button'", self.html)
        self.assertIn("card.setAttribute('aria-label'", self.html)
        self.assertIn(".card:focus-visible", self.html)

    def test_viewport_does_not_disable_zoom(self):
        viewport = re.search(
            r'<meta\s+name="viewport"\s+content="([^"]+)"',
            self.html,
        )
        self.assertIsNotNone(viewport)
        self.assertNotIn("user-scalable=no", viewport.group(1))


if __name__ == "__main__":
    unittest.main()
