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


def rearrangeLastN(l, n):
    is_last = False
    last_l_pushed = False
    if l is None:
        last_l_pushed = True
    else:
        is_last = check_if_last(l)
    out = []
    while last_l_pushed is False:
        l, is_last, last_l_pushed, val = push_out(l, is_last, last_l_pushed)
        out.append(val)
    return out[len(out) - n:] + out[:len(out) - n]
