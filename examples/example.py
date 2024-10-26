from tree_builder import build_tree
from tree_merger import merge_trees
from traversal import preorder_traversal

# Left tree data
left_data = [
    [1, 10, 1, 2],
    [2, 20],
    [3, 30]
]

# Right tree data
right_data = [
    [1, 15, 1, 3],
    [2, 25],
    [4, 40]
]

# Build left and right trees
left_root = build_tree(left_data)
right_root = build_tree(right_data)

# Merge the trees
merged_root = merge_trees(left_root, right_root)

# Perform pre-order traversal
result = preorder_traversal(merged_root)
print(result)  # Outputs: [1, 15, 2, 25, 3, 30, 4, 40]
