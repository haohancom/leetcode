def longestCommonPrefix(strs):
    index = 0
    res = ''
    while True:
        if 0 == len(strs):
            return res
        if len(strs[0]) == index:
            return res
        c = strs[0][index]
        for s in strs:
            if len(s) == index:
                return res
            if c != s[index]:
                return res
        res += c
        index += 1


class Solution(object):
    strs = ["abca","abc"]
    s = longestCommonPrefix(strs)
    print(s)
