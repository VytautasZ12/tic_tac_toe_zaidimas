# Lentelės vaizdavimas.
def lentelės_piešimas(vieta):
    print("      {} | {} | {} ".format(vieta[6], vieta[7], vieta[8]))
    print("\t ___|___|___")
    print("      {} | {} | {} ".format(vieta[3], vieta[4], vieta[5]))
    print("\t ___|___|___")
    print("      {} | {} | {} ".format(vieta[0], vieta[1], vieta[2]))
    print("\t    |   |   ")

# Rezultatų lentelė, kurioje bus rodomi žaidėjų vardai ir taškai po kiekvieno žaidimo.
def rezultatai(taškai):
    print("\t-------------------")
    print("\t Rezultatų lentelė")
    print("\t-------------------")

    žaidėjų_sąrašas = list(taškai.keys())

    print("\t ", žaidėjų_sąrašas[0], "\t", taškai[žaidėjų_sąrašas[0]])
    print("\t ", žaidėjų_sąrašas[1], "\t", taškai[žaidėjų_sąrašas[1]])
    print("\t-------------------\n")
# Gilimos laimėjimo kombinacijos, horizontaliai, vertikaliai, įstrižai.
def laimėjimo_patvirtinimas(žaidėjo_vieta, žaidėjo_ėjimas):
    laimėjimo_kombinacijos = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for kombinacijos in laimėjimo_kombinacijos:
        if all(skaičiai in žaidėjo_vieta[žaidėjo_ėjimas] for skaičiai in kombinacijos):
            return True
    return False



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
