# abcxyz - cab ==> True
# s1     - s2

def scramble(s1, s2):
    index = 0
    s1 = sorted(s1)
    s2 = sorted(s2)

    if s1 == s2:
        return True

    for letter in s2:
        if s1.__contains__(letter):
            s1 = remove(s1, index)
            s2 = remove(s2, index)
        else:
            return False

    return True


def remove(s, index):
    result = s[0: index:] + s[index + 1::]
    return result


print(str(scramble('rkqodlw', 'world')))
print(str(scramble('cedewaraaossoqqyt', 'codewars')))
print(str(scramble('katas', 'steak')))
print(str(scramble('scriptingjava', 'javascript')))
print(str(scramble('scriptjava', 'javascript')))