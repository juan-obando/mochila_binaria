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
    constraints = []  # Aquí debes llenar las restricciones basado en tus entradas en la GUI
    solution, max_cost = snap_solved(cost_entries, weight_entries, max_vol, num_constraints, constraints)
    solution_var.set(f"Solution: {solution}, Max cost: {max_cost}")

Greedy = tk.Tk()
Greedy.geometry("900x600")
Greedy.title("Greedy (Problema de la mochila binaria)")

Titulo = tk.Label(Greedy, text="GREEDY", font=("Stencil", 34))
Titulo.pack()

ECosto = tk.Entry(Greedy)
ECosto.pack()

Epeso = tk.Entry(Greedy)
Epeso.pack()

EVmax = tk.Entry(Greedy)
EVmax.pack()

Eres = tk.Entry(Greedy)
Eres.pack()

submit_button = tk.Button(Greedy, text="Submit", command=submit_button)
submit_button.pack()

solution_var = tk.StringVar()
solution_label = tk.Label(Greedy, textvariable=solution_var)
solution_label.pack()

Greedy.mainloop()
