# 1: Nupiesti zaidimo lentele


# Lenteles piesimas, skaiciai nurodo vieta lenteleja.
# lentele = "7|8|9|\n4|5|6|\n1|2|3| sablonas"
# lenteles skaiciu pakeitimas X arba 0 vietos priskyrimas.


def lenteles_piesimas(vieta):
    lentele = (f"|{vieta[7]}|{vieta[8]}|{vieta[9]}\n"
               f"|{vieta[4]}|{vieta[5]}|{vieta[6]}\n"
               f"|{vieta[1]}|{vieta[2]}|{vieta[3]}")
    print(lentele)


vieta = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}

ivestu_skaiciu_irasas = []


# pataisyti ejimus..
def ivedimas(zaidejo_vardas):
    while True:
        x = int(input(f'{zaidejo_vardas}: '))
        x -= 0
        if 0 <= x < 10:
            if x in ivestu_skaiciu_irasas:
                print("Pasirinkta vieta uzimta, pasirinkite kita vieta:")
                continue
            ivestu_skaiciu_irasas.append(x)
            return x
        print("Pasirinkite skaiciu nuo 1-9")


def laimejimo_galimybes(vieta, zaidejas1, zaidejas2):
    if (vieta[1] == vieta[2] == vieta[3] == 'X'
            or vieta[4] == vieta[5] == vieta[6] == 'X'
            or vieta[7] == vieta[8] == vieta[9] == 'X'
            or vieta[1] == vieta[4] == vieta[7] == 'X'
            or vieta[2] == vieta[5] == vieta[8] == 'X'
            or vieta[3] == vieta[6] == vieta[9] == 'X'
            or vieta[1] == vieta[5] == vieta[9] == 'X'
            or vieta[3] == vieta[5] == vieta[7] == 'X'):
        print(f"{zaidejas1}. Tu laimejei!")
        quit()
    elif (vieta[1] == vieta[2] == vieta[3] == 'O'
          or vieta[4] == vieta[5] == vieta[6] == 'O'
          or vieta[7] == vieta[8] == vieta[9] == 'O'
          or vieta[1] == vieta[4] == vieta[7] == 'O'
          or vieta[2] == vieta[5] == vieta[8] == 'O'
          or vieta[3] == vieta[6] == vieta[9] == 'O'
          or vieta[1] == vieta[5] == vieta[9] == 'O'
          or vieta[3] == vieta[5] == vieta[7] == 'O'):
        print(f"{zaidejas2}. Tu laimejei!")
        quit()
    else:
        return


def zaidimas():
    zaidejas1 = input("Iveskite pirmo zaidejo varda: ")
    zaidejas2 = input("Iveskite antro zaidejo varda: ")
    print(f" {zaidejas1}'simbolis yra - X")
    print(f" {zaidejas2}'simbolis yra- O")
    lenteles_piesimas(vieta)
    for index in range(0, 9):
        if index % 2 == 0:
            index = ivedimas(zaidejas1)
            vieta[index] = 'X'
        else:
            index = ivedimas(zaidejas2)
            vieta[index] = 'O'

        lenteles_piesimas(vieta)
        laimejimo_galimybes(vieta, zaidejas1, zaidejas2)

    print("Lygiosios, bandykite dar karta")


zaidimas()
