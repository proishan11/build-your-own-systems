import subprocess
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ErrorCountsTest(unittest.TestCase):
    def test_error_counts(self):
        result = subprocess.run(
            ["bash", "solutions/error_counts.sh"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(
            result.stdout.strip().splitlines(),
            ["3 /api/orders", "2 /api/search", "1 /api/users"],
        )


if __name__ == "__main__":
    unittest.main()

