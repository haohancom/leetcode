d1 = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 0: ''}
d2 = {1: 'X', 2: 'XX', 3: 'XXX', 4: 'XL', 5: 'L', 6: 'LX', 7: 'LXX', 8: 'LXXX', 9: 'XC', 0: ''}
d3 = {1: 'C', 2: 'CC', 3: 'CCC', 4: 'CD', 5: 'D', 6: 'DC', 7: 'DCC', 8: 'DCCC', 9: 'CM', 0: ''}
d4 = {1: 'M', 2: 'MM', 3: 'MMM'}

def intToRoman(num):
    res = ''
    res = d1[num % 10] + res
    num //= 10
    if 0 == num:
        return res

    res = d2[num % 10] + res
    num //= 10
    if 0 == num:
        return res

    res = d3[num % 10] + res
    num //= 10
    if 0 == num:
        return res

    res = d4[num % 10] + res
    return res

class Solution(object):
    s = intToRoman(399)
    print(s)
