# CountSorter
This is a class that can efficiently count items while sorting the items by their count. It uses a doubly linked list (a slightly modified version of the one I grabbed from https://favtutor.com/blogs/doubly-linked-list-python )

The runtime of the 2 public methods of the CountSorter class are as follows:

* def add_occurrence(self, item):   
  * """  
  Adds an occurrence of an item.  
  Runtime: O(1)  
  """
* def get_most_frequent(self, num_items:int) -> OrderedDict[Any,int]:  
  * """  
  Get the most frequent `num_items` items along with their counts in sorted order (largest to smallest)
  Example Result: [("c", 6), ("b",5) , ("a", 5)]
  Runtime: O(num_items)  
  """

## Benchmark
I compared this solution with collections.Counter, and this solution is much faster assuming num_items in get_most_frequent method < total number of items 
Benchmark results, calling the get_most_frequent after each item is added:
```
Count for: get_n_most_frequent: 10000 time: 2.6435976028442383
CountSorter for: get_n_most_frequent: 10000 time: 4.7814624309539795
Count for: get_n_most_frequent: 1000 time: 7.344721555709839
CountSorter for: get_n_most_frequent: 1000 time: 2.20153546333313
Count for: get_n_most_frequent: 100 time: 2.6238646507263184
CountSorter for: get_n_most_frequent: 100 time: 0.24534344673156738
Count for: get_n_most_frequent: 10 time: 1.7718539237976074
CountSorter for: get_n_most_frequent: 10 time: 0.05838155746459961
```
See benchmark.py for more details