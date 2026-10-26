from helpers.binary_tree import build_tree,TreeNode


def maxDepth_recursive(root: TreeNode | None) -> int:
    """
    Given the root of a binary tree, return its maximum depth.

    A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
    :param root: TreeNode - root node of the given tree
    :return: int, maximum depth of the tree
    """
    return 0 if not root else (1 + max(maxDepth_recursive(root.left), maxDepth_recursive(root.right)))

if __name__ == '__main__':
    assert maxDepth_recursive(build_tree([3, 9, 20, None, None, 15, 7])) == 3, f'result was {maxDepth_recursive(build_tree([3, 9, 20, None, None, 15, 7]))}'