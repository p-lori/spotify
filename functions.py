import classes


def ReadFile(path):
    fileList = []
    file = open(path, "r", encoding = "utf8")
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
    print("Összes zene az alkalmazásban")
    for i in range(len(en)):
        print(en[i].Log())

    for i in range(len(hu)):
        print(hu[i].Log())

    hm = input("3 - Kilép: ")

    while hm != "3":
        print("Hiba!")
        hm = input("3 - Kilép: ")

    Menu()


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

            new_song = f"{index};{artist};{title};{length}"
            current.insert(index - 1, classes.Separate(new_song))
            print(current[index])

            f = open(currentfile, "w", encoding = "utf8")
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
            print(f"A választott zenéd: {current[wich - 1].artist} | {current[wich - 1].title}")
            current.pop(wich - 1)

            print("Milyen zenét akrasz a helyére?")
            toWitchArtist = input("Előadó: ")
            toWitchTitle = input("Cím:")
            toWitchLength = input("Hossz: ")

            swap_song = f"{wich};{toWitchArtist};{toWitchTitle};{toWitchLength}"
            current.insert(wich - 1, classes.Separate(swap_song))

            swapCont = input("Akarsz még zenét kicserélni? [I / N]: ").lower()
            while not swapCont in ["I".lower(), "N".lower()]:
                print("HIba!")
                swapCont = input("Akarsz még zenét kicserélni? [I / N]: ").lower()
            if swapCont == "I".lower():
                continue
            elif swapCont == "N".lower():
                swapFile = open(currentfile, "w", encoding = "utf8")
                for i in range(len(current)):
                    swapFile.write(f"{current[i].index};{current[i].artist};{current[i].title};{current[i].length}\n")
                swapFile.close()
                Album()

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
                file = open(currentfile, "w", encoding = "utf8")
                for i in range(len(current)):
                    file.write(f"{current[i].index};{current[i].artist};{current[i].title};{current[i].length}\n")
                file.close()
                Album()

        else:
            Album()
