def mysplit(strng):
    lst = []
    palavra = ""
    if len(strng) == 0:
        return lst
    for i, char in enumerate(strng):
        if char == " ":
            if palavra != "": lst.append(palavra)
            palavra = ""
            continue
        palavra += char
        if i == len(strng) - 1 and palavra != "":
            lst.append(palavra)
    return lst


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
    