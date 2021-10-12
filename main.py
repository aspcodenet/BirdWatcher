from birdwatcher import Birdwatcher

birdwatcher = Birdwatcher()

while True:
    print("1. Registrera att du sett en till fågel idag")
    print("2. Skriv ut statistik från idag")
    print("3. Skriv ut hur många du sett senaste 7 dagarna")
    print("4. Påbörja ny dag")
    print("5. Check if day with no birds")
    print("0. Avsluta")
    sel = input("Ange vad du vill göra:")

    if sel == "1":
        birdwatcher.incrementTodaysCount()

    if sel == "2":
        count = birdwatcher.getCountToday()
        print(f"Idag har du sett {count} fåglar")

    if sel == "3":
        count = birdwatcher.getCountThisWeek()
        print(f"Denna vecka har du sett {count} fåglar")

    if sel == "4":
        birdwatcher.setNewDay()

    if sel == "5":
        exists = birdwatcher.hasDayWithoutBirds()
        if exists:
            print("Du har sett 0 fåglar nån dag")
        else:
            print("Du har sett fåglar alla dagar")



    if sel == "0":
        break
