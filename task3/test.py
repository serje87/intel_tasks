"""Ideas for more tests:
* Try following inputs:
** String
** Dict
** Set
* Negative cases:
** Pass something not iterable
"""

import unittest

from task import merge

iterables = (
            ((1, 5, 9), [2, 5], (x for x in (1, 6, 10, 11))),
            ((1, 5, 9), (2, 5), (1, 6, 10, 11)),
            ([1, 5, 9], [2, 5], [1, 6, 10, 11]),
            ((x for x in (1, 5, 9)), (x for x in (2, 5)), (x for x in (1, 6, 10, 11))),
            )
expecteds = (
            (1, 1, 2, 5, 5, 6, 9, 10, 11),
            (1, 1, 2, 5, 5, 6, 9, 10, 11),
            (1, 1, 2, 5, 5, 6, 9, 10, 11),
            (1, 1, 2, 5, 5, 6, 9, 10, 11),
            )


class TestTask3(unittest.TestCase):
    def test_positive(self):
        for i, e in zip(iterables, expecteds):
            with self.subTest(i=i, e=e):
                act_res = tuple(x for x in merge(*i))
                self.assertEqual(e, act_res)
            

if __name__ == "__main__":
    unittest.main()
