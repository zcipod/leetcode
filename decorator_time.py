"""This is a decorator to show the time cost by the function"""

from functools import wraps
from time import time


def count_time(func):
    """print run time calculation"""
    @wraps(func)
    def count(*args, **kwargs):
        """record the time of both start and end,
        print the cost time after finishing the function"""
        time_start = time()
        res = func(*args, **kwargs)
        time_end = time()
        print("\nThe time cost is : {:.3f}ms".format((time_end - time_start) * 1000))
        return res
    return count
