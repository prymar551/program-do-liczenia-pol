import funkcje
import time


mistake = "zadna z liczb nie moze byc ujemna lub rowna 0 sprobuj ponownie"

print("PROGRAM DO LICZENIA POL")
for i in range(999):
    mistake = "zadna z liczb nie moze byc ujemna lub rowna 0 sprobuj ponownie"

    print("wybierz")
    print()
    print("1 - pole kwadratu")
    print("2 - pole prostokata")
    print("3 - pole trojkata")
    print("4 - pole trapezu")
    print("5 - tworca")
    print("6 - wyjdz")
    choice = int(input("wybor: "))
    if (choice == 1):
        funkcje.pole_kwadratu()
    elif (choice == 2):
        funkcje.pole_prostokata()
    elif (choice == 3):
        funkcje.pole_trojkata()
    elif (choice == 4):
        funkcje.pole_trapezu()
    elif (choice == 5):
        print("fajnie ze to cie ciekawi :) Piotr Rymarczyk")
        time.sleep(3)
    elif (choice == 6):
        print("good bye:)")
        break
    else:
        for i in range(999):
            print("wybrany numer jest nie prawidlowy sprobuj pnownie")
            time.sleep(3)
            break
