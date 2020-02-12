import tkinter #okienkowe aplikacje
def sumuj():
    a = entry_a.get()
    b=entry_b.get()
    suma=int(a)+int(b)
    wynik.configure(text=suma)


root = tkinter.Tk()

label_a=tkinter.Label(master=root, text="a")
entry_a = tkinter.Entry(master=root)

label_b=tkinter.Label(master=root, text="b")
entry_b = tkinter.Entry(master=root)

submit = tkinter.Button(master=root, text="Policz", command=sumuj)
wynik=tkinter.Label(master=root, text="-")

label_a.grid(row=1, column=1)
entry_a.grid(row=1, column=2)
label_b.grid(row=2, column=1)
entry_b.grid(row=2, column=2)
submit.grid(row=3, column=1)
wynik.grid(row=4, column=2)

root.mainloop()
print("Po petli")







