import sys

def add_binary(a, b):
    sum = a + b
    result = ""
    while True:
        result += str(sum % 2)
        sum = int(sum // 2)
        if sum == 0:
            break

    return "".join(reversed(result))