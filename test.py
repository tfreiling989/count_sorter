from unittest import TestCase
from CountSorter import CountSorter

class TestCountSorter(TestCase):

    def _assert_most_frequent(self,count_sorter,num,expected):
        res = count_sorter.get_most_frequent(num)
        print(res)
        self.assertEqual(expected,[(k,v) for k,v in res.items()])

    def test_various_cases(self):
        count_sorter = CountSorter()
        count_sorter.add_occurrence("a")
        self._assert_most_frequent(count_sorter,1,[("a",1)])
        count_sorter.add_occurrence("b")
        self._assert_most_frequent(count_sorter,1, [("a", 1)])
        self._assert_most_frequent(count_sorter,2, [("a",1),("b", 1)])
        count_sorter.add_occurrence("c")
        self._assert_most_frequent(count_sorter,2, [("a", 1), ("b", 1)])
        count_sorter.add_occurrence("c")
        self._assert_most_frequent(count_sorter,2, [("c", 2), ("a", 1)])
        count_sorter.add_occurrence("b")
        self._assert_most_frequent(count_sorter,2, [("c", 2), ("b", 2)])
        count_sorter.add_occurrence("c")
        self._assert_most_frequent(count_sorter, 2, [("c", 3), ("b", 2)])
        self._assert_most_frequent(count_sorter, 3, [("c", 3), ("b", 2),("a", 1)])
        count_sorter.add_occurrence("d")
        self._assert_most_frequent(count_sorter, 3, [("c", 3), ("b", 2), ("a", 1)])
        count_sorter.add_occurrence("d")
        self._assert_most_frequent(count_sorter, 3, [("c", 3), ("b", 2), ("d", 2)])
        count_sorter.add_occurrence("d")
        self._assert_most_frequent(count_sorter, 3, [("c", 3), ("d", 3),("b", 2)])
        count_sorter.add_occurrence("d")
        self._assert_most_frequent(count_sorter, 3, [("d", 4),("c", 3), ("b", 2)])
        self._assert_most_frequent(count_sorter, 100, [("d", 4), ("c", 3), ("b", 2),("a",1)])



if __name__ == '__main__':
    main()