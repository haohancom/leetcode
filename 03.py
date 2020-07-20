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
            maxLength = max(maxLength, currentLength)
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


'''
CaptainTec
2020-05-02
哈希Map 只需一次遍历, more efficiency
附 Python 代码

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        k, res, c_dict = -1, 0, {}
        for i, c in enumerate(s):
            if c in c_dict and c_dict[c] > k:  # 字符c在字典中 且 上次出现的下标大于当前长度的起始下标
                k = c_dict[c]
                c_dict[c] = i
            else:
                c_dict[c] = i
                res = max(res, i-k)
        return res
'''