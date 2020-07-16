# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    add = 0
    res = ListNode(0)
    tmp = res

    while True:
        sum = add
        if None != l1:
            sum = sum + l1.val
            l1 = l1.next
        if None != l2:
            sum = sum + l2.val
            l2 = l2.next
        tmp.val = sum % 10
        add = 1 if (1 == sum // 10) else 0
        if l1 or l2 or add:
            tmp.next = ListNode(0);
            tmp = tmp.next
        else:
            break
    return res


class Solution(object):
    l1 = ListNode(1)
    l2 = ListNode(9)
    l2.next = ListNode(9)
    addTwoNumbers(l1, l2)
