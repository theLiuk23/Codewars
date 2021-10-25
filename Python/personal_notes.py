# file to test some functions
# pls ignore it


def add_binary(a,b):
    return '{0:o}'.format(a + b)


def add_binary2(a,b):
    """Adds a and b together and returns a binary string"""
    return bin(a + b)[2::]


print(add_binary2(6, 5))