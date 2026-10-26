# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(values: list[Optional[int]]) -> Optional[TreeNode]:
    """Build a binary tree from a LeetCode-style level-order list (None = missing node)."""
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        # Left child
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        # Right child
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root

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
            # if dead node, back up or exit
            # if not curr_ptr:
            #     if not breadcrumbs:
            #         return result
            #     else:
            #         curr_ptr = breadcrumbs.pop()
            # else:
            #     # If the previous node is the last child, bounce up
            #     if breadcrumbs:
            #         if breadcrumbs[-1] == curr_ptr.left:
            #             breadcrumbs.pop()
            #             curr_ptr.left = None
            #             continue
            #         elif breadcrumbs[-1] == curr_ptr.right
            #     if curr_ptr.left:
            #         # If left, add breadcrumb and traverse left
            #         breadcrumbs.append(curr_ptr)
            #         curr_ptr = curr_ptr.left
            #     else:
            #         # Else, add val and attempt traverse right
            #         result.append(curr_ptr.val)
            #         if curr_ptr.right:
            #             breadcrumbs.append(curr_ptr)
            #             curr_ptr = curr_ptr.right
            #         else:
            #             # No right or left, time to leave node
            #             temp_ptr = curr_ptr
            #             curr_ptr = breadcrumbs.pop()
            #             # add ptr to curr_node to prevent inf loop
            #             breadcrumbs.append(temp_ptr)


if __name__ == '__main__':
    result = Solution().inorderTraversal(build_tree([1,2,3,4,5,None,8,None,None,6,7,9]))
    result2 = Solution().inorderTraversalRecursive(build_tree([1,2,3,4,5,None,8,None,None,6,7,9]))
    # result = Solution().inorderTraversal(build_tree([1,None,2,3]))
    # result2 = Solution().inorderTraversalRecursive(build_tree([1,None,2,3]))
    assert result == result2, f'iterative={result} recursive={result2}'
    print(result)
    print(result2)