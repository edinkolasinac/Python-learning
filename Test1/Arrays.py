dan = input("Dan:  ")
mesec = input("Mesec:  ")
godina = input("Godina:  ")

dan = int(dan)
mesec = int(mesec)
godina = int(godina)

if dan < 1 or dan > 31 or mesec < 1 or mesec > 12 or godina < 0 or godina > 2020:
    print("Greska")
else:
    if mesec == 1:
        me = "jan"
    elif mesec == 2:
        me = "feb"
    elif mesec == 3:
        me = "mart"
    elif mesec == 4:
        me = "apr"

    elif mesec == 5:
        me = "maj"

    elif mesec == 6:
        me = "jun"
    elif mesec == 7:
        me = "jul"
    elif mesec == 8:
        me = "avg"
    elif mesec == 9:
        me = "sep"
    elif mesec == 10:
        me = "oktb"
    elif mesec == 11:
        me = "novm"
    elif mesec == 12:
        me = "dec"

    print(dan, ".", me, ".", godina, ".", sep="")
