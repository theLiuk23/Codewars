import timeit

# it checks if it exists any solutions of k so that:
# a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k
def dig_pow(n, p):
    sum = 0
    digits = []

    for digit in str(n):
        digits.append(int(digit))

    for i in range(len(digits)):
        sum += digits[i]**(p+i)

    if sum % n == 0:
        return sum // n

    else:
        return -1


timeit.timeit()
print(dig_pow(33, 45))