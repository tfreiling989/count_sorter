# CountSorter
This is a class that can efficiently count items while sorting the items by their count. It uses a doubly linked list (a slightly modified version of the one I grabbed from https://favtutor.com/blogs/doubly-linked-list-python )

The runtime of the 2 public methods of the CountSorter class are as follows:

* def add_occurrence(self, item):
  * O(1)
* def get_most_frequent(self, num_items:int) -> OrderedDict[Any,int]:
  * O(num_items)
