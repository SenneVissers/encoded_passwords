import base64

wat = input("Wat wil je doen? Toevoegen(t) of opvragen(o): ")

if wat == "t":
    acc = input("Welk account wil je toevoegen: ")
    ww = input("Welk wachtwoord hoort hierbij: ")
    ww_bytes = ww.encode("ascii")

    with open('passwords.txt', 'a', encoding='UTF-8') as file:
        file.write(acc + ";" + str(base64.b64encode(ww_bytes)) + "\n")

elif wat == "o":
    account = []
    wachtwoord = []

    with open("passwords.txt") as file:
        line = file.readline()
        while line:
            if line != "\n":
                record = line.rstrip().split(";")
                account.append(record[0])
                wachtwoord.append(record[1])
            line = file.readline()

    zoek = input("Waarvan zoek je het wachtwoord: ")
    index = -1

    if zoek.lower() in account:
        index = account.index(zoek.lower())
        ww = wachtwoord[index].replace("'", "")
        ww_final = ww.replace(ww[0], "", 1)
        ww_base64_bytes = ww_final.encode("ascii")
        ww_bytes = base64.b64decode(ww_base64_bytes)

        print("Het wachtwoord voor uw", zoek, "account is", ww_bytes.decode("ascii"))
    else:
        print("Het wachtwoord van uw", zoek, "account staat niet in het bestand wachtwoorden.txt")

input("Press enter: ")
