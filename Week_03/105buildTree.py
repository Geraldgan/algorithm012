from typing import List


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 先序找根，划分左右，再递归构造左右子树
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 递归终止条件
        if not preorder or not inorder:
            return
        # 先序为“根左右”，所以根据preorder可以确定root
        root = TreeNode(preorder[0])
        # 中序为“左根右”，根据root可以划分出左右子树
        idx = inorder.index(preorder[0])

        # 下面递归求root的左右子树
        root.left = self.buildTree(preorder[1:1 + idx], inorder[:idx])
        root.right = self.buildTree(preorder[1 + idx:], inorder[idx + 1:])
        return root


if __name__ == '__main__':
    print("res")
