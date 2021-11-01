import timeit

# abcxyz - cab ==> True
# aaaabc - abc
# s1     - s2

def scramble(s1, s2):
    if s1 == s2:
        return True

    for letter in s2:
        if s1.__contains__(letter):
            s1 = remove(s1, s1.index(letter))
            s2 = remove(s2, s2.index(letter))
        if not s1.__contains__(letter):
            return False

    return True


def remove(s, index):
    if index >= len(s):
        raise Exception("It does not exist an index {} at the string {}".format(index, s))

    return s[0: index:] + s[index + 1::]



print(timeit.timeit("scramble('rkqodlw', 'world')", setup="from __main__ import scramble"))




# SOLUTION:

def scramble2(s1,s2):
    for c in set(s2):
        # string.count(char) returns the num of char in the string.
        # e.g.= in "hello" "hello".count(l) ==> 2
        if s1.count(c) < s2.count(c):
            return False
    return True


print(str(timeit.timeit("scramble2('rkqodlw', 'world')", setup="from __main__ import scramble2")))