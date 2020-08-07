def reverse(x):
    s = str(x)
    if '-' == s[0]:
        s = s[1: len(s)]
        s = '-' + s[::-1]
    else:
        s = s[::-1]

    minNum = '-' + str(pow(2, 31))
    maxNum = str(pow(2, 31) - 1)
    if '-' == s[0] and len(s) >= len(minNum) and s > minNum:
        return 0
    if '-' != s[0] and len(s) >= len(maxNum) and s > maxNum:
        return 0
    return int(s)


class Solution(object):
    x = -123
    print(reverse(x))