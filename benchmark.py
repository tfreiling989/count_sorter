import timeit
from CountSorter import CountSorter
from collections import Counter

import random
from time import time
import string

KEY_LENGTH = 2
NUM_KEYS = 10000
def gen_rand_string(n)->str:
    return ''.join(random.choice(string.ascii_letters) for i in range(n))

def test_counter(get_n_most_frequent):
    """Stupid test function"""
    start = time()
    c = Counter()
    for i in range(NUM_KEYS):
        c.update([gen_rand_string(KEY_LENGTH)])
        c.most_common(get_n_most_frequent)
    #print(c.most_common(5))
    print(f"Count for: get_n_most_frequent: {get_n_most_frequent} time: {time() - start}")

def test_count_sorter(get_n_most_frequent):
    """Stupid test function"""
    start = time()
    c = CountSorter()
    for i in range(NUM_KEYS):
        c.add_occurrence(gen_rand_string(KEY_LENGTH))
        c.get_most_frequent(get_n_most_frequent)
    #print(c.get_most_frequent(5))
    print(f"CountSorter for: get_n_most_frequent: {get_n_most_frequent} time: {time() - start}")

if __name__ == '__main__':
    n = NUM_KEYS
    test_counter(n)
    test_count_sorter(n)
    n = int(NUM_KEYS / 10)
    test_counter(n)
    test_count_sorter(n)
    n = int(NUM_KEYS / 100)
    test_counter(n)
    test_count_sorter(n)
    n = int(NUM_KEYS / 1000)
    test_counter(n)
    test_count_sorter(n)
