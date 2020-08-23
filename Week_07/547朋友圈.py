from typing import List


class Solution:
    # 方法一：DFS
    def findCircleNum(self, M: List[List[int]]) -> int:
        N = len(M)
        count = 0
        visited = set()

        def dfs(i):
            for j in range(N):
                if M[i][j] and j not in visited:
                    visited.add(j)
                    dfs(j)

        for i in range(N):
            if i not in visited:
                count += 1
                visited.add(i)
                dfs(i)

        return count

    # 方法二：并查集
    def findCircleNum2(self, M: List[List[int]]) -> int:
        f = {}
        s = {}
        count = len(M)

        def find(x):
            f.setdefault(x, x)
            # 路径压缩
            if x != f[x]:
                f[x] = find(f[x])
            return f[x]

        def union(x, y):
            nonlocal count
            x_father, y_father = find(x), find(y)
            if x_father == y_father:
                return
            # 将小树的根节点连接到大叔的根节点
            if s.setdefault(x_father, 1) < s.setdefault(y_father, 1):
                f[x_father] = y_father
                s[y_father] += s[x_father]
            else:
                f[y_father] = x_father
                s[x_father] += s[y_father]
            count -= 1

        for i in range(len(M)):
            for j in range(i + 1, len(M)):
                if M[i][j] == 1:
                    union(i, j)
        return count


if __name__ == '__main__':
    solution = Solution()
    res = solution.findCircleNum([[1, 1, 0], [1, 1, 1], [0, 1, 1]])
    print(res)
    res = solution.findCircleNum2([[1, 1, 0], [1, 1, 1], [0, 1, 1]])
    print(res)
