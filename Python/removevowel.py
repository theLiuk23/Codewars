vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

def disemvowel(string_):
    text = string_
    solution = ""

    for letter in text:
        if not vowels.__contains__(letter):
            solution+=letter
    
    return solution


print(disemvowel("ciao sono Luca!"))