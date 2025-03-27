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

def Zene():
    print("Zene")


def Album():
    print("1 - Magyar zenék [Album]")
    print("2 - Angol zenék [Album]")
    print("3 - Kilép")
    choise = int(input("Választás: "))
    while choise != 3:
        if choise == 1:
            for i in range(len(hu)):
               hu[i].Log()
            todo = int(input("Mit akarsz csinálni? [1 - Zene hozzáadás] [2 - Zene kiválasztás] "
                                 "[3 - Zene áthelyezés] [4 - Zene törlése] [5 - Kilépés] "))
            while todo != 5:
                if todo == 1:
                    lista = []
                    print("Írd be a zene előadóját, sorszámát és hosszát: ")
                    artist = input("Előadó: ")
                    title = input("Cím: ")
                    length = input("Hossz: ")

                    hufile = open("magyar_zeneszamok.txt", "a", encoding="utf8")
                    hufile.write(f"{artist};{title};{length}")
                    hufile.close()

                elif todo == 2:
                    print()
                elif todo == 3:
                    print()
                elif todo == 4:
                    print()


        elif choise == 2:
            for i in range(len(en)):
                en[i].Log()
            wichsong = int(input("Válassz egy zenét a sorszáma alapján: "))
            while wichsong > len(hu):
                print("Nincs ezen a helyen zeneszám!")
                wichsong = int(input("Válassz egy zenét a sorszáma alapján: "))
            print(f"{hu[wichsong].artist} {hu[wichsong].title} {hu[wichsong].length}")
            more = input("Akarsz még zenét választani? [I / N]: ")
            while not more in ["I", "N"]:
                print("Hiba!")
                more = input("Akarsz még zenét választani? [I / N]: ")
            if more == "I":
                pass
            elif more == "N":
                choise = 3


        else:
            Menu()