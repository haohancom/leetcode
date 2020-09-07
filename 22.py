def genFullRes(s, lNum, rNum, n):
    res = []
    lLeft = n - lNum
    rLeft = n - rNum
    if lNum == rNum == n:
        res.append(s)
        return res
    if lNum == n and rNum != n:
        for i in range(rLeft):
            s += ')'
        res.append(s)
        return res
    else:
        for i in range(lLeft, -1, -1):
            newS = s
            newLNum = lNum
            newRNum = rNum
            for j in range(i):
                newS += '('
                newLNum += 1
            if newLNum == rNum:
                continue
            newS += ')'
            newRNum += 1
            res += genFullRes(newS, newLNum, newRNum, n)
    return res




def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """
    res = []
    for i in range(n, 0, -1):
        l = r = 0
        s = ''
        for j in range(i):
            s += '('
            l += 1
        s += ')'
        r += 1
        res += genFullRes(s, i, 1, n)
    return res



class Solution(object):
    print(generateParenthesis(3))