class Adressbuch:
    def __init__(self):
        self.Adressliste = []

class Kontakt:
    def __init__(self, Vorname, Nachname, Telefonnummer, Mail):
        self.Vorname = Vorname
        self.Nachname = Nachname
        self.Telefonnummer = Telefonnummer
        self.Mail = Mail

    def __str__(self):
        return self.Vorname + "," + self.Nachname + "," + self.Telefonnummer + ", " + self.Mail


# Kontakte hinzufügen = a / Kontakte suchen = s / Programm beenden = b
if __name__ == '__main__':
    adressbuch = Adressbuch()
    while (1==1):
        Anfang = input("Was soll ausgeführt werden?\n" + \
                       "Kontakte hinzufügen = a \n " + \
                       "Kontakte suchen = s \n " + \
                       "Programm beenden = b \n ")
        print(Anfang)
        if Anfang == "a":
            Vorname = input("Vorname:")
            Nachname = input("Nachname:")
            Telefonnummer = input("Telefonnummer:")
            Mail = input("Mail:")
            kontakt = Kontakt(Vorname,Nachname,Telefonnummer,Mail)
            adressbuch.Adressliste.append(kontakt)
            print(str(kontakt))
            print(len(adressbuch.Adressliste))


        elif Anfang == "s":
            print()
        elif Anfang == "b":
            exit(0)



