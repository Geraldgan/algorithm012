from typing import List


class Solution:
    # 贪心：尽可能到达最远位置（最远能到达某个位置，就一定能到达它前面的任何位置）
    def canJump(self, nums: List[int]) -> bool:
        if nums == [0]:
            return True
        maxDist = 0
        end_index = len(nums)-1
        for i, jump in enumerate(nums):
            if maxDist >= i and i+jump > maxDist:
                maxDist = i+jump
                if maxDist >= end_index:
                    return True

        return False

    # 倒序贪心算法
    def canJump2(self, nums: List[int]) -> bool:
        index = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= index:
                index = i
        return index == 0


if __name__ == '__main__':
    solution = Solution()
    res = solution.canJump2([2, 3, 1, 1, 4])
    print(res)
