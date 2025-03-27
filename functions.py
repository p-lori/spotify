import classes

def ReadFile(path):
    fileList = []
    file = open(path, "r", encoding="utf8")
    for i in file:
        fileList.append(classes.Separate(i))
    file.close()
    return fileList

def Menu():
    print("1 - Zenék\n2 - Albumok\n3 - Kilép")

def Zene():
    print("Zene")

def Album():
    print("1 - Magyar zenék [Album]")
    print("2 - Angol zenék [Album]")
    print("3 - Kilép")
    choise = int(input("Választás: "))
    while choise != 3:
        if choise == 1:
            print()
        elif choise == 2:
            print()

