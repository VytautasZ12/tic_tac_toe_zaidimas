# from zaidimo_fukcijos import patikrinti_ejima
# Lenteles piesimas, skaiciai nurodo vieta lenteleja.
# lentele = "7|8|9|\n4|5|6|\n1|2|3| pradine"
# lenteles skaiciu pakeitimas X arba 0 vietos priskyrimas.

def lenteles_piesimas(vieta):
    lentele = (f"|{vieta[7]}|{vieta[8]}|{vieta[9]}\n"
               f"|{vieta[4]}|{vieta[5]}|{vieta[6]}\n"
               f"|{vieta[1]}|{vieta[2]}|{vieta[3]}")
    print(lentele)


vieta = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}


# Zaideju ejimai, ejimu skaiciavimai, zaidimo vygdymas.


def patikrinti_ejima(ejimas):
    if ejimas % 2 == 0:
        return "0"
    else:
        return "X"


zaidimas = True
ejimas = 0

while zaidimas:
    lenteles_piesimas(vieta)
    zaidimas = input("Pasirinkite skaiciu: ")
    ejimas += 1
    vieta[int(zaidimas)] = patikrinti_ejima(ejimas)
