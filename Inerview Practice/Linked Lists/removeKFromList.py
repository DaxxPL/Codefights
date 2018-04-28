# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#


def removeKFromList(l, k):
    out = []
    while l is not None:
        if l.value == k:
            if l.next is None:
                break
            l.value = l.next.value
            l.next = l.next.next
        else:
            out.append(l.value)
            if l.next is None:
                break
            l.value = l.next.value
            l.next = l.next.next
    return out



