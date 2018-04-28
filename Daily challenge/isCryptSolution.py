

def isCryptSolution(crypt, solution):
    d = {}
    for i in solution:
        d[i[0]] = i[1]
    equation = ['', '', '']
    for item in range(0, len(crypt)):
        for letter in crypt[item]:
            equation[item] += d[letter]
    for i in range(0, 3):
         if ((len(equation[i]) > 1) and (equation[i][0] =='0')):
            return False
    print(equation)
    return int(equation[0]) + int(equation[1]) == int(equation[2])

