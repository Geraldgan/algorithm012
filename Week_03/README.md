学习笔记
算法模板
* 前中后序遍历
def preorder_traversal(self, tree):
        if (tree.root is not None):
            self.out_list_temp.append(tree.root)
        if tree.left is not None:
            self.preorder_traversal(tree.left)
        if tree.right is not None:
            self.preorder_traversal(tree.right)
        return self.out_list_temp

def preorder_traversal_print(self, tree):
        print(self.preorder_traversal(tree))
        self.out_list_temp = []

def inorder_traversal(self, tree):
        if tree.left is not None:
            self.inorder_traversal(tree.left)
        if (tree.root is not None):
            self.out_list_temp.append(tree.root)
        if tree.right is not None:
            self.inorder_traversal(tree.right)
        return self.out_list_temp


* DFS代码模板(递归写法)
visited = set()

def dfs(node, visited):
    if node in visited:
        return
    visited.add(node)
    
    for next_node in node.children():
        if not next_node in visited:
            dfs(next_node, visited)


* DFS代码模板(非递归写法)
def DFS(self, tree):
    if tree.root is None:
        return []
        
    visited, stack = [], [tree.root]
    
    while stack:
        node = stack.pop()
        visited.add(node)
        
        process(node)
        nodes = generate_related_nodes(node)
        stack.push(nodes)


