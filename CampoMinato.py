# TODO
#  -Creazione griglia
#  -Funzione click
#  -Funzione per mettere le mine e i numeri
#  -Funzione ricorsiva che scopre le celle
#  -Funzione click destro per la bandiera

# -Controllo vittoria
# -controllo sconfitta
# -timer
# -difficoltà
# -rigioca

import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
from random import randint

PrimaVolta = True
numbombe = 25
R, C = 12, 16
sec = 0
valoridiff = ["facile", "media", "difficile", "estrema"]
diff = "media"

def cambiadiff(evento):
    global diff, numbombe, R, C
    diff = combodiff.get()
    match(diff):
        case "facile":
            numbombe = 15
            R, C = 10, 14
        case "media":
            numbombe = 25
            R, C = 12, 16
        case "difficile":
            numbombe = 55
            R, C = 14, 18
        case "estrema":
            numbombe = 70
            R, C = 16, 20
        case _:
            numbombe = 25
            R, C = 12, 16
    
    ancora()

def crea():
    lista = []
    listanum = []
    for riga in range(R):
        temp = []
        tempnum = []
        for colonna in range(C):
            if (riga+colonna)%2 == 0:
                colore = "chartreuse2"
            else:
                colore = "chartreuse3"

            cella = tk.Button(frameGriglia, bg = colore, width = 4, height = 2)
            cella.bind("<Button-1>", clicksx)
            cella.bind("<Button-3>", clickdx)
            cella.grid(row = riga, column = colonna)

            temp.append(cella)
            tempnum.append("0")

        lista.append(temp)
        listanum.append(tempnum)

    return lista, listanum

def libera(riga, colonna):
    global numbombe
    for nriga in range(-1, 2):
        if nriga == -1 and riga == 0:
            continue
        elif nriga == 1 and riga == R-1:
            break

        for ncolonna in range(-1, 2):
            if nriga == 0 and ncolonna == 0:
                continue
            if ncolonna == -1 and colonna == 0:
                continue
            elif ncolonna == 1 and colonna == C-1:
                break
            
            if tabellanum[riga+nriga][colonna+ncolonna] == "0":
                tabellanum[riga+nriga].pop(colonna+ncolonna)
                tabellanum[riga+nriga].insert(colonna+ncolonna, " ")
                libera(riga+nriga, colonna+ncolonna)

            if (riga+nriga+colonna+ncolonna)%2 == 0:
                colore = "bisque"
            else:
                colore = "peachpuff2"

            if tabella[riga+nriga][colonna+ncolonna].cget("text") == "🚩":
                numbombe += 1
                bombe.config(text = f"🚩 {numbombe}")
            tabella[riga+nriga][colonna+ncolonna].config(text = tabellanum[riga+nriga][colonna+ncolonna], bg = colore, fg = "black")
    
    return

def timer():
    global sec, timerloop
    sec += 1
    orologio.config(text = f"🕙 {sec}")

    timerloop = window.after(1000, timer)

def generabombe(cella):
    x, y = -1, -1
    for riga in range(len(tabella)):
        for colonna in range(len(tabella[riga])):
            if tabella[riga][colonna] == cella:
                x, y = colonna, riga
                break
        if x != -1 and y != -1:
            break
                    
    for i in range(numbombe):
        while 1:
            riga = randint(0, R-1)
            colonna = randint(0, C-1)
            vicino = False

            for nriga in range(-1, 2):
                if nriga == -1 and y == 0:
                    continue
                elif nriga == 1 and y == R-1:
                    break

                for ncolonna in range(-1, 2):
                    if nriga == 0 and ncolonna == 0:
                        continue
                    if ncolonna == -1 and x == 0:
                        continue
                    elif ncolonna == 1 and x == C-1:
                        break
                    
                    if riga == (y+nriga) and colonna == (x+ncolonna):
                        vicino = True
                        break
                
                if vicino == True:
                    break

            if tabella[riga][colonna] != cella and tabellanum[riga][colonna] != "b" and not vicino:
                break
        
        tabellanum[riga].pop(colonna)
        tabellanum[riga].insert(colonna, "b")
        for nriga in range(-1, 2):
            if nriga == -1 and riga == 0:
                continue
            elif nriga == 1 and riga == R-1:
                break

            for ncolonna in range(-1, 2):
                if nriga == 0 and ncolonna == 0:
                    continue
                if ncolonna == -1 and colonna == 0:
                    continue
                elif ncolonna == 1 and colonna == C-1:
                    break
                
                if tabellanum[riga+nriga][colonna+ncolonna] == "b":
                    continue
                else:
                    tabellanum[riga+nriga][colonna+ncolonna] = str(int(tabellanum[riga+nriga][colonna+ncolonna]) + 1)

