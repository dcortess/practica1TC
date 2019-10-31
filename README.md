# Practica 1: Ludus Strategy
### **David Cortes i Albert Pijuan** - Tecniques de Computacio

## 1. Quod secretum nuntius

### Analisi de costos

#### Disseny iteratiu
Aquest es el disseny que hem implementat per resoldre el problema de manera **iterativa**:

    def decrypt(value):
        while value > 9:
            value = sum(int(i) for i in str(value))
        return value


Que equival a la formula (Taula representada en l'apartat "Taules de costos segons el disseny"):

$O(n) = log_{10} n $

El cost del millor cas seria quan el numero esta format per 1 digit, el cost seria 1.
En el pitjor dels casos, tindria n digits.
Cas promig: depen de la probabilitat de cada instancia.
El cost seria el sumatori de (i+1)*(1/n)  que es igual a (n+1)/2


El disseny que hem implementat per resoldre el problema de manera **recursiva** es el seg�ent:

    def decryptRecursive(value):
        value = str(value)
        suma = 0
        for i in value:
            suma += int(i)
        if (suma <= 9):
            return suma
        else:
            value = suma
            return decryptRecursive(value)

Que equival a la formula (Taula representada en l'apartat "Taules de costos segons el disseny"):


$O(n) = log_{10} n $


### Experiments amb diferents valors

    
    def testIteratiu(n, r):
        for i in range(len(n)):
            if(decrypt(n[i]) == r[i]):
                print("Test correcte")
            else:
                print("Test ERRONI")
                
    test([36, 12345, 1542524, 458726214, 547874459893, 5254512145578], [9, 6, 5, 3, 1, 9]) #Primerament li passem uns valors per a que decripti i despres li passem els valors correctes d'aquest decriptament

    def testRecursiu(n, r):
        for i in range(len(n)):
            if(decryptRecursive(n[i]) == r[i]):
                print("Test correcte")
            else:
                print("Test ERRONI")

    test([36, 12345, 1542524, 458726214, 547874459893, 5254512145578], [9, 6, 5, 3, 1, 9]) #Primerament li passem uns valors per a que decripti i despres li passem els valors correctes d'aquest decriptament


### Grafiques i taules
#### Grafica del cost de l'algorisme

    import random
    import math
    import time

    n = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] #Numero de termes
    lis  = [0,0.3,0.47,0.60,0.69,0.77,0.84,0.90,0.95,1,1.04,1.07,1.11,1.14,1.17,1.20,1.23,1.25,1.27,1.30]

    import matplotlib.pyplot as plt
    import numpy as np

    plt.plot(n,lis, 'g',label='iteratiu')
    plt.xlabel('Numero de termes')
    plt.ylabel('Temps (microsegons)')
    plt.title('Temps Iteratiu i Recursiu')
    plt.legend()
    plt.show()

#### Taules de costos segons el disseny
Disseny iteratiu

| Linia |                Operacio                   | Cost |  Iteracions  |
|-------|-------------------------------------------|------|--------------|
|   1   |              `while value>9`              |  C1  |  log_{10}+1  |
|   2   | `value = sum(int(i) for i in str(value))` |  C2  |   log_{10}   |
|   3   |              `return value`               |  C3  |      1       |


Disseny recursiu

| Linia |                Operacio                   | Cost |  Iteracions  |
|-------|-------------------------------------------|------|--------------|
|   1   |           `value = str(value)`            |  C1  |      n       |
|   2   |                `suma = 0`                 |  C2  |      n       |
|   3   |             `for i in value:`             |  C3  |     n^2      |
|   4   |             `suma += int(i)`              |  C4  |     n^2      |
|   5   |             `if (suma <= 9)`              |  C5  |      n       |
|   6   |              `return suma`                |  C6  |      n       |
|   7   |                 `else`                    |  C7  |      n       |
|   8   |              `value = suma`               |  C8  |      n       |
|   9   |      `return decryptRecursive(value)`     |  C9  |      n       |



#### Grafica de l'eficiencia a nivell de temps d'execucio dels algoritmes

    import random
    import math
    import time
    n = [10,12345,54125,55748,7458896,554125333,457985649425]
    for i in range(len(n)):
        %timeit decrypt(n[i])
        %timeit decryptRecursive(n[i])

    n = [10,12345,54125,55748,7458896,554125333,457985649425]
    decrypt  = [1.01,2.53,2.67,3.36,3.88,3.58,4.76]
    decryptRecursive = [0.681,1.96,1.98,2.63,2.9,2.6,4.06]

    import matplotlib.pyplot as plt
    import numpy as np

    plt.plot(n,decrypt, 'g',label='iteratiu')
    plt.plot(n,decryptRecursive, 'b',label='recursiu')
    plt.xscale('log')
    plt.xlabel('Inputs')
    plt.ylabel('Temps (microsegons)')
    plt.title('Temps Iteratiu/Recursiu')
    plt.legend()
    plt.show()


## 2. Jedi combo
### Analisi de costos

#### Disseny iteratiu
Aquest es el disseny que hem implementat per resoldre el problema de manera **iterativa**:


    def lis(arr): 
        n = len(arr)   
        lis = [1]*n 
        
        llistaindex = [0]*n
        for i in range(0, n):
            llistaindex[i] = i
        
        for i in range (1 , n): 
            for j in range(0 , i): 
                if arr[i] > arr[j] and lis[i]< lis[j] + 1 : 
                    lis[i] = lis[j]+1
                    llistaindex[i] = j
      
        maximum = 0
        index = 0
        
        for i in range(n): 
            if (maximum < lis[i]):
                maximum = lis[i]
                index = i
            
        seq = [arr[index]]
        while (index != llistaindex[index]):
            index = llistaindex[index]
            seq.append(arr[index])
            
            
        llistafinal = seq[::-1]
        return llistafinal


Que equival a la formula (Taula representada en l'apartat "Taules de costos segons el disseny"):

$O(n) = n^2$



### Experiments amb diferents valors

    def testIteratiu(n, r):
        for i in range(len(n)):
            if(lis(n) == r):
                print("Test correcte")
            else:
                print("Test ERRONI")
                
    testIteratiu([3, 10, 2, 1, 20], [3, 10, 20])
    testIteratiu([1, 5, 2, 8, 10, 20, 6], [1, 5, 8, 10, 20])
    testIteratiu([2, 1, 4, 2, 9, 8, 10, 22, 15, 19], [2, 4, 9, 10, 15, 19])
    testIteratiu([10, 2, 3, 9, 15, 18, 23, 5, 26, 30, 16, [2, 3, 9, 15, 18, 23, 26, 30])

### Grafiques i taules
#### Taules de costos segons el disseny
Disseny iteratiu

| Linia |                Operacio                   | Cost |  Iteracions  |
|-------|-------------------------------------------|------|--------------|
|   5   |           `for i in range(0, n)`          |  C1  |      n       |
|   8   |          `for i in range (1 , n)`         |  C2  |      n       |
|   9   |          `for j in range(0 , i)`          |  C3  |     n^2      |
|   17  |            `for i in range(n)`            |  C3  |      n       |
|   23  |   `while (index != llistaindex[index])`   |  C3  |      n       |




#### Grafica de l'eficiencia a nivell de temps d'execucio dels algoritmes

    import random
    import math
    import time
    n = [[3, 10, 2, 1, 20],[1, 5, 2, 8, 10, 20, 6],[2, 1, 4, 2, 9, 8, 10, 22, 15, 19], [10, 2, 3, 9, 15, 18, 23, 5, 26, 30, 16]]
    for i in range(len(n)):
        %timeit lis(n[i])

    n = [5,7,10,11] #Numero de termes
    lis  = [5.12,8.12,12.7,15.5]

    import matplotlib.pyplot as plt
    import numpy as np

    plt.plot(n,lis, 'g',label='iteratiu')
    plt.xlabel('Numero de termes')
    plt.ylabel('Temps (microsegons)')
    plt.title('Temps Iteratiu')
    plt.legend()
    plt.show()

#### Grafica del cost de l'algorisme

    import random
    import math
    import time

    n = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] #Numero de termes
    lis  = [1,4,9,16,25,36,49,64,81,100,121,144,169,196,225,256,289,324,361,400]

    import matplotlib.pyplot as plt
    import numpy as np

    plt.plot(n,lis, 'g',label='iteratiu')
    plt.xlabel('Numero de termes')
    plt.ylabel('Temps (microsegons)')
    plt.title('Temps Iteratiu')
    plt.legend()
    plt.show()
