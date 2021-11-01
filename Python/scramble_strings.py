import timeit

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
    if index >= len(s):
        raise Exception("It does not exist an index {} at the string {}".format(index, s))

    return s[0: index:] + s[index + 1::]



print(str(scramble('rkqodlw', 'world')))
print(str(scramble('cedewaraaossoqqyt', 'codewars')))
print(str(scramble('katas', 'steak')))
print(str(scramble('scriptingjava', 'javascript')))
print(str(scramble('scriptjava', 'javascript')))




# SOLUTION:

def scramble(s1,s2):
    for c in set(s2):
        # string.count(char) returns the num of char in the string.
        # e.g.= in "hello" "hello".count(l) ==> 2
        if s1.count(c) < s2.count(c):
            return False
    return True