def getMax(s, i):
    k = i + 1
    if len(s) % 2 == 1:
        curStr = s[i]
        curLen = 1
        j = i - 1
    else:
        curStr = ''
        curLen = 0
        j = i
    while j >= 0:
        if not s[j] == s[k]:
            return curLen, curStr
        curStr = s[j] + curStr + s[k]
        curLen += 1
        j -= 1
        k += 1
    return curLen, curStr


def longestPalindrome(s):
    i = len(s) // 2 if len(s) % 2 == 1 else len(s) // 2 - 1
    maxLength = 0
    maxString = ''
    while i > 0:
        if i < maxLength:
            return maxString
        curLen, curStr = getMax(s, i)
        maxLength = max(maxLength, curLen)
        if len(curStr) > len(maxString):
            maxString = curStr
        i -= 1
    return maxString


class Solution(object):
    s = longestPalindrome('babad')
    print(s)
