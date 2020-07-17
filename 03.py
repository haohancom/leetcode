def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    currentString = s[0:1]
    currentLength = 1
    maxLength = 1
    for i, val in enumerate(s):
        mergedString = mergedString(val, s)


def s2hex(s):
    return hex(int(s, 16))

def mergeCharWithString(c, s):
    index = ord(c) - ord('a')
    location = index // 4
    indexHex: str = hex(1 << index % 4)
    res = hex(int(s, 16) | int(indexHex + '0' * location, 16))
    if s==res:
        res = hex(int(s, 16) ^ int(indexHex + '0' * location, 16))
    return res

def judgeCharBelongs2String(s, c):
    return True if s == (s & c) else False

class Solution(object):
    lengthOfLongestSubstring("abc")