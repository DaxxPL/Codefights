
def groupingDishes(dishes):
    done = []
    out = []
    key_map = {}
    counter = 0
    for i in dishes:
        for y in i[1:]:
            if y in key_map:
                done[key_map[y]].append(i[0])
            else:
                key_map[y] = counter
                counter += 1
                done.append([y, i[0]])
    for i in done:
        if len(i) > 2:
            tmp = i[0]
            i = sorted(i[1:])
            i.insert(0, tmp)
            out.append(i)
    return sorted(out)
