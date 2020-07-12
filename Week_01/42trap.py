
# 方法1:按层来算
# 1、利用左右指针的下标差值计算出每一行雨水+柱子的体积，累加得到整体体积pillars_height。（从左边第一个格子到右边第一个格子开始算起）
# 2、计算柱子体积，为height：[0,1,0,2,1,0,1,3,2,1,2,1]数组之和SUM=14
# 3、返回结果 pillars_height−SUM就是雨水的体积
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        pillars_height, tmp, high = 0, 0, 1
        while(left <= right):
            while(left <= right and height[left] < high):
                pillars_height += height[left]
                left += 1
            while(right >= left and height[right] < high):
                pillars_height += height[right]
                right -= 1
            high += 1
            tmp += right-left+1
        return tmp-pillars_height


# 方法2:双指针法
def trap2(self, height):
    """
    :type height: List[int]
    :rtype: int
    """
    if not height:
        return 0

    left, right = 0, len(height) - 1
    maxLeft, maxRight = height[left], height[right]
    area = 0
    while left <= right:
        maxLeft = max(maxLeft, height[left])
        maxRight = max(maxRight, height[right])
        if maxLeft < maxRight:
            area += maxLeft - height[left]
            left += 1
        else:
            area += maxRight - height[right]
            right -= 1
    return area
