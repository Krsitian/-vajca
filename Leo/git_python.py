meno = input("Zadaj svoje meno: ")

while True:
    print("\n===== MENU =====")
    print("1.meno print")
    print("2.Zmenit  meno")
    print("3. Koniec")

    volba = input("Vyber možnosť: ")

    if volba == "1":
        for i in range(10):
            print(meno)

    elif volba == "2":
        meno = input("Zadaj nove meno: ")
        print("Meno bolo zmenene")

    elif volba == "3":
        print("KONEC THE END")
        break

    else:
        print("COSKAJ WRONG")
