def lentelės_piešimas(vieta):
    print("      {} | {} | {} ".format(vieta[6], vieta[7], vieta[8]))
    print("\t ___|___|___")
    print("      {} | {} | {} ".format(vieta[3], vieta[4], vieta[5]))
    print("\t ___|___|___")
    print("      {} | {} | {} ".format(vieta[0], vieta[1], vieta[2]))
    print("\t    |   |   ")


def rezultatai(taškai):
    print("\t-------------------")
    print("\t Rezultatų lentelė")
    print("\t-------------------")

    žaidėjų_sąrašas = list(taškai.keys())

    print("\t ", žaidėjų_sąrašas[0], "\t", taškai[žaidėjų_sąrašas[0]])
    print("\t ", žaidėjų_sąrašas[1], "\t", taškai[žaidėjų_sąrašas[1]])
    print("\t-------------------\n")


def laimėjimo_patvirtinimas(žaidėjo_vieta, žaidėjo_ėjimas):
    laimėjimo_kombinacijos = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for kombinacijos in laimėjimo_kombinacijos:
        if all(skaičiai in žaidėjo_vieta[žaidėjo_ėjimas] for skaičiai in kombinacijos):
            return True
    return False


# Funkcija kuri bus vygdoma jei nei vienas žaidėjas nelaimėjo.
def lygiosios(žaidėjo_vieta):
    if len(žaidėjo_vieta["X"]) + len(žaidėjo_vieta["O"]) == 9:
        return True
    return False


def žaidimo_ciklas(žaidėjo_ėjimas):
    vieta = [" " for vieta in range(9)]
    žaidėjo_vieta = {"X": [], "O": []}
    while True:
        lentelės_piešimas(vieta)
        try:
            įvestas_skaičius = int(input(f"{žaidėjo_ėjimas}, Pasirinkite skaičių nuo 1 iki 9: "))
        except ValueError:
            print("Netinkamas įvedimas, reikia įvesti skaičių!")
            continue
        if įvestas_skaičius < 1 or įvestas_skaičius > 9:
            print("Netinkamas skaičius!")
            continue
        if vieta[įvestas_skaičius - 1] != " ":
            print("Pasirinkta vieta užimta, pasirinkite kitą vietą:")
            continue
        vieta[įvestas_skaičius - 1] = žaidėjo_ėjimas
        žaidėjo_vieta[žaidėjo_ėjimas].append(įvestas_skaičius)
        if laimėjimo_patvirtinimas(žaidėjo_vieta, žaidėjo_ėjimas):
            lentelės_piešimas(vieta)
            print("Jūs laimėjote")
            return žaidėjo_ėjimas
        if lygiosios(žaidėjo_vieta):
            lentelės_piešimas(vieta)
            print("Lygiosios")
            return "="

        if žaidėjo_ėjimas == "X":
            žaidėjo_ėjimas = "O"
        else:
            žaidėjo_ėjimas = "X"


if __name__ == "__main__":
    žaidėjas1 = input("Įveskite pirmo žaidėjo vardą: ")
    žaidėjas2 = input("Įveskite antro žaidėjo vardą: ")
    žaidėjo_ėjimas = žaidėjas1
    žaidėjo_pasirinkimas = {"X": "", "O": ""}
    galimas_pasirinkimas = ["X", "O"]
    taškai = {žaidėjas1: 0, žaidėjas2: 0}
    rezultatai(taškai)

    while True:
        print(žaidėjo_ėjimas, "Pasirinkite savo simbolį (X arba O): ", "\n")
        print("Spauskite 1 jei norite pasirinkti X: ")
        print("Spauskite 2 jei norite pasirinkti O: ")
        print("Spauskite 0 jei norite IŠEITI:")
        try:
            pasirinkimas = int(input())
        except ValueError:
            print("Reikia įvesti skaičių")
            continue
        if pasirinkimas < 0 or pasirinkimas > 3:
            print("Reikia pasirinkti skaičių: 1, 2 arba 0: ")
            continue
        if pasirinkimas == 1:
            žaidėjo_pasirinkimas["X"] = žaidėjo_ėjimas
            if žaidėjo_ėjimas == žaidėjas1:
                žaidėjo_pasirinkimas["O"] = žaidėjas2
            else:
                žaidėjo_pasirinkimas["O"] = žaidėjas1
        elif pasirinkimas == 2:
            žaidėjo_pasirinkimas["O"] = žaidėjo_ėjimas
            if žaidėjo_ėjimas == žaidėjas1:
                žaidėjo_pasirinkimas["X"] = žaidėjas2
            else:
                žaidėjo_pasirinkimas["X"] = žaidėjas1
        elif pasirinkimas == 0:
            print("Žaidimas baigtas")
            rezultatai(taškai)
            break

        laimėtojas = žaidimo_ciklas(galimas_pasirinkimas[pasirinkimas - 1])

        if laimėtojas != "=":
            žaidėjas_laimėjo = žaidėjo_pasirinkimas[laimėtojas]
            taškai[žaidėjas_laimėjo] = taškai[žaidėjas_laimėjo] + 1

            rezultatai(taškai)
        if žaidėjo_ėjimas == žaidėjas1:
            žaidėjo_ėjimas = žaidėjas2
        else:
            žaidėjo_ėjimas = žaidėjas1
