weak06 学习笔记
动态规划

* 基本思想:
问题的最优解如果可以由子问题的最优解推导得到，则可以先求解子问题的最优解，在构造原问题的最优解；若子问题有较多的重复出现，则可以自底向上从最终子问题向原问题逐步求解。


* 使用条件：
可分为多个相关子问题，子问题的解被重复使用
1、优化子结构：
    一个问题的优化解包含了子问题的优化解
    缩小子问题集合，只需那些优化问题中包含的子问题，降低实现复杂性
2、我们可以自下而上的
    重叠子问题：在问题的求解过程中，很多子问题的解将被多次使用。
    

* 步骤：
1、分析优化解的结构
2、递归地定义最优解的代价
3、自底向上地计算优化解的代价保存之，并获取构造最优解的信息
4、根据构造最优解的信息构造优化解
    