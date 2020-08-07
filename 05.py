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

"""
DP solution , refer to https://leetcode-cn.com/problems/longest-palindromic-substring/solution/zui-chang-hui-wen-zi-chuan-by-leetcode-solution/

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = ""
        for l in range(n):
            for i in range(n):
                j = i + l
                if j >= len(s):
                    break
                if l == 0:
                    dp[i][j] = True
                elif l == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
                if dp[i][j] and l + 1 > len(ans):
                    ans = s[i:j+1]
        return ans
"""