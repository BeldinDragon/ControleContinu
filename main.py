from tkinter import *

tk = Tk()
tk.title("Contrôle Continu")
canv=Canvas(tk,width=750,height=200,background="#DCDCDC")
canv.pack(fill="both", expand=True)

Label(tk, text="Indique chacune de tes moyennes,").place(x=10,y=10)
Label(tk, text="ou rien si tu n'en a pas.").place(x=10,y=30)
Label(tk, text="Attention: utiliser \".\" au lieu des virgules").place(x=10,y=50)
Label(tk, text="Première").place(x=400,y=10)
Label(tk, text="Terminale").place(x=600,y=10)

# Coef 8
Label(tk, text="Spécialité").place(x=275,y=50)
PreSpecialite = [Entry(tk), Entry(tk), Entry(tk)]
PreSpecialite[0].place(x=350,y=50,width=50)
PreSpecialite[1].place(x=400,y=50,width=50)
PreSpecialite[2].place(x=450,y=50,width=50)

# Coef 3 + 3
Label(tk, text="Histoire-Géo").place(x=275,y=70)
PreHG = [Entry(tk), Entry(tk), Entry(tk)]
PreHG[0].place(x=350,y=70,width=50)
PreHG[1].place(x=400,y=70,width=50)
PreHG[2].place(x=450,y=70,width=50)
TerHG = [Entry(tk), Entry(tk), Entry(tk)]
TerHG[0].place(x=550,y=70,width=50)
TerHG[1].place(x=600,y=70,width=50)
TerHG[2].place(x=650,y=70,width=50)

# Coef 3 + 3
Label(tk, text="Anglais").place(x=275,y=90)
PreLVA = [Entry(tk), Entry(tk), Entry(tk)]
PreLVA[0].place(x=350,y=90,width=50)
PreLVA[1].place(x=400,y=90,width=50)
PreLVA[2].place(x=450,y=90,width=50)
TerLVA = [Entry(tk), Entry(tk), Entry(tk)]
TerLVA[0].place(x=550,y=90,width=50)
TerLVA[1].place(x=600,y=90,width=50)
TerLVA[2].place(x=650,y=90,width=50)

# Coef 3 + 3
Label(tk, text="Espagnol/All.").place(x=275,y=110)
PreLVB = [Entry(tk), Entry(tk), Entry(tk)]
PreLVB[0].place(x=350,y=110,width=50)
PreLVB[1].place(x=400,y=110,width=50)
PreLVB[2].place(x=450,y=110,width=50)
TerLVB = [Entry(tk), Entry(tk), Entry(tk)]
TerLVB[0].place(x=550,y=110,width=50)
TerLVB[1].place(x=600,y=110,width=50)
TerLVB[2].place(x=650,y=110,width=50)

# Coef 3 + 3
Label(tk, text="Ens. Scientif.").place(x=275,y=130)
PreES = [Entry(tk), Entry(tk), Entry(tk)]
PreES[0].place(x=350,y=130,width=50)
PreES[1].place(x=400,y=130,width=50)
PreES[2].place(x=450,y=130,width=50)
TerES = [Entry(tk), Entry(tk), Entry(tk)]
TerES[0].place(x=550,y=130,width=50)
TerES[1].place(x=600,y=130,width=50)
TerES[2].place(x=650,y=130,width=50)

# Coef 1 + 1
Label(tk, text="EMC").place(x=275,y=150)
PreEMC = [Entry(tk), Entry(tk), Entry(tk)]
PreEMC[0].place(x=350,y=150,width=50)
PreEMC[1].place(x=400,y=150,width=50)
PreEMC[2].place(x=450,y=150,width=50)
TerEMC = [Entry(tk), Entry(tk), Entry(tk)]
TerEMC[0].place(x=550,y=150,width=50)
TerEMC[1].place(x=600,y=150,width=50)
TerEMC[2].place(x=650,y=150,width=50)

# Coef 6
Label(tk, text="Sport").place(x=275,y=170)
TerEPS = [Entry(tk), Entry(tk), Entry(tk)]
TerEPS[0].place(x=550,y=170,width=50)
TerEPS[1].place(x=600,y=170,width=50)
TerEPS[2].place(x=650,y=170,width=50)

def moyenne(liste):
    if liste==[]:
        return -1
    result = 0
    for i in range(len(liste)):
        result += liste[i]
    return result/len(liste)
        
def calculer():
    # Récupération des valeurs en str
    specialite = [(PreSpecialite[0].get().strip()), (PreSpecialite[1].get().strip()), (PreSpecialite[2].get().strip())]
    Phg = [(PreHG[0].get().strip()), (PreHG[1].get().strip()), (PreHG[2].get().strip())]
    Plva = [(PreLVA[0].get().strip()), (PreLVA[1].get().strip()), (PreLVA[2].get().strip())]
    Plvb = [(PreLVB[0].get().strip()), (PreLVB[1].get().strip()), (PreLVB[2].get().strip())]
    Pes = [(PreES[0].get().strip()), (PreES[1].get().strip()), (PreES[2].get().strip())]
    Pemc = [(PreEMC[0].get().strip()), (PreEMC[1].get().strip()), (PreEMC[2].get().strip())]
    eps = [(TerEPS[0].get().strip()), (TerEPS[1].get().strip()), (TerEPS[2].get().strip())]
    Thg = [(TerHG[0].get().strip()), (TerHG[1].get().strip()), (TerHG[2].get().strip())]
    Tlva = [(TerLVA[0].get().strip()), (TerLVA[1].get().strip()), (TerLVA[2].get().strip())]
    Tlvb = [(TerLVB[0].get().strip()), (TerLVB[1].get().strip()), (TerLVB[2].get().strip())]
    Tes = [(TerES[0].get().strip()), (TerES[1].get().strip()), (TerES[2].get().strip())]
    Temc = [(TerEMC[0].get().strip()), (TerEMC[1].get().strip()), (TerEMC[2].get().strip())]

    # Elimination des entrées vides et calcul de la moyenne
    specialite = moyenne([float(i) for i in specialite if i!=""])
    Phg = moyenne([float(i) for i in Phg if i!=""])
    Plva = moyenne([float(i) for i in Plva if i!=""])
    Plvb = moyenne([float(i) for i in Plvb if i!=""])
    Pes = moyenne([float(i) for i in Pes if i!=""])
    Pemc = moyenne([float(i) for i in Pemc if i!=""])
    Thg = moyenne([float(i) for i in Thg if i!=""])
    Tlva = moyenne([float(i) for i in Tlva if i!=""])
    Tlvb = moyenne([float(i) for i in Tlvb if i!=""])
    Tes = moyenne([float(i) for i in Tes if i!=""])
    Temc = moyenne([float(i) for i in Temc if i!=""])
    eps = moyenne([float(i) for i in eps if i!=""])

    # Calcul du Controle Continu
    listeMatieres = [specialite]*8+[Phg]*3+[Thg]*3+[Plva]*3+[Tlva]*3+[Plvb]*3+[Tlvb]*3+[Pes]*3+[Tes]*3+[Pemc]*1+[Temc]*1+[eps]*6
    while -1 in listeMatieres:
        listeMatieres.remove(-1)
    controlecontinu = round(moyenne(listeMatieres), 2)

    Label(tk, text="Note au Controle Continu:").place(x=100, y=100)
    Label(tk, text=controlecontinu, fg="green").place(x=100, y=150)

calculer = Button(tk, text="Calculer", command=calculer)
calculer.place(x=25, y=125)
tk.mainloop()
