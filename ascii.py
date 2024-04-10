length = 10
astr = "*"

for _ in range(10):
    for i in range(length):
        for j in range(length - i):
            print(" ", end='')
        print(astr)
        astr += "**"

    for i in range(length):
        for j in range(i + 1):
            print(" ", end='')
        astr = astr[:-2]
        print(astr)
