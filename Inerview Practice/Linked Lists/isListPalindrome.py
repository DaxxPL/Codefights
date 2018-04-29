# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#


def isListPalindrome(l):
    table = []
    while l:
        table.append(l.value)
        l = l.next
    if table == table[::-1]:
        return True
    else:
        return False