# 方法三：动态规划
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # 状态：以该点结尾的最长有效括号的子串长度
        dp = [0 for _ in range(len(s))]
        if len(s) < 2:
            return 0

        if s[1] == ')' and s[0] == '(':
            dp[1] = 2

        if len(s) == 2:
            return dp[1]

        for i in range(2, len(s)):
            if s[i] == '(':     # 一种情况
                dp[i] = 0
                continue
            if s[i] == ')':    # 另一种情况
                if s[i-1] == '(':       # 细分
                    dp[i] = dp[i-2] + 2
                if s[i-1] == ')' and s[i-1-dp[i-1]] == '(' and i-1-dp[i-1] >= 0:  # 复杂的一种情况，需要特判
                    dp[i] = dp[i - 1 - dp[i-1] - 1] + 2 + dp[i-1]
        print(dp)
        return max(dp)


if __name__ == '__main__':
    solution = Solution()
    res = solution.longestValidParentheses(")()())")
    print(res)
