import unittest
from lab import ParseError, parse_pipeline

class ShellPipelineTest(unittest.TestCase):
    def test_parses_pipeline_with_quotes(self):
        self.assertEqual(parse_pipeline('echo "hello world" | wc -c'), [['echo', 'hello world'], ['wc', '-c']])
    def test_rejects_empty_stage(self):
        with self.assertRaises(ParseError):
            parse_pipeline('echo ok | | wc')
    def test_rejects_empty_input(self):
        with self.assertRaises(ParseError):
            parse_pipeline('   ')
if __name__ == '__main__': unittest.main()
