import sys
import types
import unittest
from pathlib import Path
from unittest.mock import patch


SFT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SFT_ROOT))


class TokenizerStub:
    def convert_tokens_to_ids(self, token):
        return 1


class DatasetConfigurationTest(unittest.TestCase):
    def test_cfg_probability_is_preserved(self):
        vision_tokenizer = types.ModuleType("src.vision_tokenizer")
        vision_tokenizer.build_vision_tokenizer = lambda *args, **kwargs: None

        with patch.dict(sys.modules, {"src.vision_tokenizer": vision_tokenizer}):
            from src.utils.dataset_vr_train import VRTrainDataset

        dataset = VRTrainDataset(
            dataset_cfg={},
            tokenizer=TokenizerStub(),
            cfg_prob=0.75,
        )

        self.assertEqual(dataset.cfg_prob, 0.75)


if __name__ == "__main__":
    unittest.main()
