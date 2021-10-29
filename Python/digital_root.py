def digital_root(n):
    # result = n so that if n < 10 it returns immidiately n
    result = n

    # operates only if the previous result was greater or equal to 10
    while result >= 10:
        result = sum_nums(n)
        print("result= " + str(result))
        n = result

    return result

# returns the sum of the given num's figures
def sum_nums(n):
    sum = 0
    for figure in str(n):
        sum += int(figure)
    return sum


print(str(digital_root(7577854349)))