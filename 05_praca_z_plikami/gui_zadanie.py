"""
utworz proste GUI przy pomocy ktorego policzymy koszt paliwa na dystansie

3 pola: dystans w km, cena za 1 L, spalanie na 100 km
1 przycisk
labelka na wynik
"""

import tkinter #okienkowe aplikacje
def oblicz():
    dystans  = entry_dystans.get()
    cena     = entry_cena.get()
    spalanie = entry_spalanie.get()
    koszt = round(float(dystans)/100 * float(cena) * float(spalanie),3)
    wynik.configure(text=koszt)


root = tkinter.Tk()

label_dystans=tkinter.Label(master=root, text="Dystans w km")
entry_dystans = tkinter.Entry(master=root)

label_cena=tkinter.Label(master=root, text="Cena za 1L")
entry_cena = tkinter.Entry(master=root)

label_spalanie=tkinter.Label(master=root, text="Spalanie na 100 km")
entry_spalanie = tkinter.Entry(master=root)

submit = tkinter.Button(master=root, text="Policz", command=oblicz)
wynik=tkinter.Label(master=root, text="-")

label_cena.grid(row=1, column=1)
entry_cena.grid(row=1, column=2)
label_dystans.grid(row=2, column=1)
entry_dystans.grid(row=2, column=2)
label_spalanie.grid(row=3, column=1)
entry_spalanie.grid(row=3, column=2)

submit.grid(row=4, column=1)
wynik.grid(row=5, column=1)

root.mainloop()
print("Po petli")