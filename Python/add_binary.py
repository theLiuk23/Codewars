import math

def add_binary(a, b):
    sum = a + b
    result = 0
    for i in range(0, math.log2(sum)):
        result += sum % 2

    return result

print(add_binary(156))