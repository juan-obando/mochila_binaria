import tkinter as tk
import re

def parse_constraint(constraint_str):
    terms = constraint_str.split("+")
    coeff_dict = {}
    value = 0
    for term in terms:
        term = term.strip()
        if "<=" in term:
            value = int(term.split("<=")[1].strip())
        else:
            coeff, variable = re.match(r'(\d*)X(\d*)', term).groups()
            coeff_dict[f'X{variable}'] = int(coeff)
    return coeff_dict, value

def sumaproducto(v1, v2, maxWeight):
    if sum(v1.get(k, 0) * v2.get(k, 0) for k in set(v1.keys()).union(v2.keys())) <= maxWeight:
        return True
    else:
        return False

def restricciones(s, restricciones, valores):
    for i, restriccion in enumerate(restricciones):
        if sum(s.get(k, 0) * restriccion.get(k, 0) for k in set(s.keys()).union(restriccion.keys())) <= valores[i]:
            continue
        else:
            return False
    return True

def snap_solved(cost_entries, weight_entries, max_vol, constraints):
    values = {f'X{i+1}': cost for i, cost in enumerate(cost_entries)}
    weight = {f'X{i+1}': w for i, w in enumerate(weight_entries)}
    maxWeight = max_vol
    Restricciones = [r[0] for r in constraints]
    valores = [r[1] for r in constraints]

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
        if sumaproducto(weight, s, maxWeight) and restricciones(s, Restricciones, valores):
            solution[key] = 1
        else:
            s[key] = 0

    max_cost = sum(solution[k] * values[k] for k in solution.keys())
    
    # MAYOR COSTO 
    values1 = dict(sorted(values.items(), key=lambda x: x[1], reverse=True))
    weight1 = dict(sorted(weight.items(), key=lambda x: values1[x[0]], reverse=True))
    c1 = c
    s1 = s
    solution1 = solution

    for key in c1.keys():
        c1[key] = 0
        s1[key] = 1
        if sumaproducto(weight1, s1, maxWeight) and restricciones(s1, Restricciones, valores):
            solution1[key] = 1
        else:
            s1[key] = 0

    max_cost1 = sum(solution1[k] * values1[k] for k in solution1.keys())
    
    # MENOR PESO
    values2 = dict(sorted(values.items(), key=lambda x: weight[x[0]]))
    weight2 = dict(sorted(weight.items(), key=lambda x: weight[x[0]]))
    c2 = c
    s2 = s
    solution2 = solution

    for key in c2.keys():
        c2[key] = 0
        s2[key] = 1
        if sumaproducto(weight2, s2, maxWeight) and restricciones(s2, Restricciones, valores):
            solution2[key] = 1
        else:
            s2[key] = 0

    max_cost2 = sum(solution2[k] * values2[k] for k in solution2.keys())
    
    if max_cost >= max_cost1 and max_cost >= max_cost2:
        return solution
    elif max_cost1 >= max_cost and max_cost1 >= max_cost2:
        return solution1
    else:
        return solution2



def generate_constraint_entries():
    """
    Esta función se encarga de generar las entradas de restricciones en la interfaz de usuario.
    """
    num_constraints = int(Eres.get())
    for i in range(num_constraints):
        constraint_label = tk.Label(Greedy, text=f"Restricción {i+1}: ", font=("Times New Roman",12), anchor="w")
        constraint_label.place(x=30, y=330+i*30)
        constraint_entry = tk.Entry(Greedy, width=91, font=("Times New Roman",12))
        constraint_entry.place(x=120, y=330+i*30)
        constraint_entries.append(constraint_entry)

def submit_button():
    """
    Esta función es llamada cuando el usuario presiona el botón de enviar.
    Toma las entradas del usuario y las pasa a la función de resolución del problema de la mochila.
    """
    cost_entries = list(map(int, ECosto.get().split()))
    weight_entries = list(map(int, Epeso.get().split()))
    max_vol = int(EVmax.get())
    constraints = [parse_constraint(entry.get()) for entry in constraint_entries]
    solution, max_cost = snap_solved(cost_entries, weight_entries, max_vol, constraints)
    solution_var.set(f"Solucion: {solution}, Costo maximo: {max_cost}")

Greedy = tk.Tk()
Greedy.geometry("900x900")
Greedy.title("Greedy (Problema de la mochila binaria)")

# Aquí se configura la interfaz de usuario.
# Se crean y se colocan los widgets necesarios.

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

Eres_button = tk.Button(Greedy, text="Generar campos de restricciones", command=generate_constraint_entries)
Eres_button.place(x=400,y=293)

constraint_entries = []

submit_button = tk.Button(Greedy, text="Submit", command=submit_button)
submit_button.place(x=400,y=750)

solution_var = tk.StringVar()
solution_label = tk.Label(Greedy, textvariable=solution_var)
solution_label.place(x=200,y=780)

Greedy.mainloop()
