"""Compare bubble sort and merge sort using several datasets."""


def bubble_sort(lst):
    """TODO (Student): Sort a copy by comparing and swapping adjacent values."""
    result = lst.copy()  # Leave the caller's original list unchanged.
    # Nested passes give O(n²) comparisons in the average and worst cases.
    for end in range(len(result) - 1, 0, -1):
        swapped = False
        for index in range(end):
            if result[index] > result[index + 1]:
                result[index], result[index + 1] = result[index + 1], result[index]
                swapped = True
        if not swapped:  # An already ordered pass means the list is sorted.
            break
    return result


def merge_sort(lst):
    """TODO (Student): Recursively divide, sort, and merge a list."""
    if len(lst) <= 1:
        return lst.copy()  # Empty and single-item lists are already sorted.
    midpoint = len(lst) // 2
    left = merge_sort(lst[:midpoint])
    right = merge_sort(lst[midpoint:])
    return merge(left, right)


def merge(left, right):
    """TODO (Student): Combine two sorted halves into one sorted list."""
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        # Choosing the left item on a tie preserves the order of equal items.
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # One half may still contain items after the other is exhausted.
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def show_comparison(label, values):
    """Show and verify both algorithms against Python's expected ordering."""
    bubble_result = bubble_sort(values)
    merge_result = merge_sort(values)
    print(f"\n{label}: {values}")
    print(f"  Bubble Sort: {bubble_result}")
    print(f"  Merge Sort:  {merge_result}")
    print(f"  Same sorted result: {bubble_result == merge_result == sorted(values)}")
    assert bubble_result == merge_result == sorted(values)


def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")

    # TODO (Student): DATASET #1
    # Price scenario: sort seven product prices using both algorithms.
    print("\n=== DATASET #1: PRODUCT PRICES ===")
    show_comparison("Prices", [42, 19, 88, 7, 31, 56, 12])

    # TODO (Student): DATASET #2
    # Streaming scenario: popularity scores differ from the first dataset.
    print("\n=== DATASET #2: STREAMING POPULARITY SCORES ===")
    show_comparison("Scores", [96, 25, 71, 43, 82, 14, 65, 38])

    # TODO (Student): EDGE CASES
    print("\n=== EDGE CASE TESTS ===")
    for label, values, explanation in [
        ("Empty list", [], "Both return an empty list without an error."),
        ("Already sorted", [1, 2, 3, 4], "Bubble Sort stops after a pass with no swaps."),
        ("Reverse sorted", [4, 3, 2, 1], "Both restore ascending order."),
        ("Duplicates", [3, 1, 3, 2, 1], "Both retain every repeated value."),
        ("Single item", [9], "Neither needs to rearrange one value."),
    ]:
        show_comparison(label, values)
        print(f"  Interpretation: {explanation}")


if __name__ == "__main__":
    main()
