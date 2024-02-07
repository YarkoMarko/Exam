def func(lst: list):
    lst1 = []

    for value in lst:
        if value[0] in "QWERTYUIOPASDFGHJKLZXCVBNM":
            lst1.append(value)

    return lst1


lst = func(["Fgksdjngkl fdsgfsd", "sadfas", "asfdasdf", "Dsdfgsdgf", "D sfsafd A"])

print(lst)

