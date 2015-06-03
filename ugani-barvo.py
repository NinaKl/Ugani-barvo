from tkinter import *

class Besede():
    def __init__(self, master):

#velikost 'platna'
        self.canvas = Canvas(master, width=300, height=300)
        self.canvas.grid(row=2, column=0)
        
##začetni meni : vnesi ime igralca
        





##navodila, tipka start + številka levela (ponavlja se po vsakem levelu)






## gumb escape prekine in ugasne igro







## ********* IGRA ***********


		
#self.beseda = beseda, ki jo bomo prikazali - iz datoteke dobimo seznam
#besed, ki jih bomo prikazovali.
        Label(master, text="self.beseda", font=("Helvetica", 32)).grid(row=2)




        
# Polje v katerega pišemo + spremenljivka, ki hrani njegovo vrednost.
        self.vnesi = StringVar()
        polje_vnesi = Entry(master, textvariable=self.vnesi)
        polje_vnesi.grid(row=3)







# preverimo če je rešitev pravilna









#štetje točk


















##high-score - datoteka ki hrani podatke 10ih najboljših iger

        




root = Tk()
aplikacija = Besede(root)
root.mainloop()

