def inverte(string):
    if len(string) <= 1:
        return string
    return inverte(string[1:]) + string[0]

print(inverte('python'))




