import unittest

from task import parse_line, InvalidArgumentError

io_positive = {"30": 30, "30s": 30, "s": 1, "60.5m": 3630, "30.5s": 30.5, "30.0": 30, "30.": 30, ".5m": 30, "30.s": 30}
io_negative_iae = ("10seconds", "", "1m30s", "1y", "", "-1")
io_negative_te = (1, ("30", ), print)
io_negative_ve = (".h", ".")


class TestTask1(unittest.TestCase):
    def test_positive(self):
        for i in io_positive.keys():
            with self.subTest(line=i):
                self.assertEqual(io_positive[i], parse_line(i))

    def test_got_exception_iae(self):
        for i in io_negative_iae:
            with self.subTest(i=i):
                self.assertRaises(InvalidArgumentError, parse_line, i)

    def test_got_exception_te(self):
        for i in io_negative_te:
            with self.subTest(i=i):
                self.assertRaises(TypeError, parse_line, i)

    def test_got_exception_ve(self):
        for i in io_negative_ve:
            with self.subTest(i=i):
                self.assertRaises(ValueError, parse_line, i)


if __name__ == "__main__":
    unittest.main()
