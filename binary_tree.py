class TreeNode:
    def __init__(self, key) -> None:
        self.key, self.left, self.right = key, None, None
        
    def height(self):
        if self is None:
            return 0
        return 1 + max(TreeNode.height(self.left), TreeNode.height(self.right))

    def size(self):
        if self is None:
            return 0
        return 1 + TreeNode.size(self.left) + TreeNode.size(self.right)

    def traverse_in_order(self):
        if self is None:
            return []
        return TreeNode.traverse_in_order(self.left) + [self.key] + TreeNode.traverse_in_order(self.right)

    def traverse_pre_order(self):
        if self is None:
            return []
        return [self.key] + TreeNode.traverse_pre_order(self.left) + TreeNode.traverse_pre_order(self.right)

    def traverse_post_order(self):
        if self is None:
            return []
        return TreeNode.traverse_post_order(self.right) + TreeNode.traverse_post_order(self.left) + [self.key]

    def display_keys(self, space="\t", level=0):
        # If node is empty
        if self is None:
            print(space*level + "ø")
            return
        
        # If the node is a leaf
        if self.left is None and self.right is None:
            print(space*level + str(self.key))
            return

        # If the node has children
        TreeNode.display_keys(self.right, space, level+1)
        print(space*level + str(self.key))
        TreeNode.display_keys(self.left, space, level+1)

    def to_turple(self):
        if self is None:
            return None
        if self.left is None and self.right is None:
            return self.key
        return TreeNode.to_turple(self.left), self.key, TreeNode.to_turple(self.right)

    def __str__(self) -> str:
        return f"BinaryTree <{self.to_turple()}>"

    def __repr__(self) -> str:
        return f"BinaryTree <{self.to_turple()}>"

    @staticmethod
    def parse_turple(data):
        if data is None:
            node = None
        if isinstance(data, tuple) and len(data) == 3:
            node = TreeNode(data[1])
            node.left = TreeNode.parse_turple(data[0])
            node.right = TreeNode.parse_turple(data[2])
        else:
            node = TreeNode(data)
        return node




tree_turple = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))
tree = TreeNode.parse_turple(tree_turple)
print(tree)
tree.display_keys("    ")
height = tree.height()
size = tree.size()
traverse_in_order = tree.traverse_in_order()
traverse_pre_order = tree.traverse_pre_order()
traverse_post_order = tree.traverse_post_order()

print(f"height: {height}")
print(f"size: {size}")
print(f"traverse_in_order: {traverse_in_order}")
print(f"traverse_pre_order: {traverse_pre_order}")
print(f"traverse_post_order: {traverse_post_order}")