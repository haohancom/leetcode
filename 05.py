def getMax(s, i):
    j = i
    k = i + 1
    curLen = 0
    curStr = ''
    while j >= 0 and k < len(s):
        if not s[j] == s[k]:
            break
        curStr = s[j] + curStr + s[k]
        curLen += 2
        j -= 1
        k += 1

    _curStr = s[i]
    _curLen = 1
    j = i - 1
    k = i + 1
    while j >= 0 and k < len(s):
        if not s[j] == s[k]:
            break
        _curStr = s[j] + _curStr + s[k]
        _curLen += 2
        j -= 1
        k += 1

    if curLen > _curLen:
        return curLen, curStr
    else:
        return _curLen, _curStr


def longestPalindrome(s):
    i = 0
    maxLength = 0
    maxString = ''
    while i < len(s):
        if i < maxLength // 2 or len(s) - 1 - i < maxLength // 2:
            return maxString
        curLen, curStr = getMax(s, i)
        maxLength = max(maxLength, curLen)
        if len(curStr) > len(maxString):
            maxString = curStr
        i += 1
    return maxString


class Solution(object):
    s = longestPalindrome('ccc')
    print(s)
