import unittest
import io
from mock import patch
import sys

sys.path.append('../src/skills')

import AVA_IO


class TestAVAIO(unittest.TestCase):
    def test_text_read(self):
        with patch('__builtin__.raw_input', return_value='Hello World') as text:
            io_obj = AVA_IO.TextIO()
            input = io_obj.read()
            self.assetEqual("Hello World", input)

    def test_text_write(self):
        io_obj = AVA_IO.TextIO()
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        io_obj.write('Hello World')
        sys.stdout = sys.__stdout__
        self.assetEqual('Hello World', capturedOutput.getvalue())
