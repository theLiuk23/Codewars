def unique_in_order(iterable):
    used_chars = []
    solution = []
    for char in iterable:
        if not used_chars.__contains__(char):
            solution.append(char)
            used_chars.append(char)
    return iterable(solution)

print(unique_in_order("AHASFJASF"))