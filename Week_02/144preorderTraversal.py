# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # 递归的方法
    def preorderTraversal(self, root):
        res = []

        def dfs(root):
            nonlocal res
            if not root:
                return

            res.append(root.val)
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return res

    # 栈的方法
    def preorderTraversal2(self, root):
        if not root:
            return []
        stack, res = [root], []
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)  # 根节点值加入到结果中
                if node.right:
                    stack.append(node.right)  # 右子树入栈
                if node.left:
                    stack.append(node.left)  # 左子树入栈
        return res
