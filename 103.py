'''
给定一个二叉树，返回其节点值的锯齿形层序遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回锯齿形层序遍历如下：

[
  [3],
  [20,9],
  [15,7]
]
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        from collections import deque
        right = deque()
        left = deque()
        res = []
        if root is not None:
            left.append(root)
        else:
            return []
        while len(left) > 0 or len(right) > 0:
            temp = []
            if len(left) > 0:
                while len(left) > 0:
                    if left[-1].left is not None:
                        right.append(left[-1].left)
                    if left[-1].right is not None:
                        right.append(left[-1].right)
                    temp.append(left.pop().val)
            elif len(right) > 0:
                while len(right) > 0:
                    if right[-1].right is not None:
                        left.append(right[-1].right)
                    if right[-1].left is not None:
                        left.append(right[-1].left)
                    temp.append(right.pop().val)
            res.append(temp)
        return res
