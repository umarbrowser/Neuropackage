from unittest import TestCase
from tvb.ascii import py_format

class TestAsciiArt(TestCase):
    def test_py_format_contains_input_text(self):
        """ Test that py_format output contains the input string
        """
        self.assertIn(
            'test-string',
            py_format('test-string')
        )
