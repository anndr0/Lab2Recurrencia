#A EScriba una función que ordene de menor a mayor una lista de enteros basándose en la siguiente idea:

# coloque el elemento más pequeño en la primera ubicación, y luego ordene el resto del arreglo con una llamada recursiva.
def ordenar(A):
    if len(A) <= 0:
        return A
    minimo = min(A)
    B = []
    C = []
    for i in range(len(A)):
        if A[i] == minimo:
            C.append(A[i])
        else:
            B.append(A[i])
    result = C + ordenar(B)
    return result
print(ordenar([5,3,8,1,2,2,-54634,12]))


#B Escribir una función recursiva que devuelva la suma de un subarreglo de N enteros,
# límitado por indices (i,j)  en una lista de enteros L
def sumasubarreglos(A, i, j):
    if len(A) <= 1 or i == j:
        return A[i]
    return A[i] + sumasubarreglos(A, i+1, j)
print(sumasubarreglos([4,2,3,5,6], 1, 2))


#C. Escribir una función y un programa que encuentre
# la suma de los enteros positivos pares desde N hasta 2.

def sumaenterospares(n):
    if n <= 2:
        return n
    else:
        if n%2==1:
            n = sumaenterospares(n-1)
        else:
            n += sumaenterospares(n-2)
    return n
print(sumaenterospares(11))


#D Dada una funcion recursiva para MCD cómo
#MCD = M si N = 0
#MCD = MCD(N, M mod N) si N <> 0
#Escriba un programa que le permita al usuario ingresar los valores
# para M y N desde la consola. Una función recursiva es entonces llamada para calcular el MCD.
# El programa entonces imprime el valor para el MCD.
#PRE: m debe ser mayor que n
def MCD(n,m):
    if m == 0: # Caso Base
        return n
    if n == 0:  # Caso Base
        return 1 # en caso de que nos quedamos sin cociente, el mcd es 1
    else:
        mcd = MCD(m//n, m%n)   #Segun el MCD, lo q se hace es descomponer los numeros hasta que el residuo sea cero
    return mcd  # el valor de n es el cociente y m va tomando el residuo de esas divisiones, el cociente es lo que se retorna
print(MCD(3, 55))


#E Programe un método recursivo que transforme un número
# entero positivo a notación binaria.
def notabinario(n):
    lista = []
    if n <= 1:
        return n
    lista = str(n%2) + str(notabinario(n//2))
    return lista
print(notabinario(153))


#F  Programe un método recursivo que
# invierta los números de un arreglo de enteros.
def invertir_arreglo(A=[]):
    return A if len(A) <= 1 else [A[-1]] + invertir_arreglo(A[:-1])


#H Para la implementación de Merge en el algoritmo merge_sort visto en clase,
# haga el análisis temporal por método de factores con función cáracteristica
# para el peor y el mejor de los casos
#Pre: A y B están ordenadas
def merge(A=[], B=[]):                             #cost        times(O)        times(Ohm)
    i,j, result = 0,0, []                           #c1             1               1
    while i < len(A) and j < len(B):                #c2             n + 1           n
        if A[i] <= B[j]:                            #c3             n               n
            result.append(A[i])                     #c4             n / 2           n
            i+=1                                    #c5             n / 2           n
        else:                                       #c6             n               0
            result.append(B[j])                     #c7             n / 2           0
            j+=1                                    #c8             n / 2           0
    # Alguna de las secuencias tiene restante
    if i < len(A):                                  #c9             n               n
        result += A[i:]                             #c10            n / 2           n
    else:                                           #c11            n               0
        result += B[j:]                             #c12            n / 2           0
    return result                                   #c13            1               1

    #T(O) = n
    #T(Ohm) = n

# pre : A es una secuencia de elementos comparables
# pos : Los elementos estan ordenados
def mergeSort(A=[]):
    if len(A) <= 1:
        return A
    half = len(A)//2
    left, right = mergeSort(A[:half]), mergeSort(A[half:])
    result = merge(left, right) #Combinar
    return result
print(mergeSort([6,5,8,4]))



