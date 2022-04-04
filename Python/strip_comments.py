# non completato

def strip_comments(text, markers):
    # pieces of string that will be deleted
    trash = []
    for line in text.split('\n'):
        for marker in markers:
            if line.__contains__(marker):
                trash.append(marker + line.split(marker)[1])
    
    for piece in trash:
        text = text.replace(piece, '')
        
    text = ''.join([line.rstrip()+'\n' for line in text.splitlines()])
    text = text.strip()

    return text


solution = strip_comments("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
print(solution)