def tree_by_levels(node):
    if node is None:
        return []
    result = []
    q = [node]
    while q:
        nod = q.pop(0)
        result.append(nod.value)
        if nod.left:
            q.append(nod.left)
        if nod.right:
            q.append(nod.right)
    return result
