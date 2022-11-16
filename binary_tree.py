class TreeNode:
    def __init__(self, key) -> None:
        self.key = key
        self.left = None
        self.right = None

tree_turple = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))

def parse_turple(data):
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parse_turple(data[0])
        node.right = parse_turple(data[2])
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node

tree2 = parse_turple(tree_turple)

# print(tree2.key)
# print(tree2.left.key, tree2.right.key)
# print(tree2.left.left.key, tree2.left.right, tree2.right.left.key, tree2.right.right.key)
# print(tree2.right.left.left, tree2.right.left.right.key, tree2.right.right.left.key, tree2.right.right.right.key)

def tree_to_turple(node):
    if isinstance(node, TreeNode):
        turple = tree_to_turple((node.left.key, node.key, node.right.key))
    elif node is None:
        turple = None
    else:
        turple = node
    print(turple)

def traverse_in_order(node):
    if node is None:
        return []
    return traverse_in_order(node.left) + [node.key] + traverse_in_order(node.right)

def traverse_pre_order(node):
    if node is None:
        return []
    return [node.key] + traverse_pre_order(node.left) + traverse_pre_order(node.right)

def traverse_post_order(node):
    if node is None:
        return []
    return traverse_post_order(node.right) + traverse_post_order(node.left) + [node.key]

traverse_in_order = traverse_in_order(tree2)
traverse_pre_order = traverse_pre_order(tree2)
traverse_post_order = traverse_post_order(tree2)

print(f"traverse_in_order: {traverse_in_order}")
print(f"traverse_pre_order: {traverse_pre_order}")
print(f"traverse_post_order: {traverse_post_order}")