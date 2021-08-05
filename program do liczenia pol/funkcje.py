import time 

mistake = "zadna z liczb nie moze byc ujemna lub rowna 0 sprobuj ponownie" 


def pole_kwadratu():
    for i in range(999):
        a = float(input("podaj dlugosc a: "))

        if (a > 0):
            print("pole kwadratu wynosi: " + str(a ** 2))
            print()
            time.sleep(3)
            break
        elif (a <= 0):
            print(mistake)
            continue


def pole_prostokata():
    for i in range(999):
        a = float(input("podaj dlugosc a: "))
        if (a <= 0):
            print(mistake)
            continue
        elif (a > 0):
            b = float(input("podaj dlugosc b: "))
        if (b <= 0):
            print(mistake)
            continue
        elif (b > 0):
            print("pole prostokata wynosi: " + str(a * b))
            print()
            time.sleep(3)
            break



def pole_trojkata():
    for i in range(999):
        a = float(input("podaj dlugosc a: "))
        if (a <= 0):
            print(mistake)
            continue
        elif (a > 0):
            h = float(input("podaj dlugosc h: "))
        if (h <= 0):
            print(mistake)
            continue
        elif (h > 0):
            print("pole trojkata wynosi: " + str(a * h / 2))
            print()
            time.sleep(3)
            break


def pole_trapezu():
    for i in range(999):
        a = float(input("podaj dlugosc a: "))
        if (a <= 0):
            print(mistake)
            continue
        elif (a > 0):
            b = float(input("podaj dlugosc b: "))
        if (b <= 0):
            print("zadna z liczb nie moze byc ujemna lub rowna 0")
            continue
        elif (b > 0):
            h = float(input("podaj dlugosc h: "))
        if (h <= 0):
            print("zadna z liczb nie moze byc ujemna lub rowna 0")
            continue
        elif (h > 0):
            print("pole trapezu wynosi: " + str((a + b) * h / 2))
            print()
            time.sleep(3)
            break
