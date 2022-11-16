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

def tree_to_turple(node):
    if isinstance(node, TreeNode):
        turple = tree_to_turple((node.left.key, node.key, node.right.key))
    elif node is None:
        turple = None
    else:
        turple = node
    print(turple)

def display_keys(node, space="\t", level=0):

    # If node is empty
    if node is None:
        print(space*level + "ø")
        return
    
    # If the node is a leaf
    if node.left is None and node.right is None:
        print(space*level + str(node.key))
        return

    # If the node has children
    display_keys(node.right, space, level+1)
    print(space*level + str(node.key))
    display_keys(node.left, space, level+1)

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

display_keys(tree2, "    ")
traverse_in_order = traverse_in_order(tree2)
traverse_pre_order = traverse_pre_order(tree2)
traverse_post_order = traverse_post_order(tree2)

print(f"traverse_in_order: {traverse_in_order}")
print(f"traverse_pre_order: {traverse_pre_order}")
print(f"traverse_post_order: {traverse_post_order}")