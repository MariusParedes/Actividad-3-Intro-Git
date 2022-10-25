# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
cadena=input("Ingrese un texto: ")
contador=0
for i in cadena:
    if i in "aeiou":
        contador = contador + 1
print ("La cantidad de vocales son: ", contador)
