def solve():
    real = input()
    a = int(real, 2)
    b = int(input(), 2)

    pre = a ^ b
    pre = bin(pre)[2:]
    test = str(pre)
    while len(test) < len(str(real)):
        test = "0" + test

    print(test)


solve()
