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
    print(inp)
    while inp < 1 or inp > 3:
        print("Hiba!")
        inp = int(input("Választott menüpont: "))
        
    if inp == 1:
        Zene()
    elif inp == 2:
        Album()
        
    return inp


def Zene():
    print("Zene")
    input()

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
    todo = ToDo()
    
    while todo <= 0 or todo >= 6:
        print("Hiba!")
        todo = ToDo()
    
    while todo <= 5 or todo >= 1:
        if todo == 1:
            cont = input("Akarsz még zenét hozzáadni? [I / N]: ").lower()
            while not cont in ["I".lower(), "N".lower()]:
                print("Hiba!")
                cont = input("Akarsz még zenét hozzáadni? [I / N]: ").lower()
                
            if cont == "I".lower():   
                print("Írd be a zene sorszámát, hogy hova kerüljön, az előadójáz, címét és hosszát: ")
                index = input("Sorszám: ").lower()
                artist = input("Előadó: ").lower()
                title = input("Cím: ").lower()
                length = input("Hossz: ").lower()

                hufile = open("magyar_zeneszamok.txt", "a", encoding="utf8")
                hufile.write(f"{index};{artist};{title};{length}\n")
                hufile.close()
            elif cont == "N".lower():
                print("Érzem baszod")
                todo = ToDo()

        elif todo == 2:
            print()
        elif todo == 3:
            print()
        elif todo == 4:
            delete = input("Akarsz még zenét törölni? [I / N]: ").lower()
            while not delete in ["I".lower(), "N".lower()]:
                print("Hiba!")
                delete = input("Akarsz még zenét törölni? [I / N]: ").lower()
            if delete == "I".lower():
                indexDelete = int(input("Írd be a zene sorszámát amit ki akarsz törölni: "))
                while indexDelete > len(current) or indexDelete < 0:
                    print("Nincs ilyen sorszámú zene! ")
                    indexDelete = int(input("Írd be a zene sorszámát amit ki akarsz törölni: "))
                print(f"{indexDelete}. zene törölve lett: {current[indexDelete - 1].Log()}")

                del current[indexDelete - 1]
                file = open(currentfile, "w", encoding="utf8")
                for i in range(len(current)):
                    file.write(f"{current[i].index};{current[i].artist};{current[i].title};{current[i].length}\n")

                
        elif todo == 5:
            Album()

                
        elif choise == 3:
            Menu()
            
