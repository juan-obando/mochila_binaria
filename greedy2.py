import tkinter as tk
import re

def sumaproducto(v1, v2):
    if sum(v1[k] * v2[k] for k in v2.keys()) <= maxWeight:
        return True
    else:
        return False

def restricciones(s, restricciones):
    for i in restricciones:
        if sum(s[k] * restricciones[i][k] for k in restricciones[i].keys()) <= valores[i]:
            return True
        else:
            return False

def snap_solved(cost_entries, weight_entries, max_vol, num_constraints, constraints):
    values = {f'X{i+1}': cost for i, cost in enumerate(cost_entries)}
    weight = {f'X{i+1}': w for i, w in enumerate(weight_entries)}
    maxWeight = max_vol
    Restricciones = constraints
    valores = {i: r[-1] for i, r in enumerate(Restricciones)}
    
    vw = {key: round(values[key]/weight[key], 2) for key in values.keys()}

    vw = dict(sorted(vw.items(), key=lambda x: x[1], reverse=True))
    values = dict(sorted(values.items(), key=lambda x: vw[x[0]], reverse=True))
    weight = dict(sorted(weight.items(), key=lambda x: vw[x[0]], reverse=True))

    c = {key: 1 for key in vw.keys()}
    s = {key: 0 for key in vw.keys()}
    solution = {f"X{i+1}": 0 for i in range(len(cost_entries))}

    for key in c.keys():
        c[key] = 0
        s[key] = 1
        if sumaproducto(weight, s) and restricciones(s, Restricciones):
            solution[key] = 1
        else:
            s[key] = 0

    return solution, sum(solution[k] * values[k] for k in solution.keys())

# Tkinter GUI
def submit_button():
    cost_entries = list(map(int, ECosto.get().split()))
    weight_entries = list(map(int, Epeso.get().split()))
    max_vol = int(EVmax.get())
    num_constraints = int(Eres.get())
    constraints = [list(map(int, entry.get().split())) for entry in constraint_entries]  # Extraer restricciones de los campos de entrada
    solution, max_cost = snap_solved(cost_entries, weight_entries, max_vol, num_constraints, constraints)
    solution_var.set(f"Solution: {solution}, Max cost: {max_cost}")

Greedy = tk.Tk()
Greedy.geometry("900x600")
Greedy.title("Greedy (Problema de la mochila binaria)")

Titulo = tk.Label(Greedy, text="GREEDY", font=("Stencil", 34), anchor="center")
Titulo.place(x=360,y=10)

Titulo1 = tk.Label(Greedy, text="Problema de la mochila binaria", font=("Times New Roman", 14), anchor="e")
Titulo1.place(x=330, y=60)

Texto= tk.Label(Greedy, text="Ingrese el costo de los elementos separados por espacio: [Ej: 7 8 1 2...]", font=("Times New Roman",12), anchor="w")
Texto.place(x=30,y=100)
ECosto = tk.Entry(Greedy, width=102, font=("Times New Roman",12))
ECosto.place(x=33,y=135)

Texto = tk.Label(Greedy, text="Ingrese el peso de los elementos separados por espacio: [Ej: 6 10 4 3...]", font=("Times New Roman",12), anchor="w")
Texto.place(x=30,y=170)
Epeso = tk.Entry(Greedy, width=102, font=("Times New Roman",12))
Epeso.place(x=33,y=200)

Texto = tk.Label(Greedy, text="Ingrese el volumen maximo de la mochila: ", font=("Times New Roman",12), anchor="w")
Texto.place(x=30,y=240)
EVmax = tk.Entry(Greedy, width=7, font=("Times New Roman",12))
EVmax.place(x=290,y=243)

Texto = tk.Label(Greedy, text="Ingrese el numero de restricciones:  ", font=("Times New Roman",12), anchor="w")
Texto.place(x=30,y=290)
Eres = tk.Entry(Greedy, width=7, font=("Times New Roman",12))
Eres.place(x=250,y=293)

constraint_entries = []
for i in range(num_constraints):  # Añadir un campo de entrada para cada restricción
    constraint_label = tk.Label(Greedy, text=f"Restricción {i+1}: ", font=("Times New Roman",12), anchor="w")
    constraint_label.place(x=30, y=330+i*30)
    constraint_entry = tk.Entry(Greedy, width=102, font=("Times New Roman",12))
    constraint_entry.place(x=33, y=360+i*30)
    constraint_entries.append(constraint_entry)

submit_button = tk.Button(Greedy, text="Submit", command=submit_button)
submit_button.place(x=400,y=400)

solution_var = tk.StringVar()
solution_label = tk.Label(Greedy, textvariable=solution_var)
solution_label.place(x=400,y=450)

Greedy.mainloop()
