import timeit
from CountSorter import CountSorter
from collections import Counter

import random
from time import time
import string

def gen_rand_string(n)->str:
    return ''.join(random.choice(string.ascii_letters) for i in range(n))


def test_counter(get_n_most_frequent,num_items=10000,item_length=2):
    """Stupid test function"""
    start = time()
    c = Counter()
    for i in range(num_items):
        c.update([gen_rand_string(item_length)])
        c.most_common(get_n_most_frequent)
    #print(c.most_common(5))
    print(f"Counter, {num_items}, {item_length}, {get_n_most_frequent}, {time() - start}")

def test_count_sorter(get_n_most_frequent,num_items=10000,item_length=2):
    """Stupid test function"""
    start = time()
    c = CountSorter()
    for i in range(num_items):
        c.add_occurrence(gen_rand_string(item_length))
        c.get_most_frequent(get_n_most_frequent)
    #print(c.get_most_frequent(5))
    print(f"CountSorter, {num_items}, {item_length}, {get_n_most_frequent}, {time() - start}")

if __name__ == '__main__':
    item_length = 2
    num_items = 10000
    print("method, num_items, get_n_most_frequent, time")
    for get_n_most_frequent in [int(num_items/(10**i)) for i in range(5)]:
        test_counter(get_n_most_frequent,num_items=num_items,item_length=item_length)
        test_count_sorter(get_n_most_frequent,num_items=num_items,item_length=item_length)
    test_counter(get_n_most_frequent=1, num_items=num_items*10, item_length=item_length)
    test_count_sorter(get_n_most_frequent=1, num_items=num_items*10, item_length=item_length)
