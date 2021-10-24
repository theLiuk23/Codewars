# it checks if it exists any solutions of k so that:
# a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ... = n * k
def dig_pow(n, p):
    sum = 0
    digits = []

    # gets single digits of n
    for digit in str(n):
        digits.append(int(digit))

    # get the sum (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...)
    for i in range(len(digits)):
        sum += digits[i]**(p+i)

    # if sum / n returns an integer, we have found a special number
    if sum % n == 0:
        return sum // n

    # if not return -1
    else:
        return -1


print(dig_pow(33, 45))