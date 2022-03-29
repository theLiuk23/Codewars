def expanded_form(num):
    # digits of num
    length = len(str(num))
    result = ""
    # foreach digit in num
    for figure in str(num):
        length -= 1
        # if digit is 0 skip
        if figure == "0":
            continue
        # add figure + "0" length times
        result += figure + "0"*length + " + "
    # removes the exceeding " + "
    result = result[:-3]
    return result

print(expanded_form(1021))