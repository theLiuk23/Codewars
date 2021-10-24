import math
import sys

def add_binary(a, b):
    sum = a + b
    print("max: " + str(sys.maxsize))
    print(type(sum))
    result = ""
    while True:
        result += str(sum % 2)
        # print("sum: " + str(sum) + "; result: " + result)
        sum = int(sum // 2)
        # print(str(sum))
        if sum == 0:
            break

    return "".join(reversed(result))

print(add_binary(6906393867515314436669271, 1375110409054115922127037))