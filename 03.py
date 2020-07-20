def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    currentLength = 0
    maxLength = 0
    l = 0
    r = 0
    charMap = {}
    while r < len(s):
        if s[r] not in charMap or (s[r] in charMap and charMap[s[r]] is False):
            charMap[s[r]] = True
            r += 1
            currentLength += 1
            maxLength = maxLength if maxLength >= currentLength else currentLength
        else:
            while True:
                charMap[s[l]] = False
                currentLength -= 1
                if s[l] == s[r]:
                    l += 1
                    break
                l += 1
    return maxLength


class Solution(object):
    i = lengthOfLongestSubstring("dvdf")
    print(i)