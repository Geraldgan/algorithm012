from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        if not nums:
            return 0
        self.cnt = 0

        def merge(first, second):
            if first == second:
                return [nums[first]]
            else:
                mid = first + (second - first) // 2
                left = merge(first, mid)
                right = merge(mid + 1, second)
                ans = []
                ll = len(left)
                lr = len(right)

                # 这一部分是用来计数的
                i = j = 0
                while i < ll and j < lr:
                    if left[i] > 2 * right[j]:
                        self.cnt += ll - i
                        j += 1
                    else:
                        i += 1

                # 这一部分是用来合并的
                i = j = 0
                while i < ll and j < lr:
                    if left[i] < right[j]:
                        ans.append(left[i])
                        i += 1
                    else:
                        ans.append(right[j])
                        j += 1
                if i < ll:
                    ans += left[i:]
                if j < lr:
                    ans += right[j:]
            return ans
        merge(0, len(nums) - 1)
        return self.cnt
