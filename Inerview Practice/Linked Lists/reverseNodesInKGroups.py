def push_out(l_l, is_last, last_l_pushed):
    out = l_l.value
    if is_last is False:
        l_l.value = l_l.next.value
        l_l.next = l_l.next.next
        is_last = check_if_last(l_l)
    else:
        last_l_pushed = True
    return l_l, is_last, last_l_pushed, out


def check_if_last(l):
    if l.next is None:
        return True
    return False


def reverseNodesInKGroups(l, k):
    is_last = False
    last_l_pushed = False
    counter = 0
    is_last = check_if_last(l)
    out = []
    temp = []
    while last_l_pushed is False:
        l, is_last, last_l_pushed, val = push_out(l, is_last, last_l_pushed)
        if counter < k:
            temp.insert(0, val)
            counter += 1

        if counter == k:
            counter = 0
            out.extend(temp)
            temp = []
    if temp:
        out.extend(list(reversed(temp)))
    return out
