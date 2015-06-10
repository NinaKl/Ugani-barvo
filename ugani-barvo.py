
from tkinter import *
import random
import os

class Besede():
    def __init__(self, master):

#velikost 'platna'
        
        self.canvas = Canvas(master, width=300, height=300)
        self.canvas.grid(row=2, column=0)

##navodila + številka levela 
## gumb escape prekine in ugasne igro
        self.besede = []
        with open("Level_1.txt") as f:
            for vrstica in f:
                self.besede.append(vrstica)
		
#self.beseda = beseda, ki jo bomo prikazali - iz datoteke dobimo seznam
#besed, ki jih bomo prikazovali.
        self.barve = ["red", "orange", "yellow", "green", "blue", "violet"]
        Label(master, text=self.besede, font=("Helvetica", 32)).grid(row=2)
        
# Polje v katerega pišemo + spremenljivka, ki hrani njegovo vrednost.
        self.vnesi = StringVar()
        polje_vnesi = Entry(master, textvariable=self.vnesi)
        polje_vnesi.grid(row=3)
        self.naslednja()


    def naslednja(self):
        self.barva = random.choice(self.barve)
        self.beseda = random.choice(self.besede)
        # izpisi besedo v dani barvi

    def ugibaj(self):
        if self.vnesi.get() == self.beseda:
            ...
        else:
            ...
        self.naslednja()   
                    


# igralec vpiše rešitev in preverimo če je pravilna
        if str(vartext.fg) == vnesi:
            rezultat += 1
        else: rezultat = rezultat

# ko igralec vpiše besedilo, se naša beseda zamenja




#štetje točk




##high-score - datoteka ki hrani podatke 10ih najboljših iger

        




root = Tk()
aplikacija = Besede(root)
root.mainloop()

