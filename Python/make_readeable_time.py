from cgitb import reset


def make_readable(seconds:int):
    result = []
    result.append(str(int(seconds / 3600))) # hours
    result.append(str(int((seconds % 3600) / 60))) # minutes
    result.append(str((seconds % 3600) % 60)) # seconds
    
    for element in result:
        if element == "0":
            result[result.index(element)] = "00"
            continue
        if int(element) < 10:
            result[result.index(element)] = "0" + element
    
    return ":".join(result)

    ### #1
    # return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)

while True:
    print(make_readable(int(input("secondi: "))))