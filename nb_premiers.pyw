from tkinter import *
from tkinter import messagebox

def Verifier():
    try:
        assert nombreSaisi.get() != ""
        int(nombreSaisi.get())
    except AssertionError: messagebox.showerror("Champ vide", "Veuillez saisir un nombre entier dans la barre de saisie")
    except ValueError: messagebox.showerror("Saisie erronée", "Veuillez saisir un nombre entier dans la barre de saisie")
    else:

        diviseur = 2        
        while 1:
            
            if int(nombreSaisi.get()) % diviseur == 0 and int(nombreSaisi.get()) != diviseur:
                messagebox.showinfo("Verification effectuée", f"Le nombre {int(nombreSaisi.get())} n'est pas premier, il est divisible par {diviseur}")
                break
            elif int(nombreSaisi.get()) == 1:
                messagebox.showinfo("Verification effectuée", "1 n'est pas premier")
                break
            elif int(nombreSaisi.get()) < diviseur:
                messagebox.showinfo("Verification effectuée", f"Le nombre {int(nombreSaisi.get())} est premier")
                break
            elif int(nombreSaisi.get()) % diviseur != 0 or int(nombreSaisi.get()) == diviseur: diviseur += 1      


def Verifier_bind(j): Verifier()
    
fenetre = Tk()
fenetre.title('Nombre premier ?')
fenetre.geometry('275x50')

nombreSaisi = StringVar()
nombreSaisi.set("Saisir un nombre premier")
Entry(textvariable=nombreSaisi, width=30).pack()

Button(text="Verifier", command=Verifier).pack()

fenetre.bind('<Return>', Verifier_bind)
fenetre.mainloop()
