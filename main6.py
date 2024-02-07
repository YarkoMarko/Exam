def func(lst: list):
    lst1 = []

    for value in lst:
        if "Python" in value:
            lst1.append(value)

    return lst1


lst = func(["Python fdsgfsd", "sadfas", "asfdasdfPython", "Dsdfgsdgf", "D sfsafd A", "adsafd asdf Python", "safsaf"])

print(lst)

