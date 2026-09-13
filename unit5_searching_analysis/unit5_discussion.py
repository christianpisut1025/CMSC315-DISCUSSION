"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

This program implements linear and binary search, compares them on small and
large sorted datasets, and demonstrates several edge cases.
"""

from time import perf_counter


def linear_search(lst, target):
    """Return the target index, or -1 when the target is not present."""
    # Linear search checks values sequentially. In the worst case, it checks
    # all n elements, so its time complexity is O(n).
    for index, value in enumerate(lst):
        if value == target:
            return index
    return -1


def binary_search(lst, target):
    """Return the target index in a sorted list, or -1 if it is absent."""
    low = 0
    high = len(lst) - 1

    while low <= high:
        middle = low + (high - low) // 2

        if lst[middle] == target:
            return middle
        if lst[middle] < target:
            # Everything through middle is too small, so that half is removed.
            low = middle + 1
        else:
            # Everything from middle onward is too large, removing that half.
            high = middle - 1

    return -1


def timed_search(search_function, dataset, target):
    """Run one search and return its result and elapsed time in milliseconds."""
    start = perf_counter()
    result = search_function(dataset, target)
    elapsed_ms = (perf_counter() - start) * 1_000
    return result, elapsed_ms


def display_result(label, target, result):
    """Print a search result in an explanatory format."""
    if result == -1:
        print(f"{label}: {target} was not found; the method returned -1.")
    else:
        print(f"{label}: {target} was found at index {result}.")


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # TODO (Student): SMALL DATASET - completed
    print("\n=== SMALL DATASET TEST ===")
    small_data = [5, 12, 18, 27, 31, 44, 58, 63, 79, 92]
    print(f"Sorted dataset: {small_data}")

    for target in (44, 50):
        print(f"\nSearching for {target}:")
        display_result("Linear search", target, linear_search(small_data, target))
        display_result("Binary search", target, binary_search(small_data, target))

    # TODO (Student): LARGE DATASET - completed
    print("\n=== LARGE DATASET TEST ===")
    large_data = list(range(1_000_000))
    large_target = 999_999
    linear_result, linear_ms = timed_search(linear_search, large_data, large_target)
    binary_result, binary_ms = timed_search(binary_search, large_data, large_target)

    print(f"Dataset size: {len(large_data):,} sorted integers")
    print(f"Target: {large_target:,} (last position, a worst case for linear search)")
    print(f"Linear search: index {linear_result:,}, elapsed time {linear_ms:.4f} ms")
    print(f"Binary search: index {binary_result:,}, elapsed time {binary_ms:.4f} ms")
    print(
        "Interpretation: Linear search may inspect all 1,000,000 values, while "
        "binary search repeatedly halves the search space and needs only about "
        "20 comparisons. Exact timing varies by computer, but the growth-rate "
        "difference becomes clear on the large dataset."
    )

    # TODO (Student): EDGE CASES - completed
    print("\n=== EDGE CASE TESTS ===")
    edge_cases = [
        ("empty list", [], 10),
        ("single element present", [10], 10),
        ("single element missing", [10], 7),
        ("first position", [2, 4, 6, 8], 2),
        ("last position", [2, 4, 6, 8], 8),
    ]

    for description, dataset, target in edge_cases:
        linear_result = linear_search(dataset, target)
        binary_result = binary_search(dataset, target)
        print(
            f"{description.title()}: data={dataset}, target={target} -> "
            f"linear={linear_result}, binary={binary_result}"
        )

    print(
        "Edge-case interpretation: Both methods return -1 safely for empty or "
        "missing input and return valid boundary indexes for first, last, and "
        "single-element matches. Binary search assumes every tested list is sorted."
    )


if __name__ == "__main__":
    main()
