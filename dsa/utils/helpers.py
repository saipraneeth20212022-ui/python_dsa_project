"""Utility helpers: timer decorator, complexity logger."""
import time
import functools


def timer(func):
    """Decorator to print execution time of a function."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = (time.perf_counter() - start) * 1000
        print(f"{func.__name__} took {elapsed:.3f} ms")
        return result
    return wrapper
