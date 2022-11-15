import tkinter as tk
from tkinter import *
import random
import time

noir = "black"
blanc = "#f4f4f4"
 

class Application(tk.Tk):
    def __init__(self, largeur=720, hauteur=630):
        tk.Tk.__init__(self)

        self.resizable(False, False)
        self.title("Générateur de calcul mental")
        self.largeur = largeur
        self.hauteur = hauteur

        self.geometry("{}x{}".format(str(largeur),str(hauteur)))
        
        pre_number = random.randint(1,500)
        self.pre_number = pre_number

        post_number = random.randint(1,500)
        self.post_number = post_number

        operateur = ["+", "-", "*"]
        self.operateur = operateur

        self.operateur_choice = random.choice(self.operateur)
        operateur_choice = self.operateur_choice

        self.WIN = 0

    def generate_operation(self):
        all_operation = str(self.pre_number) + self.operateur_choice + str(self.post_number)
        return all_operation

    def verif_operation(self):
        correction = eval(str(self.pre_number) + self.operateur_choice + str(self.post_number))
        return correction

    def menu(self):
        pass
        #self.Start_image = PhotoImage(file='start.png')
        #self.Button_start = tk.Button(self.root, image=self.Start_image, borderwidth=0, bg=blanc, activebackground=blanc, command=lambda:[root.affichage()]).place(x=205, y=300)


        
    def win_condition(self):
        if self.getReponseUser() == str(self.verif_operation()) and not self.LOSS:
            self.correction = tk.Label(self, text="Bravo, bonne réponse", fg="green", bg=blanc, font=("Franklin Gothic Demi", 18)).place(x=250, y=364)
        else: 
            self.correction = tk.Label(self, text=f"Dommage, voici la correction : {self.verif_operation()}", fg="green", bg=blanc, font=("Franklin Gothic Demi", 18)).place(x=170, y=364)
            self.LOSS = 1



    def getReponseUser(self):
        self.input_value = self.my_input.get()
        return self.input_value


    def affichage(self):

        self.background = PhotoImage(file = "apercu3.png")
        tk.Label(self, image = self.background).place(x = -2, y = -1)

        self.my_label = Label(self, text="Veuillez résoudre l'opération", fg="green", bg=blanc, font=("Franklin Gothic Demi", 18)).place(x=205, y=205)
        
        self.generate = Label(self, text=self.generate_operation(), font=("Franklin Gothic Demi", 18), fg=noir).place(x = 300, y = 250)


        self.my_input = tk.Entry(self, width= 27, font=("Franklin Gothic Demi", 18))
        self.my_input.place(x=162, y=310, height = 40)
        #self.correction = tk.Label(self.root, text="Voici la correction:", fg="green", bg=blanc, font=("Franklin Gothic Demi", 18)).place(x=300, y=400)

        self.Start_image = PhotoImage(file='start.png')
        self.Button_start = tk.Button(self, image=self.Start_image, borderwidth=0, bg=blanc, activebackground='WHITE', command=lambda:[self.getReponseUser(), self.win_condition()]).place(x=210, y=420)


"""class Compteur(): 
    def __init__(self, compteur_start = 10, compteur_stop = 0):

        self.compteur_start = compteur_start
        self.compteur_stop = compteur_stop

    def compteur_avancement(self):
        while self.compteur_start >= self.compteur_stop:

            self.affichage['text'] = str(self.compteur_start)
            self.compteur += 1
            root.affichage.update_idletasks()
            time.sleep(1)
            return self """
            


class User(): 
    def __init__(self):
        pass

        

if __name__ == "__main__":

    root = Application()
    root.affichage()
    root.mainloop()

    print(root.verif_operation())
