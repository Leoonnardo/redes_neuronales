from cmath import sqrt
import numpy as np
import random as rand
import matplotlib.lines as mlines
import matplotlib.pyplot as plt

X =[
    [1,0,0],
    [1,1,0],
    [1,0,1],
    [1,1,1],
]

Y = [0 for i in range(3)]
Y.append(1)


# list = [round(rand.random(),3) for i in range(3)]
n = 0.4

X = np.array(X).transpose()

Y = np.array(Y)

k = 0

# print('---------------------------')
# print('DATOS INICIALES')
# print(f'Generacion = {k}')
# print(f'W = {wk}')
# print(f'N = {n}')
# print('---------------------------')

# calculos(n, k, X, Y, wk)

def ponderacion(w):
    print(float(w[0]))
    wk = np.array([(float(w[0]), float(w[1]), float(w[2]))])
    print(wk)
    return wk

def calculos(ns, ws, k, X, Y):
    errorTemp = []
    kTemp = []
    errorK = []
    n = ns
    wk = ponderacion(ws)
    # 0.854,0.327,0.558,0.456,0.541,0.78
    while(True):
        k += 1
        kTemp.append(k)
        uk = np.dot(wk,X)

        yck = np.array([0 if uk[0][i] < 0 else 1  for i in range(len(uk[0]))])

        ek = Y-yck

        temp = np.dot(X,ek) * n

        wt = wk + temp

        cont = 0

        for i in range(len(ek)):
            cont += ek[i]**2

        print('---------------------------')
        print('DATOS')
        print(f'Generacion = {k}')
        print(f'W = {wk}')
        print(f'Uk = {uk}')
        print(f'Yck = {yck}')
        print(f'Ek = {ek}')
        print(f'wt = {wt}')
        print(f'error = Raiz de {cont}')
        valorRaiz = abs(sqrt(cont).conjugate())
        errorTemp.append(valorRaiz)
        print(f'error = {valorRaiz}')
        print('---------------------------')

        wk = wt
        if np.all(yck == Y):
            print(f'Y calculada = {yck}')
            print(f'Y deseada = {Y}')
            break
    errorK.append(errorTemp)
    errorK.append(kTemp)
    return errorK

def iteraciones(n1, n2, n3, n4, n5, ws):
    errores = []
    numErrores = []
    for i in range(5):
        print("----Numero ",i+1 ,"----")
        if i == 0:
            n1 = float(n1)
            datos = calculos(n1, ws, k, X, Y)
            errores.append(datos[0])
            numErrores.append(datos[1])
        elif i == 1:
            n2 = float(n2)
            datos = calculos(n2, ws, k, X, Y)
            errores.append(datos[0])
            numErrores.append(datos[1])
        elif i == 2:
            n3 = float(n3)
            datos = calculos(n3, ws, k, X, Y)
            errores.append(datos[0])
            numErrores.append(datos[1])
        elif i == 3:
            n4 = float(n4)
            datos = calculos(n4, ws, k, X, Y)
            errores.append(datos[0])
            numErrores.append(datos[1])
        elif i == 4:
            n5 = float(n5)
            datos = calculos(n5, ws, k, X, Y)
            errores.append(datos[0])
            numErrores.append(datos[1])
    print("Errores: ", errores)
    print("Num Errores: ", numErrores)

    figure2 = plt.figure(figsize=(15, 10))

    ax = plt.subplot(1,1,1)

    # print(self.ns[0])
    # print(self.curvas[0])

    ax.set_title('Grafica')
    for x in range(len(errores)):
        ax.plot(numErrores[x], errores[x], marker='o',label=f'N {x+1}')

    ax.legend()

    plt.show()