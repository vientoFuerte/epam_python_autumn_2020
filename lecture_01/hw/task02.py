"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from collections import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    i = None
    j = None
    for k in data:
        if i is None:
            i = k
        elif j is None:
            j = k
        else:
            i, j = j, i + j
            if k != j:
                return False
    return True




def test_check_fibonacci():
    assert check_fibonacci([0, 1, 1, 2, 3, 5, 8, 13]) is True

def test_check_fibonacci_fail():
    assert check_fibonacci([0, 1, 1, 2, 3, 5, 8, 133]) is False
