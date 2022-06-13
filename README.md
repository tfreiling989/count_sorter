# CountSorter
This is a class that can efficiently count items while sorting the items by their count.

The runtime of the 2 public methods of the CountSorter class are as follows:

* def add_occurrence(self, item):
  * O(1)
* def get_most_frequent(self, num_items:int) -> OrderedDict[Any,int]:
  * O(num_items)