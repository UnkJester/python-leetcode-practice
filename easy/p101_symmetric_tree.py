from helpers.binary_tree import TreeNode, build_tree

def isSymmetric(root: TreeNode | None) -> bool:
    def isSymmetricSides(left, right) -> bool:
        return (left is None and right is None) or (
                    left.val == right.val and isSymmetricSides(left.left, right.right) and isSymmetricSides(left.right,
                                                                                                            right.left))

    return isSymmetricSides(root.left, root.right)


if __name__ == '__main__':
    assert isSymmetric(build_tree([1, 2, 2, 3, 4, 4, 3])), f'Was not symmetric'