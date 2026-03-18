ukoly = []

def hlavni_menu():
    while True:
        print("Správce úkolů - Hlavní menu")
        print("1. Přidat nový úkol")
        print("2. Zobrazit všechny úkoly")
        print("3. Odstranit úkol")
        print("4. Konec programu")
        volba = input("Vyberte možnost (1-4): ")

        if volba == "1":
            pridat_ukol()
        elif volba == "2":
            zobrazit_ukoly()
        elif volba == "3":
            odstranit_ukol()
        elif volba == "4":
            print("Konec programu.")
            break
        else:
            print("Neplatná volba. Zkuste to znovu.")

def pridat_ukol():
    while True:
        nazev = input("Zadejte název úkolu: ")
        if nazev == "":
            print("Název úkolu nemůže být prázdný.")
        else:
            break
    while True:
        popis = input("Zadejte popis úkolu: ")
        if popis == "":
            print("Popis úkolu nemůže být prázdný.")
        else:
            break
    ukoly.append({"nazev": nazev, "popis": popis})
    print(f"Úkol '{nazev}' byl přidán.")

def zobrazit_ukoly():
    print("Seznam úkolů:")
    if not ukoly:
        print("Žádné úkoly.")
    else:
        for i, ukol in enumerate(ukoly, 1):
            print(f"{i}. {ukol['nazev']} - {ukol['popis']}")

def odstranit_ukol():
    zobrazit_ukoly()
    if not ukoly:
        return
    while True:
        cislo = input("Zadejte číslo úkolu, který chcete odstranit: ")
        if cislo.isdigit() and 1 <= int(cislo) <= len(ukoly):
            cislo = int(cislo) - 1
            print(f"Úkol '{ukoly[cislo]['nazev']}' byl odstraněn.")
            ukoly.pop(cislo)
            break
        else:
            print("Neplatné číslo úkolu.")

hlavni_menu()
