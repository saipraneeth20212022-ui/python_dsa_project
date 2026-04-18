"""
Benchmark sorting algorithms across different input sizes.
Generates a comparison plot: benchmarks/sort_comparison.png
"""
import time
import random
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from dsa.algorithms.sorting import merge_sort, quick_sort, heap_sort

SIZES = [100, 500, 1000, 3000, 5000, 10000]
RUNS = 3


def benchmark(func, arr):
    times = []
    for _ in range(RUNS):
        data = arr[:]
        start = time.perf_counter()
        func(data)
        times.append(time.perf_counter() - start)
    return min(times)


def run_benchmarks():
    results = {name: [] for name in ("merge_sort", "quick_sort", "heap_sort", "python_sort")}

    print(f"\n{'Size':>8} | {'Merge (ms)':>11} | {'Quick (ms)':>11} | {'Heap (ms)':>10} | {'Python (ms)':>12}")
    print("-" * 65)

    for size in SIZES:
        arr = [random.randint(0, 100_000) for _ in range(size)]
        r = {
            "merge_sort":   benchmark(merge_sort, arr) * 1000,
            "quick_sort":   benchmark(quick_sort, arr) * 1000,
            "heap_sort":    benchmark(heap_sort, arr) * 1000,
            "python_sort":  benchmark(sorted, arr) * 1000,
        }
        for k, v in r.items():
            results[k].append(v)
        print(f"{size:>8} | {r['merge_sort']:>11.2f} | {r['quick_sort']:>11.2f} | {r['heap_sort']:>10.2f} | {r['python_sort']:>12.2f}")

    try:
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(figsize=(10, 6))
        colors = {"merge_sort": "#2563eb", "quick_sort": "#16a34a", "heap_sort": "#dc2626", "python_sort": "#7c3aed"}
        for name, times in results.items():
            ax.plot(SIZES, times, marker="o", label=name, color=colors[name])
        ax.set_xlabel("Input size (n)")
        ax.set_ylabel("Time (ms)")
        ax.set_title("Sorting Algorithm Benchmark")
        ax.legend()
        ax.grid(True, alpha=0.3)
        output_path = os.path.join(os.path.dirname(__file__), "sort_comparison.png")
        plt.savefig(output_path, dpi=150, bbox_inches="tight")
        print(f"\nPlot saved to {output_path}")
    except ImportError:
        print("\nInstall matplotlib to generate plots: pip install matplotlib")

    return results


if __name__ == "__main__":
    run_benchmarks()
