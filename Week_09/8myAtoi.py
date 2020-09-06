class Solution:
    def myAtoi(self, str: str) -> int:
        import re
        matches = re.match('[ ]*([+-]?\d+)', str)
        if matches:
            res = int(matches.group(1))
            if res > (MAX := 2 ** 31 - 1):
                return MAX
            elif res < (MIN := -2 ** 31):
                return MIN
            else:
                return res
        else:
            return 0