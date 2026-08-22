import re
import unittest
from pathlib import Path


SFT_ROOT = Path(__file__).resolve().parents[1]


def read_use_lora_flag(script_name: str) -> str:
    script = (SFT_ROOT / "scripts" / script_name).read_text(encoding="utf-8")
    match = re.search(r"^\s*--use_lora\s+(True|False)\s*\\\s*$", script, re.MULTILINE)
    if match is None:
        raise AssertionError(f"{script_name} does not set --use_lora explicitly")
    return match.group(1)


class TrainingLauncherTest(unittest.TestCase):
    def test_full_launcher_disables_lora(self):
        self.assertEqual(read_use_lora_flag("train_sft_full.sh"), "False")

    def test_lora_launcher_enables_lora(self):
        self.assertEqual(read_use_lora_flag("train_sft_lora.sh"), "True")


if __name__ == "__main__":
    unittest.main()