def ancora():
    global sec, PrimaVolta, tabella, tabellanum, timerloop
    
    try:
        window.after_cancel(timerloop)
    except:
        pass

    sec = 0
    PrimaVolta = True

    bombe.config(text = f"🚩 {numbombe}")
    orologio.config(text = f"🕙 {sec}")
    
    for riga in tabella:
        for cella in riga:
            cella.destroy()

    tabella, tabellanum = crea()

def pulisci():
    global numbombe
    for riga in range(len(tabella)):
        for colonna in range(len(tabella[riga])):
            if tabella[riga][colonna].cget("text") == "" or tabella[riga][colonna].cget("text") == "🚩":
                if (riga+colonna)%2 == 0:
                    colore = "darkolivegreen1"
                else:
                    colore = "darkolivegreen3"
                
                if tabellanum[riga][colonna] == "b":
                    if tabella[riga][colonna].cget("text") == "🚩":
                        numbombe += 1
                        tabella[riga][colonna].config(bg = "light salmon")
                    else:
                        tabella[riga][colonna].config(text = "🧨", bg = "light salmon", fg = "red4")
                else:
                    if tabellanum[riga][colonna] == "0":
                        tabellanum[riga].pop(colonna)
                        tabellanum[riga].insert(colonna, " ")

                    if tabella[riga][colonna].cget("text") == "🚩":
                        numbombe += 1
                        tabella[riga][colonna].config(bg = colore)
                    else:
                        tabella[riga][colonna].config(text = tabellanum[riga][colonna], bg = colore, fg = "black")

def sconfitta():
    pulisci()
    risposta = tk.messagebox.askquestion("Sconfitta", f"Hai perso in difficoltà {diff} \nDesideri rigiocare?")
    if risposta == "yes":
        ancora()
    else:
        window.destroy()

def vittoria():
    pulisci()
    risposta = tk.messagebox.askquestion("Vittoria", f"Bravo, hai completato Campo Minato in {sec} secondi a difficoltà {diff} \nDesideri rigiocare?")
    if risposta == "yes":
        ancora()
    else:
        window.destroy()

def intorno(cella):
    riga, colonna = -1, -1
    for nriga in range(len(tabella)):
        for ncolonna in range(len(tabella[riga])):
            if tabella[nriga][ncolonna] == cella:
                riga, colonna = nriga, ncolonna
                break
        
        if riga != -1:
            break
    
    bandiere = 0
    for nriga in range(-1, 2):
        if nriga == -1 and riga == 0:
            continue
        elif nriga == 1 and riga == R-1:
            break

        for ncolonna in range(-1, 2):
            if nriga == 0 and ncolonna == 0:
                continue
            if ncolonna == -1 and colonna == 0:
                continue
            elif ncolonna == 1 and colonna == C-1:
                break
            
            if tabella[riga+nriga][colonna+ncolonna].cget("text") == "🚩":
                bandiere += 1

    if bandiere == 0:
        return

    tab = []
    for nriga in range(-1, 2):
        temp = []
        if nriga == -1 and riga == 0:
            tab.append(["-","-","-"])
            continue
        elif nriga == 1 and riga == R-1:
            break

        for ncolonna in range(-1, 2):
            if nriga == 0 and ncolonna == 0:
                temp.append("-")
                continue
            if ncolonna == -1 and colonna == 0:
                temp.append("-")
                continue
            elif ncolonna == 1 and colonna == C-1:
                break

            temp.append(tabella[riga+nriga][colonna+ncolonna].cget("text"))
        
        tab.append(temp)

    print()
    for a in tab:
        print(a)
    
    i = 0

    if bandiere == int(tabella[riga][colonna].cget("text")):
        for nriga in range(-1, 2):
            if nriga == -1 and riga == 0:
                continue
            elif nriga == 1 and riga == R-1:
                break

            for ncolonna in range(-1, 2):
                if nriga == 0 and ncolonna == 0:
                    continue
                if ncolonna == -1 and colonna == 0:
                    continue
                elif ncolonna == 1 and colonna == C-1:
                    break
                
                i += 1

                if tabella[riga+nriga][colonna+ncolonna].cget("text") == "🚩":
                    print("band",i)
                    continue
                else:
                    print(i)
                    if (riga+nriga+colonna+ncolonna)%2 == 0:
                        colore = "bisque"
                    else:
                        colore = "peachpuff2"

                    if tabellanum[riga+nriga][colonna+ncolonna] == "0":
                        tabellanum[riga+nriga].pop(colonna+ncolonna)
                        tabellanum[riga+nriga].insert(colonna+ncolonna, " ")
                        libera(riga+nriga, colonna+ncolonna)
                    
                    if tabellanum[riga+nriga][colonna+ncolonna] == "b":
                        tabella[riga+nriga][colonna+ncolonna].config(text = "🧨", bg = "light salmon", fg = "red4")
                        sconfitta()
                        return

                    tabella[riga+nriga][colonna+ncolonna].config(bg = colore, text = tabellanum[riga+nriga][colonna+ncolonna], fg = "black")

        for riga in range(len(tabella)):
            for colonna in range(len(tabella[riga])):
                if (tabella[riga][colonna].cget("text") == "" or tabella[riga][colonna].cget("text") == "🚩")  and tabellanum[riga][colonna] != " " and tabellanum[riga][colonna] != "b":
                    return
                elif riga == len(tabella)-1 and colonna == len(tabella)-1:
                    window.after_cancel(timerloop)
                    vittoria()
                    return

