import random
import tkinter as tk
from tkinter import messagebox


def generer_cle():
    caracteres = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[{]}|;:',<.>/?")
    melange = caracteres[:]
    random.shuffle(melange)
    cle = dict(zip(caracteres, melange))
    cle_inverse = {v: k for k, v in cle.items()}
    cle_str = ",".join([f"{k}:{v}" for k, v in cle.items()])
    return cle, cle_inverse, cle_str


def analyser_cle(cle_str):
    try:
        paires = cle_str.split(",")
        cle_inverse = {}
        for paire in paires:
            if ":" in paire and len(paire.split(":")) == 2:
                k, v = paire.split(":", 1)
                if len(k) == 1 and len(v) == 1:
                    cle_inverse[v] = k
                else:
                    print(f"Avertissement : Paire ignorée car invalide : {paire}")
            else:
                print(f"Avertissement : Paire mal formée : {paire}")
        return cle_inverse
    except Exception as e:
        raise ValueError(f"Format de clé invalide : {e}")


def transformer_texte(texte):
    resultat = ""
    majuscule_suivante = False
    for char in texte:
        if char == " ":
            majuscule_suivante = True
        else:
            if majuscule_suivante and char.isalpha():
                resultat += char.upper()
                majuscule_suivante = False
            else:
                resultat += char
    return resultat


def crypter(texte, cle):
    texte_crypte = ""
    for char in texte:
        if char in cle:
            texte_crypte += cle[char]
        else:
            texte_crypte += char
    return texte_crypte


def decrypter(texte, cle_inverse):
    texte_decrypte = ""
    for char in texte:
        if char in cle_inverse:
            texte_decrypte += cle_inverse[char]
        else:
            texte_decrypte += char
    return texte_decrypte


def afficher_message_crypte():
    def crypter_messages():
        try:
            nombre_messages = int(champ_nombre.get())
            textes = []
            for i in range(nombre_messages):
                texte = champs_textes[i].get()
                textes.append(transformer_texte(texte))

            cle, cle_inverse, cle_str = generer_cle()
            textes_crypte = [crypter(texte, cle) for texte in textes]

            resultat = ""
            for i, (texte_transforme, texte_crypte) in enumerate(zip(textes, textes_crypte), 1):
                resultat += f"Message {i} transformé : {texte_transforme}\nMessage {i} crypté : {texte_crypte}\n\n"

            resultat += f"Clé de décryptage : {cle_str}"
            messagebox.showinfo("Résultat", resultat)
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur est survenue : {e}")

    def generer_champs_messages():
        for widget in cadre_messages.winfo_children():
            widget.destroy()
        try:
            nombre_messages = int(champ_nombre.get())
            global champs_textes
            champs_textes = []
            for i in range(nombre_messages):
                tk.Label(cadre_messages, text=f"Entrez le message {i + 1} à crypter :").pack(pady=5)
                champ = tk.Entry(cadre_messages, width=50)
                champ.pack(pady=5)
                champs_textes.append(champ)
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer un nombre valide.")

    fenetre_crypter = tk.Toplevel()
    fenetre_crypter.title("Crypter des messages")

    tk.Label(fenetre_crypter, text="Entrez le nombre de messages à crypter :").pack(pady=5)
    champ_nombre = tk.Entry(fenetre_crypter, width=10)
    champ_nombre.pack(pady=5)
    tk.Button(fenetre_crypter, text="Valider", command=generer_champs_messages).pack(pady=10)

    cadre_messages = tk.Frame(fenetre_crypter)
    cadre_messages.pack(pady=10)

    tk.Button(fenetre_crypter, text="Crypter", command=crypter_messages).pack(pady=10)


def afficher_message_decrypte():
    def decrypter_messages():
        try:
            nombre_messages = int(champ_nombre.get())
            textes = [champs_textes[i].get() for i in range(nombre_messages)]
            cle_str = champ_cle.get()
            cle_inverse = analyser_cle(cle_str)

            textes_decrypte = [decrypter(texte, cle_inverse) for texte in textes]

            resultat = ""
            for i, texte_decrypte in enumerate(textes_decrypte, 1):
                resultat += f"Message {i} décrypté : {texte_decrypte}\n\n"

            messagebox.showinfo("Résultat", resultat)
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur est survenue : {e}")

    def generer_champs_messages():
        for widget in cadre_messages.winfo_children():
            widget.destroy()
        try:
            nombre_messages = int(champ_nombre.get())
            global champs_textes
            champs_textes = []
            for i in range(nombre_messages):
                tk.Label(cadre_messages, text=f"Entrez le message {i + 1} crypté :").pack(pady=5)
                champ = tk.Entry(cadre_messages, width=50)
                champ.pack(pady=5)
                champs_textes.append(champ)
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer un nombre valide.")

    fenetre_decrypter = tk.Toplevel()
    fenetre_decrypter.title("Décrypter des messages")

    tk.Label(fenetre_decrypter, text="Entrez le nombre de messages à décrypter :").pack(pady=5)
    champ_nombre = tk.Entry(fenetre_decrypter, width=10)
    champ_nombre.pack(pady=5)
    tk.Button(fenetre_decrypter, text="Valider", command=generer_champs_messages).pack(pady=10)

    cadre_messages = tk.Frame(fenetre_decrypter)
    cadre_messages.pack(pady=10)

    tk.Label(fenetre_decrypter, text="Entrez la clé de décryptage :").pack(pady=5)
    champ_cle = tk.Entry(fenetre_decrypter, width=50)
    champ_cle.pack(pady=5)

    tk.Button(fenetre_decrypter, text="Décrypter", command=decrypter_messages).pack(pady=10)


def principal():
    racine = tk.Tk()
    racine.title("Cryptage et Décryptage")

    tk.Label(racine, text="Bienvenue dans le système de cryptage !", font=("Arial", 14)).pack(pady=10)

    tk.Button(racine, text="Crypter des messages", command=afficher_message_crypte, width=30).pack(pady=10)
    tk.Button(racine, text="Décrypter des messages", command=afficher_message_decrypte, width=30).pack(pady=10)

    racine.mainloop()


if __name__ == "__main__":
    principal()
