# Laboratorio 2 - Recurrencia
_Funciones que dan solución a los siguientes problemas:_

* A. Escriba una función recursiva que ordene de menor a mayor una lista de enteros basándose en la siguiente idea: coloque el elemento más pequeño en la primera ubicación, y luego ordene el resto del arreglo con una llamada recursiva.
​
* B. Escribir una función recursiva que devuelva la suma de un subarreglo de N enteros, límitado por indices (i,j)  en una lista de enteros L
* C. Escribir una función y un programa que encuentre la suma de los enteros positivos pares desde N hasta 2.
* D. Dada una función recursiva para MCD cómo
​
  MCD = M si N =0
  MCD = MCD (N, M mod N) si N <> 0
​
 Escriba un programa que le permita al usuario ingresar los valores para M y N desde la consola. Una función recursiva es entonces llamada para calcular el MCD. El      programa entonces imprime el valor para el MCD.
* E. Programe un método recursivo que transforme un número entero positivo a notación binaria.
​
  Ejemplo: 5 - 101
​
* F. Programe un método recursivo que invierta los números de un arreglo de enteros.

* H. Para la implementación de Merge en el algoritmo merge_sort visto en clase, haga el análisis temporal por métdodo de factores con función cáracteristica para el peor y el mejor de los casos

## Ejecutando las pruebas ⚙️

```
print(ordenar([5,3,8,1,2,2,-54634,12]))
print(sumasubarreglos([4,2,3,5,6], 1, 2))
print(sumaenterospares(11))
print(MCD(3, 55))
print(notabinario(153))
print(invertir_arreglo([3,5,1,6,-1,2342,43]))
print(mergeSort([6,5,8,4]))

```

