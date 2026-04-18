"""Benchmark binary search variants."""
import time, random, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from dsa.algorithms.searching import binary_search

SIZES = [10_000, 100_000, 500_000, 1_000_000]

print(f"\n{'Size':>10} | {'Binary (µs)':>12} | {'Linear (µs)':>12}")
print("-" * 42)
for size in SIZES:
    arr = list(range(size))
    target = random.randint(0, size - 1)

    t0 = time.perf_counter()
    for _ in range(1000): binary_search(arr, target)
    bs_time = (time.perf_counter() - t0) / 1000 * 1_000_000

    t0 = time.perf_counter()
    for _ in range(1000): arr.index(target) if target in arr else -1
    lin_time = (time.perf_counter() - t0) / 1000 * 1_000_000

    print(f"{size:>10} | {bs_time:>12.2f} | {lin_time:>12.2f}")
