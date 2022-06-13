# CountSorter
This is a class that can efficiently count items while sorting the items by their count. It uses a doubly linked list (a slightly modified version of the one I grabbed from https://favtutor.com/blogs/doubly-linked-list-python )

## Method Signatures and Runtimes
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

## How It Works - Theory
* It uses a doubly linked list where each node in the list has a count and the set of items with that count.
* There is also a hashmap that for each item, a pointer to its current node is stored. This allows O(1) lookups.
* When add_occurence is called for an item, it moves the item to the next node with the current count + 1. If that node doesn't exist, it will create it. This is also constant time O(1)
* When calling get_most_frequent, it simply can collect the n items that are at the end of the list. This is O(n) where n is the number of items requested.
* Theoretically, in a big O time complexity sense, this is the fastest possible solution.

## Example Usage:
```
c = CountSorter()
c.add_occurrence("a")
c.add_occurrence("a")
c.add_occurrence("a")
c.add_occurrence("b")
c.add_occurrence("c")
c.add_occurrence("b")
print(c.get_most_frequent(2).items())
```
Would be expected to print: [("a",3),("b",2)]

## Benchmark
I compared this solution with collections.Counter, and this solution is much faster assuming num_items in get_most_frequent method < total number of items 
Benchmark results, calling the get_most_frequent after each item is added:
```
method, num_items, get_n_most_frequent, time
Counter, 10000, 2, 10000, 2.556185007095337
CountSorter, 10000, 2, 10000, 4.463066577911377
Counter, 10000, 2, 1000, 6.818758010864258
CountSorter, 10000, 2, 1000, 2.0864181518554688
Counter, 10000, 2, 100, 2.4893338680267334
CountSorter, 10000, 2, 100, 0.2403562068939209
Counter, 10000, 2, 10, 1.6655514240264893
CountSorter, 10000, 2, 10, 0.05485248565673828
Counter, 10000, 2, 1, 1.0242605209350586
CountSorter, 10000, 2, 1, 0.039891719818115234
Counter, 100000, 2, 1, 13.034128665924072
CountSorter, 100000, 2, 1, 0.7719311714172363
```
Keeping in mind that there are definitely optimizations that this python solution could utilize.
See benchmark.py for more details