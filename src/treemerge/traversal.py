def preorder_traversal(node):
    result = []
    def traverse(n):
        if n:
            result.append(n.key)
            result.append(n.value)
            for child in n.children:
                traverse(child)
    traverse(node)
    return result