def clicksx(evento):
    global PrimaVolta, timerloop
    cella = evento.widget

    if cella.cget("text") == "":
        if PrimaVolta:
            generabombe(cella)
            PrimaVolta = False
            timer()
            for riga in tabellanum:
                print(riga)

        for riga in range(len(tabella)):
            for colonna in range(len(tabella[riga])):
                if tabella[riga][colonna] == cella:
                    if (riga+colonna)%2 == 0:
                        colore = "bisque"
                    else:
                        colore = "peachpuff2"
                    
                    if tabellanum[riga][colonna] == "b":
                        cella.config(text = "🧨", bg = "light salmon", fg = "red4")
                        window.after_cancel(timerloop)
                        sconfitta()
                        return
                    else:
                        if tabellanum[riga][colonna] == "0":
                            tabellanum[riga].pop(colonna)
                            tabellanum[riga].insert(colonna, " ")
                            libera(riga, colonna)
                
                        cella.config(text = tabellanum[riga][colonna], bg = colore, fg = "black")

                    break
        
        for riga in range(len(tabella)+1):
            for colonna in range(len(tabella[riga])+1):
                if (tabella[riga][colonna].cget("text") == "" or tabella[riga][colonna].cget("text") == "🚩")  and tabellanum[riga][colonna] != " " and tabellanum[riga][colonna] != "b":
                    return
                elif riga == len(tabella)+1 and colonna == len(tabella)+1:
                    window.after_cancel(timerloop)
                    vittoria()
                    return
    
    else:
        intorno(cella)

def clickdx(evento):
    global numbombe

    cella = evento.widget
    for riga in range(len(tabella)):
        for colonna in range(len(tabella[riga])):
            if tabella[riga][colonna] == cella:
                if tabella[riga][colonna].cget("text") == "":
                    cella.config(text = "🚩", fg = "red4")
                    numbombe -= 1
                    bombe.config(text = f"🚩 {numbombe}")
                elif tabella[riga][colonna].cget("text") == "🚩":
                    cella.config(text = "")
                    numbombe += 1
                    bombe.config(text = f"🚩 {numbombe}")
                    
                break

window = tk.Tk()

frameAlto = tk.Frame(window, bg = "green4")
frameAlto.pack(fill = "x")

titolo = tk.Label(frameAlto, text = "Campo Minato", bg = "DarkOliveGreen2", font = "Helvetica 20")
titolo.pack(side = "left")
combodiff = tk.ttk.Combobox(frameAlto, values = valoridiff, state = "readonly")
combodiff.current(1)
combodiff.bind("<<ComboboxSelected>>", cambiadiff)
combodiff.pack(side = "left", padx=10)

bombe = tk.Label(frameAlto, text = f"🚩 {numbombe}", fg = "Red", bg = "DarkOliveGreen2", font = "Helvetica 15")
bombe.pack(side = "right", pady=20)
orologio = tk.Label(frameAlto, text = f"🕙 {sec}", bg = "DarkOliveGreen2", font = "Helvetica 15")
orologio.pack(side = "right", padx=10)

frameGriglia = tk.Frame(window)
frameGriglia.pack()

tabella, tabellanum = crea()

window.mainloop()