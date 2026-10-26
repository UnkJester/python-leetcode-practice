from p94_binary_tree_inorder_traversal import build_tree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        return p is None and q is None or (
                p is not None and q is not None
                and p.val == q.val
                and self.isSameTree(p.left, q.left)
                and self.isSameTree(p.right, q.right))


if __name__ == '__main__':
    tree1 = build_tree([1,2,3])
    tree2 = build_tree([1,2,3])
    tree3 = build_tree([1,2,4])
    assert Solution().isSameTree(tree1, tree2)
    assert not Solution().isSameTree(tree1, tree3)