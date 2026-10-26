# Definition for a binary tree node.
from collections import deque
from typing import Optional
from helpers.binary_tree import TreeNode,build_tree

class Solution:
    def inorderTraversalRecursive(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []
        left = self.inorderTraversalRecursive(root.left) if root.left else []
        right = self.inorderTraversalRecursive(root.right) if root.right else []
        return left + [root.val] + right


    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []
        breadcrumbs : list = []
        result = []
        curr_ptr = root
        while True:
            if breadcrumbs:
                if breadcrumbs[-1] == curr_ptr.left:
                    curr_ptr.left = None
                    breadcrumbs.pop()
                    result.append(curr_ptr.val)
                    if curr_ptr.right:
                        curr_ptr = curr_ptr.right # No need to store breadcrumb, assume it is there
                    else:
                        if len(breadcrumbs) >= 2:
                            curr_ptr = breadcrumbs[-2]
                        else:
                            return result
                    continue
                elif breadcrumbs[-1] == curr_ptr.right:
                    curr_ptr.right = None
                    breadcrumbs.pop()
                    if len(breadcrumbs) >= 2:
                        curr_ptr = breadcrumbs[-2]
                    else:
                        return result
                    continue

            if curr_ptr.left:
                breadcrumbs.append(curr_ptr)
                curr_ptr = curr_ptr.left
            elif curr_ptr.right:
                result.append(curr_ptr.val)
                breadcrumbs.append(curr_ptr)
                curr_ptr = curr_ptr.right
            else:
                if not breadcrumbs:
                    # Case: Tree has only one node
                    return [curr_ptr.val]
                else:
                    result.append(curr_ptr.val)
                    breadcrumbs.append(curr_ptr)
                    curr_ptr = breadcrumbs[-2]


if __name__ == '__main__':
    result = Solution().inorderTraversal(build_tree([1,2,3,4,5,None,8,None,None,6,7,9]))
    result2 = Solution().inorderTraversalRecursive(build_tree([1,2,3,4,5,None,8,None,None,6,7,9]))
    # result = Solution().inorderTraversal(build_tree([1,None,2,3]))
    # result2 = Solution().inorderTraversalRecursive(build_tree([1,None,2,3]))
    assert result == result2, f'iterative={result} recursive={result2}'
    print(result)
    print(result2)