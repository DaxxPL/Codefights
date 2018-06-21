def push_out(last_l_pushed, last_l, l, out):
    if last_l_pushed is False:
        out.append(l.value)
        if last_l is False:
            l.value = l.next.value
            l.next = l.next.next
            last_l = check_if_last(l)
        else:
            last_l_pushed = True
    return last_l_pushed, last_l, l


def check_if_last(l):
    if l.next is None:
        return True
    else:
        return False


def mergeTwoLinkedLists(l1, l2):
    out = []
    last_l1 = False
    last_l2 = False
    last_l1_pushed = False
    last_l2_pushed = False
    if l1 is None:
        last_l1_pushed = True
    else:
        last_l1 = check_if_last(l1)
    if l2 is None:
        last_l2_pushed = True
    else:
        last_l2 = check_if_last(l2)
    while last_l1_pushed is False or last_l2_pushed is False:
        if last_l1_pushed is False and last_l2_pushed is False:
            if l1.value <= l2.value:
                last_l1_pushed, last_l1, l1 = push_out(last_l1_pushed, last_l1, l1, out)
            else:
                last_l2_pushed, last_l2, l2 = push_out(last_l2_pushed, last_l2, l2, out)
        elif last_l1_pushed is True and last_l2_pushed is False:
            last_l2_pushed, last_l2, l2 = push_out(last_l2_pushed, last_l2, l2, out)
        elif last_l1_pushed is False and last_l2_pushed is True:
            last_l1_pushed, last_l1, l1 = push_out(last_l1_pushed, last_l1, l1, out)
    return out
