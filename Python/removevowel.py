vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

def disemvowel(string_):
    text = string_
    solution = ""

    for letter in text:
        if not vowels.__contains__(letter):
            solution+=letter
    
    return solution



#1 return s.translate(None, "aeiouAEIOU")
#2 return "".join(c for c in string if c.lower() not in "aeiou")
#3 for i in "aeiouAEIOU":
    #     s = s.replace(i,'')
    # return s

print(disemvowel("ciao sono Luca!"))