x = input("Zadaj svoje meno: ")

while True:
    moznost = int(input("Zadaj možnosť: 1.10x vypíše meno alebo 2.vypne program"))
    if moznost == 1:
        print(x * 10)
    elif moznost == 2:
        print("Koniec programu")
        break