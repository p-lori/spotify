import classes
import functions

print("Spotify")

en = functions.ReadFile("english_songs.txt")
hu = functions.ReadFile("magyar_zeneszamok.txt")

functions.Menu()
inp = int(input("Választott menüpont: "))
while inp != 3:
    if inp == 1:
        functions.Zene()
    elif inp == 2:
        functions.Album()
    else:
        print("Hiba!")
        inp = int(input("Választott menüpont: "))

