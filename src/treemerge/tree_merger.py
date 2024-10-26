from node import Node

def merge_trees(node_left, node_right):
    if not node_left and not node_right:
        return None
    if not node_left:
        return node_right
    if not node_right:
        return node_left
    if node_left.key != node_right.key:
        return None  # Roots have different keys

    # Create merged node
    merged_node = Node(node_left.key, node_right.value)

    # Build dictionaries for quick access
    left_children = {child.key: child for child in node_left.children}
    right_children = {child.key: child for child in node_right.children}

    merged_children = []

    # Merge children present in both trees
    for key, left_child in left_children.items():
        if key in right_children:
            merged_child = merge_trees(left_child, right_children[key])
            merged_children.append(merged_child)
            del right_children[key]
        else:
            merged_children.append(left_child)

    # Append children only in right tree
    merged_children.extend(right_children.values())

    merged_node.children = merged_children
    return merged_node
