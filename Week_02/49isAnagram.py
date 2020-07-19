
# 通过set去重，再直接比较字符的个数
def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    se = set(s)
    if se == set(t):
        for i in se:
            if s.count(i) != t.count(i):
                return False
        return True
    else:
        return False


# hasp map的方法
def isAnagram2(self, s, t):
    if len(s) != len(t):
        return False

    counter = {}
    for char in s:
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1

    for char2 in t:
        if char2 in counter:
            counter[char2] -= 1
        else:
            return False
    for count in counter.values():
        if count != 0:
            return False
    return True


result = isAnagram2("anagram", "anagram", "nagaram")
if result:
    print("True")
else:
    print("False")
