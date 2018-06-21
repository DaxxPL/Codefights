# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#


def addTwoHugeNumbers(a, b):
    x1 = convert_to_int(a)
    x2 = convert_to_int(b)
    result = x1 + x2
    print(x1, x2, result)
    conv_result = convert_to_linked_list(result)
    return list(reversed(conv_result))


def convert_to_int(x):
    result = 0
    base = 10 ** 4
    counter = 0
    done = False
    result += x.value
    if x.next is not None:
        x.value = x.next.value
        x.next = x.next.next
        done = True
        counter += 1
    while x.next is not None:
        result *= base
        result += x.value
        x.value = x.next.value
        x.next = x.next.next
        counter += 1
        done = True
    if done:
        result *= base
        result += x.value
    return result


def convert_to_linked_list(x):
    out = []
    done = False
    while x:
        done = True
        tmp = x % 10000
        x = x // 10000
        out.append(tmp)
    if done:
        out.append(0)
    return out
