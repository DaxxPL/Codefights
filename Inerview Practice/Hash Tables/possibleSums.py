
def possibleSums(coins, quantity):
    results = set()
    results.add(0)
    for i in range(len(coins)):
        coin = coins[i]
        quant = quantity[i]
        for item in frozenset(results):
            for ii in range(1, quant+1):
                tmp = item+coin*ii
                results.add(tmp)
    return len(results) - 1
