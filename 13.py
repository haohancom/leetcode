def romanToInt(s):
    roman_dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    strLen = len(s)
    res = 0
    for i in range(strLen):
        if i < strLen - 1 and roman_dic[s[i]] < roman_dic[s[i + 1]]:
            res -= roman_dic[s[i]]
        else:
            res += roman_dic[s[i]]
    return res


class Solution(object):
    i = romanToInt('CCCXCIX')
    print(i)



