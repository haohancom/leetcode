import re

#refer to : https://leetcode-cn.com/problems/string-to-integer-atoi/solution/python-1xing-zheng-ze-biao-da-shi-by-knifezhu/

def myAtoi(str):
    INT_MAX = 2147483647
    INT_MIN = -2147483648
    str = str.lstrip()
    num_re = re.compile(r'^[\+\-]?\d+')
    num = num_re.findall(str)
    num = int(*num)
    return max(min(num, INT_MAX), INT_MIN)


class Solution(object):
    i = myAtoi('    -42')
    print(i)
