string = ["cat", "dog", "dog"]
pattern = ["a", "a", "b"]


def areFollowingPatterns(strings, patterns):
    mapas = {}
    mapap = {}
    counter_p = 0
    counter_s = 0
    for i in range(0, len(strings)):
        if patterns[i] in mapap:
            ans_p = mapap[patterns[i]]
        else:
            mapap[patterns[i]] = counter_s
            ans_p = mapap[patterns[i]]
            counter_s += 1
        if strings[i] in mapas:
            ans_s = mapas[strings[i]]
        else:
            mapas[strings[i]] = counter_p
            ans_s = mapas[strings[i]]
            counter_p += 1
        if ans_p != ans_s:
            return False
    return True


print(set(string), set(pattern), set(zip(string, pattern)))

