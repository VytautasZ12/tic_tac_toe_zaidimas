# Nupiešti lentelę.
# Priskirti skaičius kureis bus galima įrašyti X arba 0 lentelėje.
# Sukurti funkciją kuri patikrintų ar nebus pajimamas tas pats langelis abiejų žaidėjų.
# Sukurti fukciją kurioje būtų nurodomi žaidėjų laimejimo galimybės
#   (horizontaliai, vertikaliai, įstrižai). Nurodytų kuris žaidėjas laimėjo.
# Sukurti funkciją kuri: leistų įvesti žaidėjo vardą,
#                        įvestam vardui priskirtų simbolį (X arba 0),
#                        suks ciklą per lentelę,
#                        atspausdins laimėjusį žaidėję arba lygiąsias.

# Lentelės piešimas:
def lentelės_piešimas(vieta):
    lentelė = (f"|{vieta[7]}|{vieta[8]}|{vieta[9]}\n"
               f"|{vieta[4]}|{vieta[5]}|{vieta[6]}\n"
               f"|{vieta[1]}|{vieta[2]}|{vieta[3]}")
    print(lentelė)

# Priskirti skaičiai kurie pakeis lentelėje esamus skaičius į X arba 0 simbolius.
vieta = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}

įvestų_skaičių_įrašas = []


# Funkcija kuri neleis žaidėjams užimti to paties langelio,
# nurodys, kad langelis užimtas ir leis pasirinkti kitą langelį.
def ėjimų_įvedimas(žaidėjo_vardas):
    while True:
        x = int(input(f"{žaidėjo_vardas}: "))
        x -= 0
        if 0 <= x < 10:
            if x in įvestų_skaičių_įrašas:
                print("Pasirinkta vieta užimta, pasirinkite kitą vietą:")
                continue
            įvestų_skaičių_įrašas.append(x)
            return x
        print("Pasirinkite skaičių nuo 1 iki 9")


# Galimo laimėjimo kombinacijos kiekvienam žaidėjui (X ir 0).
# Horizontaliai, vertikaliai, įstrižai.
def laimėjimo_galimybės(vieta, žaidėjas1, žaidėjas2):
    if (vieta[1] == vieta[2] == vieta[3] == "X"
            or vieta[4] == vieta[5] == vieta[6] == "X"
            or vieta[7] == vieta[8] == vieta[9] == "X"
            or vieta[1] == vieta[4] == vieta[7] == "X"
            or vieta[2] == vieta[5] == vieta[8] == "X"
            or vieta[3] == vieta[6] == vieta[9] == "X"
            or vieta[1] == vieta[5] == vieta[9] == "X"
            or vieta[3] == vieta[5] == vieta[7] == "X"):
        print(f"{žaidėjas1}. Jūs laimėjote!")
        quit()
    elif (vieta[1] == vieta[2] == vieta[3] == "0"
          or vieta[4] == vieta[5] == vieta[6] == "0"
          or vieta[7] == vieta[8] == vieta[9] == "0"
          or vieta[1] == vieta[4] == vieta[7] == "0"
          or vieta[2] == vieta[5] == vieta[8] == "0"
          or vieta[3] == vieta[6] == vieta[9] == "0"
          or vieta[1] == vieta[5] == vieta[9] == "0"
          or vieta[3] == vieta[5] == vieta[7] == "0"):
        print(f"{žaidėjas2}. Jūs laimėjote!")
        quit()
    else:
        return

# Leis įvesti žaidėjo vardą,
# priskirs simboli (X arba 0),
# suks cikla per lentelę tikrinant ėjimus ir laimėjimo galimybes,
# atspausdins laimėtoja arba lygiąsias.
def žaidimas():
    žaidėjas1 = input("Įveskite pirmo žaidėjo vardą: ")
    žaidėjas2 = input("Įveskite pirmo žaidėjo vardą: ")
    print(f" {žaidėjas1}'simbolis yra - X")
    print(f" {žaidėjas2}'simbolis yra - O")
    lentelės_piešimas(vieta)
    for index in range(0, 9):
        if index % 2 == 0:
            index = ėjimų_įvedimas(žaidėjas1)
            vieta[index] = "X"
        else:
            index = ėjimų_įvedimas(žaidėjas2)
            vieta[index] = "0"

        lentelės_piešimas(vieta)
        laimėjimo_galimybės(vieta, žaidėjas1, žaidėjas2)

    print("Lygiosios, bandykite dar kartą 🙂")


žaidimas()
