import sys
import unittest

from minishell import ShellError, parse, run


class MiniShellTest(unittest.TestCase):
    def test_parse_respects_quotes(self):
        self.assertEqual(parse('echo "hello world"'), ["echo", "hello world"])

    def test_parse_rejects_empty_command(self):
        with self.assertRaises(ShellError):
            parse("   ")

    def test_run_captures_stdout_and_exit_code(self):
        result = run(f'{sys.executable} -c "print(123)"')
        self.assertEqual(result.code, 0)
        self.assertEqual(result.stdout.strip(), "123")
        self.assertEqual(result.stderr, "")

    def test_run_captures_stderr(self):
        result = run(f'{sys.executable} -c "import sys; print(456, file=sys.stderr); sys.exit(7)"')
        self.assertEqual(result.code, 7)
        self.assertEqual(result.stdout, "")
        self.assertEqual(result.stderr.strip(), "456")


if __name__ == "__main__":
    unittest.main()

