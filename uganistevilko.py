name = input("Zivjo, kako ti je ime? ")

print(name,"dobrodosel v racunalniskem kvizu.")

playing = input("Bi rad zacel igrati ta kviz? ")

if playing.lower() != "ja":
    quit()

print("Super! Pa zacnimo!:)")
score = 0

answer = input("Kako se imenuje glavno mesto Slovenije? ")
if answer == "ljubljana":
    print("Cestitke, tvoj odgovor je pravilen!")
    score += 2
else: 
    print("Odgovor je nazalost nepravilen.")

answer = input("V katerem mestu si se rodil? ")
if answer == "trbovlje":
    print("Cestitke, tvoj odgovor je pravilen!")
    score += 1
else: 
    print("Odgovor je nazalost nepravilen.")

answer = input("Iz koliko crk je sestavljeno ime Brigita? Odgovori z besedo, ne stevilko. ")
if answer.lower() == "sedem":
    print("Cestitke, tvoj odgovor je pravilen!")
    score += 1
else: 
    print("Odgovor je nazalost nepravilen.")

answer = input("Katera zival je tezja - slon ali morski kit? ")
if answer.lower() == "slon":
    print("Cestitke, tvoj odgovor je pravilen!")
    score += 1
else: 
    print("Odgovor je nazalost nepravilen.")

answer = input("Kaj je bolj slastno - torta ali zganci? ")
if answer.lower() == "torta":
    print("Cestitke, tvoj odgovor je pravilen!")
    score += 1
else: 
    print("Odgovor je nazalost nepravilen.")

answer = input("Koliko stranic ima trikotnik? ")
if answer.lower() == "tri":
    print("Cestitke, tvoj odgovor je pravilen!")
    score += 1
else: 
    print("Odgovor je nazalost nepravilen.")

print("Bravo! Pravilno si odgovoril na " + str(score) + " vprasanj.")

print(name, "super ti je slo! Hvala za sodelovanje? :)" )



