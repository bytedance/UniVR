import sys
import unittest
from pathlib import Path

import torch


SFT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SFT_ROOT))

from src.utils.input_utils import ensure_bos_token


class EnsureBosTokenTest(unittest.TestCase):
    def test_prepends_bos_with_input_dtype_and_device(self):
        input_ids = torch.tensor([[7, 8]], dtype=torch.long)

        result = ensure_bos_token(input_ids, 203)

        self.assertEqual(result.tolist(), [[203, 7, 8]])
        self.assertEqual(result.dtype, input_ids.dtype)
        self.assertEqual(result.device, input_ids.device)

    def test_leaves_existing_bos_unchanged(self):
        input_ids = torch.tensor([[203, 7, 8]], dtype=torch.long)

        result = ensure_bos_token(input_ids, 203)

        self.assertIs(result, input_ids)


if __name__ == "__main__":
    unittest.main()
