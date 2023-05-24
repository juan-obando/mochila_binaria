import re

# Definición de funciones -------------------------------
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


# def parametro(v1, v2):
#     if sum(v1[k] * v2[k] for k in v1.keys()) >= P:
#         return True
#     else:
#         return False


# Cuerpo del procedimiento ---------------------------------------
if __name__ == "__main__":

    # Recibiendo el costo
    entrada = input("Ingrese el costo de los elementos separados por espacio: ").split()

    values = {}
    valores = {}

    for i, costo in enumerate(entrada):
        key = f'X{i+1}' 
        values[key] = int(costo)


    # Recibiendo el peso
    entrada = input("Ingrese el peso de los elementos separados por espacio: ").split()

    weight = {}

    for i, peso in enumerate(entrada):
        key = f'X{i+1}' 
        weight[key] = int(peso)

    # Recibiendo el peso máximo de la mochila
    maxWeight = int(input("Ingrese el volumen máximo de la mochila: "))
    # P = int(input("Ingrese el parámetro de parada: "))

    ## Restricciones
    ## Esta es para las restricciones
    Restricciones = {}
    NR = int(input("Ingrese el número de restricciones del problema: "))  # Número de restricciones del problema

    for q in range(NR):
        r2 = {}
        for i in range(len(entrada)):
            r2["X" + str(i + 1)] = 0

        expresion = input("Ingresa una restricción (ej: 3X3 + 15X6 + 9X7 <= 15): ")

        # Utilizar expresiones regulares para extraer los nombres de las variables y los coeficientes
        matches = re.findall(r'([+-]?)(\d*)\s*([Xx]\d+)', expresion)

        for match in matches:
            signo = match[0]
            numero = match[1]
            variable = match[2]

            if numero == "":
                numero = "1"
            if signo == "-":
                numero = "-" + numero

            r2[variable] = int(numero)  # Convertir el número a entero antes de guardar en el diccionario
        
        try:
            leq_match = re.search(r'<=\s*(\d+)', expresion)
            leq = int(leq_match.group(1))
        except AttributeError:
            leq = 0

        valores[q]=leq 
        Restricciones[q] = r2
        

    print(Restricciones)

    # El método que usaremos será por mayor costo/peso
    # Por eso, acá generamos la lista con este valor

    vw = {}

    for key in values.keys():
        vw[key] = round(values[key]/weight[key], 2)


    # # Imprimimos los diccionarios
    print("\n\nProductos:\n")
    print("Costo: ", values)
    print("Peso: ", weight)
    # print("Costo/Peso: ", vw)
    # print("Restricción 1: ", r1)
    # print("Restricción 2: ", r2)


    # MAYOR COSTO/PESO ---------------------------------------------------------
    # Ordenando de acuerdo al mayor costo/peso
    vw = dict(sorted(vw.items(), key=lambda x: x[1], reverse=True))
    values = dict(sorted(values.items(), key=lambda x: vw[x[0]], reverse=True))
    weight = dict(sorted(weight.items(), key=lambda x: vw[x[0]], reverse=True))


    # Conjunto candidatos
    c = {}
    for key in vw.keys():
        c[key] = 1

    # Conjunto de candidatos aceptados
    s = {}
    for key in vw.keys():
        s[key] = 0

    # Conjunto solución
    solution = {}
    for i in range(len(entrada)):
        solution["X"+str(i+1)] = 0

    # Algoritmo ------------------------------------
    for key in c.keys():
        c[key] = 0
        s[key] = 1

        if sumaproducto(weight, s) and restricciones(s, Restricciones):
            solution[key] = 1
        else:
            s[key] = 0


    # MAYOR COSTO ---------------------------------------------------------
    # Ordenando de acuerdo al mayor costo
    values1 = values
    weight1 = weight
    values1 = dict(sorted(values1.items(), key=lambda x: x[1], reverse=True))
    weight1 = dict(sorted(weight1.items(), key=lambda x: values1[x[0]], reverse=True))


    # Conjunto candidatos
    c = {}
    for key in values1.keys():
        c[key] = 1

    # Conjunto de candidatos aceptados
    s = {}
    for key in values1.keys():
        s[key] = 0

    # Conjunto solución
    solution1 = {}
    for i in range(len(entrada)):
        solution1["X"+str(i+1)] = 0

    # Algoritmo ------------------------------------
    for key in c.keys():
        c[key] = 0
        s[key] = 1

        if sumaproducto(weight, s) and restricciones(s, Restricciones):
            solution1[key] = 1
        else:
            s[key] = 0
    
    if sum(solution[k] * values[k] for k in solution.keys()) < sum(solution1[k] * values[k] for k in solution1.keys()):
        solution = solution1


    # MENOR PESO ---------------------------------------------------------
    # Ordenando de acuerdo al menor peso
    values2 = values
    weight2 = weight
    weight2 = dict(sorted(weight2.items(), key=lambda x: x[1]))
    values2 = dict(sorted(values2.items(), key=lambda x: weight2[x[0]], reverse=True))


    # Conjunto candidatos
    c = {}
    for key in weight2.keys():
        c[key] = 1

    # Conjunto de candidatos aceptados
    s = {}
    for key in weight2.keys():
        s[key] = 0

    # Conjunto solución
    solution2 = {}
    for i in range(len(entrada)):
        solution2["X"+str(i+1)] = 0

    # Algoritmo ------------------------------------
    for key in c.keys():
        c[key] = 0
        s[key] = 1

        if sumaproducto(weight, s) and restricciones(s, Restricciones):
            solution2[key] = 1
        else:
            s[key] = 0
    
    if sum(solution[k] * values[k] for k in solution.keys()) < sum(solution2[k] * values[k] for k in solution2.keys()):
        solution = solution2
    
    # Solución ------------------------------
    print("\n\nSe encontró una solución óptima con el vector:", solution)
    print("Con un costo máximo de:", sum(solution[k] * values[k] for k in solution.keys()))
