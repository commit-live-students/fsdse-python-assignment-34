from unittest import TestCase


class TestSort_list_last(TestCase):
    def test_sort_list_last(self):
        from build import solution

        self.assertEqual(solution([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]), [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)])
