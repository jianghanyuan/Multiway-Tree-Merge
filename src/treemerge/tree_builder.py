from node import Node

def build_tree(data):
    nodes = []
    for entry in data:
        key = entry[0]
        value = entry[1]
        node = Node(key, value)
        nodes.append(node)

    all_indices = set(range(len(data)))
    child_indices = set()
    for idx, entry in enumerate(data):
        children_indices = entry[2:]
        for child_idx in children_indices:
            nodes[idx].add_child(nodes[child_idx])
            child_indices.add(child_idx)

    root_indices = all_indices - child_indices
    if not root_indices:
        return None  # No root found
    root_idx = root_indices.pop()
    return nodes[root_idx]
