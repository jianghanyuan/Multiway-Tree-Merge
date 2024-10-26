# Usage

## 1. Constructing a Tree

```bash

from tree_builder import build_tree

# Sample data
data = [
    [1, 10, 1, 2],  # Node 0: key=1, value=10, children indices=1 and 2
    [2, 20],        # Node 1: key=2, value=20, no children
    [3, 30]         # Node 2: key=3, value=30, no children
]

# Build the tree
root = build_tree(data)
```
## 2. Merging Trees

```bash

from tree_builder import build_tree
from tree_merger import merge_trees

# Left tree data
left_data = [
    [1, 10, 1],
    [2, 20]
]

# Right tree data
right_data = [
    [1, 15, 1],
    [3, 30]
]

# Build left and right trees
left_root = build_tree(left_data)
right_root = build_tree(right_data)

# Merge the trees
merged_root = merge_trees(left_root, right_root)
```
## 3. Pre-order Traversal

```bash

from traversal import preorder_traversal

# Perform pre-order traversal on the merged tree
result = preorder_traversal(merged_root)
print(result)  # Outputs: [1, 15, 2, 20, 3, 30]

```
## Merging Rules
1. **Same Root Key**: The trees can only be merged if their root nodes have the same key.
2. **Node Merging**:
   - Merged node's key is taken from the left tree.
   - Merged node's value is taken from the right tree.
3. **Children Merging**:
   - Recursively merge children if they exist in both trees.
   - Include children from either tree if they exist in only one.
   - Retain the order of children from the left tree and append any new children from the right tree.

