import timeit
from CountSorter import CountSorter
from collections import Counter

import random
from time import time
import string

KEY_LENGTH = 3
NUM_KEYS = 1000
def gen_rand_string(n)->str:
    return ''.join(random.choice(string.ascii_letters) for i in range(n))

def test_counter():
    """Stupid test function"""
    start = time()
    c = Counter()
    for i in range(NUM_KEYS):
        c.update([gen_rand_string(KEY_LENGTH)])
        c.most_common(NUM_KEYS)
    print(f"Counter time: {time()-start}")

def test_count_sorter():
    """Stupid test function"""
    start = time()
    c = CountSorter()
    for i in range(NUM_KEYS):
        c.add_occurrence(gen_rand_string(KEY_LENGTH))
        c.get_most_frequent(NUM_KEYS)
    print(f"CountSorter time: {time() - start}")

if __name__ == '__main__':
    test_counter()
    test_count_sorter()
