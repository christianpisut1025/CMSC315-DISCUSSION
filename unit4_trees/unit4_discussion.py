"""Unit 4 Discussion: Binary Search Trees."""


class Node:
    def __init__(self, value):
        # TODO (Student): Store the node's value and child references.
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # TODO (Student): Initialize an empty Binary Search Tree.
        self.root = None

    def insert(self, value):
        """TODO (Student): Insert a value using the recursive helper."""
        # Reassigning root handles an empty tree. Smaller values belong in the
        # left subtree, while larger values belong in the right subtree.
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """TODO (Student): Implement recursive BST insertion."""
        if node is None:
            return Node(value)

        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        # Duplicate employee IDs are ignored because each ID should be unique.
        return node

    def search(self, value):
        """TODO (Student): Return whether a value exists in the BST."""
        # Each comparison selects one subtree and eliminates the other. A
        # balanced BST therefore averages O(log n), versus O(n) linear search.
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """TODO (Student): Implement recursive BST search."""
        if node is None:
            return False
        if value == node.value:
            return True
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    def inorder(self):
        """TODO (Student): Return values from an in-order traversal."""
        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """TODO (Student): Implement left-node-right traversal."""
        if node is None:
            return

        # Left values are smaller and right values are larger, so visiting the
        # left subtree, node, and right subtree produces ascending output.
        self._inorder_recursive(node.left, values)
        values.append(node.value)
        self._inorder_recursive(node.right, values)


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # TODO (Student): BUILD A TREE
    print("\n=== EMPLOYEE ID TREE CONSTRUCTION ===")
    employee_tree = BST()
    employee_ids = [1050, 1025, 1075, 1010, 1035, 1060, 1090, 1005, 1020, 1040, 1080]
    for employee_id in employee_ids:
        employee_tree.insert(employee_id)
    print(f"Employee IDs inserted: {employee_ids}")
    print("The insertion order placed values on both sides of the root.")
    print("Each search comparison can discard the opposite subtree.")

    # TODO (Student): IN-ORDER TRAVERSAL
    print("\n=== IN-ORDER TRAVERSAL ===")
    ordered_ids = employee_tree.inorder()
    print(f"Employee IDs in ascending order: {ordered_ids}")
    print("Left-node-right traversal is sorted because left values are smaller and right values are larger.")

    # TODO (Student): SEARCH TESTS
    print("\n=== SEARCH TESTS ===")
    for employee_id in [1010, 1080, 999, 1100]:
        result = employee_tree.search(employee_id)
        status = "found" if result else "not found"
        print(f"Employee ID {employee_id}: {status}")
    print("Existing IDs return True; IDs absent from the tree return False.")

    # TODO (Student): EDGE CASES
    print("\n=== EDGE CASES ===")
    empty_tree = BST()
    print(f"Empty-tree traversal: {empty_tree.inorder()}")
    print(f"Search empty tree for 1050: {empty_tree.search(1050)}")

    before_duplicate = employee_tree.inorder()
    employee_tree.insert(1050)
    after_duplicate = employee_tree.inorder()
    print(f"Duplicate 1050 ignored: {before_duplicate == after_duplicate}")

    single_node_tree = BST()
    single_node_tree.insert(2000)
    print(f"Single-node traversal: {single_node_tree.inorder()}")
    print("Empty operations are safe, duplicates are ignored, and a one-node tree works normally.")


if __name__ == "__main__":
    main()
