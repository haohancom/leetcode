def convert(s, numRows):
    res = ''
    if 1 == numRows:
        return s
    for i in range(numRows):
        j = i
        if 0 == i or numRows - 1 == i:
            while j < len(s):
                res += s[j]
                j += 2 * numRows - 2
        else:
            while j < len(s):
                res += s[j]
                k = j + 2 * (numRows - i - 1)
                if k < len(s):
                    res += s[k]
                j += 2 * numRows - 2

    return res


class Solution(object):
    res = convert("A", 1)
    print(res)
