from collections import defaultdict
from collections import deque


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        # 建立通用list
        size, general_dic = len(beginWord), defaultdict(list)
        for w in wordList:
            for j in range(size):
                general_dic[w[:j]+"*"+w[j+1:]].append(w)
        # BFS
        queue = deque()
        # 因为在BFS中，queue中通常会同时混合多层的node，这就无法区分层了，要区分层就要queue中直接加入当前node所属层数。
        queue.append((beginWord, 1))
        # bool 的默认值是false，因此所有不在list里的是false
        mark_dic = defaultdict(bool)
        mark_dic[beginWord] = True
        while queue:
            cur_word, level = queue.popleft()   # queue头出来一个
            for i in range(size):               # 找邻居，这里的所有邻居都在level+1层
                for neighbour in general_dic[cur_word[:i]+"*"+cur_word[i+1:]]:
                    if neighbour == endWord:
                        return level + 1
                    if not mark_dic[neighbour]:
                        mark_dic[neighbour] = True
                        # 符合条件（neighbour + unmarked)的进去
                        queue.append((neighbour, level+1))
        return 0


if __name__ == '__main__':
    solution = Solution()
    res = solution.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot",
                                "log", "cog"])
    print(res)
