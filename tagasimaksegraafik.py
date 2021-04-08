def tagasimaksegraafik(algsumma, i, koguperiood):
    algsumma = float(algsumma)
    i = float(i)
    koguperiood = float(koguperiood)
    fail = open("graafik.txt", "w+", encoding = "utf-8")
    intress = (i / 12) * 0.01
    per1 = algsumma * ((1 + intress) ** koguperiood)
    per2 = per1-algsumma
    osamakse = algsumma * (intress / (1 - pow(1 + intress, (-1) * koguperiood)))
    laenujääk = algsumma
    kuu = 1
    intresskokku = 0
    fail.write("Kuu" + " " + "Laenujääk" + " " + "Makse" + " Intressiosa\n" )
    while laenujääk > 0 and kuu <= koguperiood:
        intressiosa = laenujääk * intress
        intresskokku += intressiosa
        makse = osamakse - intressiosa
        laenujääk -= makse
        
        fail.write(str(kuu) + " " + str(round(laenujääk,2)) + " "+ str(round(makse,2)) + " " + str(round(intressiosa,2)) + "\n")
        kuu += 1
        
    fail.write("Intress kokku: " + str(round(intresskokku,2)) + " eurot")