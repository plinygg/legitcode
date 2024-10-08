# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.


fibonacci = [1, 2, 3, 5]
sum = 2
value = 4*(10**6)

while fibonacci[-1] < value:
    newfib = fibonacci[-1] + fibonacci[-2]
    # print('rar', newfib)
    fibonacci.append(newfib)
    # print('fibonacci', fibonacci)
    if newfib % 2 == 0:
        sum = sum + newfib
    # print('sum', sum)

print(sum)
# should print 4613732