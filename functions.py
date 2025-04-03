import classes

def ReadFile(path):
    fileList = []
    file = open(path, "r", encoding="utf8")
    for i in file:
        fileList.append(classes.Separate(i))
    file.close()
    return fileList

en = ReadFile("english_songs.txt")
hu = ReadFile("magyar_zeneszamok.txt")

def Menu():
    print("1 - Zenék\n2 - Albumok\n3 - Kilép")
    inp = int(input("Választott menüpont: "))
    while inp < 1 or inp > 3:
        print("Hiba!")
        inp = int(input("Választott menüpont: "))
        
    if inp == 1:
        Zene()
    elif inp == 2:
        Album()
    elif inp == 3:
        inp = 3

        
    return inp


def Zene():
    for i in range(len(en)):
        print("Összes zene")


def ToDo():
    todo = int(input("Mit akarsz csinálni? [1 - Zene hozzáadás] [2 - Zene kiválasztás] "
                                 "[3 - Zene áthelyezés] [4 - Zene törlése] [5 - Kilépés] "))
    return todo

def Album():
    print("1 - Magyar zenék [Album]")
    print("2 - Angol zenék [Album]")
    print("3 - Kilép")
    choise = int(input("Választás: "))
    while choise > 3 or choise < 1:
        print("Hiba!")
        choise = int(input("Választás: "))
        
    current = hu
        
    if choise == 1:
        for i in range(len(hu)):
            current = hu
            currentfile = "magyar_zeneszamok.txt"
            print(current[i].Log())
    elif choise == 2:
        for i in range(len(en)):
            current = en
            currentfile = "english_songs.txt"
            print(current[i].Log())
    elif choise == 3:
        while Menu() == 3:
            Menu()

    todo = ToDo()

    while todo <= 0 or todo >= 6:
        print("Hiba!")
        todo = ToDo()

    while todo <= 5 or todo >= 1:
        if todo == 1:
            print("Írd be a zene sorszámát, hogy hova kerüljön, az előadójáz, címét és hosszát: ")
            index = int(input("Sorszám: "))
            artist = input("Előadó: ").lower()
            title = input("Cím: ").lower()
            length = input("Hossz: ").lower()

            current.insert(index - 1, f"{index};{artist};{title};{length}")
            print(current[index])

            f = open(currentfile, "w", encoding="utf8")
            for i in range(len(current)):
                f.write(f"{current[i].index};{current[i].artist};{current[i].title};{current[i].length}\n")
            f.close()
            cont = input("Akarsz még zenét hozzáadni? [I / N]: ").lower()
            while not cont in ["I".lower(), "N".lower()]:
                print("Hiba!")
                cont = input("Akarsz még zenét hozzáadni? [I / N]: ").lower()

                if cont == "I".lower():
                    continue
                elif cont == "N".lower():
                    todo = ToDo()

        elif todo == 2:
            chooseIndex = int(input("Írd be a zene sorszámát amit ki akarsz választani: "))
            while chooseIndex > len(current) or chooseIndex < 0:
                print("Hiba!")
                chooseIndex = int(input("Írd be a zene sorszámát amit ki akarsz választani: "))
            print(current[chooseIndex - 1].Log())
            conti = input("Akrasz még zenét választani? [I / N]: ").lower()
            while not conti in ["I".lower(), "N".lower()]:
                print("Hiba!")
                conti = input("Akrasz még zenét választani? [I / N]: ").lower()
            if conti == "I".lower():
                continue
            elif conti == "N".lower():
                Album()

        elif todo == 3:
            wich = int(input("Melyik zenét akarod kicserélni: "))
            while wich > len(current) or wich < 0:
                print("Hiba!")
                wich = int(input("Melyik zenét akarod kicserélni: "))

            current.pop(wich)

        elif todo == 4:
            indexDelete = int(input("Írd be a zene sorszámát amit ki akarsz törölni: "))
            while indexDelete > len(current) or indexDelete < 0:
                print("Nincs ilyen sorszámú zene! ")
                indexDelete = int(input("Írd be a zene sorszámát amit ki akarsz törölni: "))
            print(f"{indexDelete}. zene törölve lett: {current[indexDelete - 1].Log()}")
            current.pop(indexDelete - 1)

            delete = input("Akarsz még zenét törölni? [I / N]: ").lower()
            while not delete in ["I".lower(), "N".lower()]:
                print("Hiba!")
                delete = input("Akarsz még zenét törölni? [I / N]: ").lower()
            if delete == "I".lower():
                continue
            elif delete == "N".lower():
                file = open(currentfile, "w", encoding="utf8")
                for i in range(len(current)):
                    file.write(f"{current[i].index};{current[i].artist};{current[i].title};{current[i].length}\n")
                file.close()
                Album()


        elif todo == 5:
            Album()
