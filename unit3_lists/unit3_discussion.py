"""Unit 3 Discussion: List Operations (Insert, Delete, and Search)."""


def insert_at(lst, index, value):
    """Insert value at index when the index is valid and return success."""
    # A valid insertion index ranges from 0 through len(lst).
    if index < 0 or index > len(lst):
        return False

    # Elements at and after index shift right. Beginning or middle insertion
    # is O(n), while insertion at the end is typically O(1) amortized.
    lst.insert(index, value)
    return True


def delete_at(lst, index):
    """Remove and return the item at index, or return None if invalid."""
    # Validation prevents IndexError and safely handles empty lists.
    if index < 0 or index >= len(lst):
        return None

    # Later elements shift left, making most indexed deletions O(n).
    return lst.pop(index)


def search_value(lst, value):
    """Return the index of value, or -1 when value is not present."""
    # This is linear search because items are checked sequentially. Its
    # worst-case running time is O(n).
    for index, item in enumerate(lst):
        if item == value:
            return index

    return -1


def main():
    """Demonstrate list operations and clearly explain each result."""
    print("=== UNIT 3: LIST OPERATIONS ===")
    playlist = ["Blinding Lights", "Levitating", "As It Was"]

    print("\n=== INSERTION TESTS ===")
    print(f"Original playlist: {playlist}")

    # Test insertion at the beginning, middle, and end.
    insert_at(playlist, 0, "Lose Yourself")
    print(f"After beginning insertion: {playlist}")

    middle_index = len(playlist) // 2
    insert_at(playlist, middle_index, "Viva La Vida")
    print(f"After middle insertion:    {playlist}")

    insert_at(playlist, len(playlist), "Bad Habits")
    print(f"After end insertion:       {playlist}")

    print("\n=== DELETION TESTS ===")

    # Test deletion at the beginning, middle, and end.
    removed = delete_at(playlist, 0)
    print(f"Removed from beginning: {removed}")
    print(f"Playlist now: {playlist}")

    middle_index = len(playlist) // 2
    removed = delete_at(playlist, middle_index)
    print(f"Removed from middle:    {removed}")
    print(f"Playlist now: {playlist}")

    removed = delete_at(playlist, len(playlist) - 1)
    print(f"Removed from end:       {removed}")
    print(f"Playlist now: {playlist}")

    print("\n=== SEARCH TESTS ===")

    # Search for one existing value and one missing value.
    target = "Viva La Vida"
    result = search_value(playlist, target)
    print(f"Search for '{target}': index {result}")

    target = "Bohemian Rhapsody"
    result = search_value(playlist, target)
    print(f"Search for '{target}': index {result} (not found)")

    print("\n=== EDGE CASES ===")

    # An invalid deletion returns None rather than raising an exception.
    invalid_result = delete_at(playlist, 99)
    print(f"Delete using invalid index 99: {invalid_result}")

    # Demonstrate safe deletion and valid insertion with an empty list.
    empty_playlist = []
    empty_delete_result = delete_at(empty_playlist, 0)
    print(f"Delete from an empty list: {empty_delete_result}")

    empty_insert_result = insert_at(empty_playlist, 0, "First Song")
    print(
        "Insert into an empty list: "
        f"success={empty_insert_result}, list={empty_playlist}"
    )

    # An invalid insertion returns False and leaves the list unchanged.
    invalid_insert_result = insert_at(empty_playlist, 5, "Invalid Song")
    print(
        "Insert using invalid index 5: "
        f"success={invalid_insert_result}, list={empty_playlist}"
    )


if __name__ == "__main__":
    main()
