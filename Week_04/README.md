weak04 学习笔记
算法模板
* BFS的标准套路
    
```
for head in all_node()
    if head 没有visited过   # 以上两步是为了防止有孤立的部分存在而被遗漏，如果没有孤立的部分可以不写，直接放queue里一个就开始循环即可

    queue.append(head)
    mark head

    # 主干部分
    while queue is not empty:
    cur_node = queue.pop() # 我们不需要关心node将会以何种顺序出queue，我们只在乎如何往queue里进就行了。

    # 找邻居
    for 所有 cur_node 的邻居们：
           if cur_neighbour 没有visit过：

               deal -> cur_neighbour
               mark -> cur_neighbour
               inject -> cur_neighbour
```


* 二分查找模版
```
left, right = 0, len(array) - 1 
while left <= right: 
  mid = (left + right) / 2 
  if array[mid] == target: 
        # find the target!! 
        break or return result 
  elif array[mid] < target: 
        left = mid + 1 
  else: 
        right = mid - 1

```


* 贪心算法 (Greedy)
```
    贪心算法是一种在每一步选择中都采取在当前状态下最好或最优(即最有利)的选择，从而希望导致结果是全局最好或最优的算法。
贪心算法与动态规划的不同在于它对每个子问题的解决方案都做出选择，不能回退。动态规划则会保存以前的运算结果，并根据以前的结果对当前进行选择，有回退功能。
适用贪心算法的场景: 简单地说，问题能够分解成子问题来解决，子问题的最优解能递推到最终问题的最优解。

```



