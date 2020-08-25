"""Ideas for more tests:
* Try already opened files
* Try files with no read permissions
* Try non-existing files
"""

import io
import sys
import unittest

from task import open_files

i_files = (
          ("file1.txt", "file2.txt", "file3.txt"),
          ("file4.txt", )
          )
o_files = (
          "task2_test_output_file1_file2_file3.txt",
          "task2_test_output_file4.txt"
          )
iterations = (5, 1)


class TestTask2(unittest.TestCase):
    def test_positive(self):
        for i, o, n in zip(i_files, o_files, iterations):
            with self.subTest(i=i, o=o, n=n):
                captured_out = io.StringIO()
                sys.stdout = captured_out
                of = open_files(i)
                for _ in range(n):
                    next(of)
                sys.stdout = sys.__stdout__
                with open(o) as f:
                    self.assertEqual(captured_out.getvalue().strip("\n"), f.read().strip("\n"))
    
    def test_almost_ethernal(self):
        iteration_count = 10000
        
        i = i_files[0]
        prev_out = io.StringIO().getvalue()
        captured_out = io.StringIO()
        sys.stdout = captured_out
        of = open_files(i)
        for _ in range(iteration_count):
            next(of)
            self.assertGreater(len(captured_out.getvalue()), len(prev_out))
            prev_out = captured_out.getvalue()

if __name__ == "__main__":
    unittest.main()
