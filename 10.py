import re


def isMatch(s, p):
    res = re.compile(p).findall(s)
    return bool(res and res[0] == s)


class Solution(object):
    print(isMatch('ab', ".c"))
