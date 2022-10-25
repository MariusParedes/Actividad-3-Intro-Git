# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
num1=int(input("Ingrese número 1: "))
num2=int(input("Ingrese número 2: "))
num3=int(input("Ingrese número 3: "))
if (num1 > num2) and (num1 > num3):
    print("El número mayor es el número uno")
elif (num2 > num1) and (num2 >num3):
    print("El número mayor es el número dos")
elif (num3 > num1) and (num3>num2):
    print("El número mayor es el número tres")
else:
    print("Los 3 números son iguales")
