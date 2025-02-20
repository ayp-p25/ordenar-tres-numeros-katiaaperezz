"""
Ordenar tres números
"""


# Entradas
numero1 = int(input("Primer número: "))
numero2 = int(input("Segundo número: "))
numero3 = int(input("Tercer número: "))

# Proceso
if numero1 >= numero2  and numero3 >= numero1: 
    resultado = str(numero3) + " " + str(numero1) + " " + str(numero2)
elif numero1 >= numero2 and numero1 <= numero3:
    resultado = str(numero3) + " " + str(numero1) + " " + str(numero2)
elif numero1 <= numero2 and numero2 <= numero3: 
    resultado = str(numero3) + " " + str(numero2) + " " + str(numero1) 
elif numero2 >= numero3 and numero3 >= numero1:
    resultado = str(numero2) + " " + str(numero3) + " " + str(numero1)          
elif numero2 >= numero3 and numero1 <= numero3:
    resultado = str(numero2) + " " + str(numero1) + " " + str(numero3)
elif numero1 >= numero2 and numero2 >= numero3:
    resultado = str(numero1) + " " + str(numero2) + " " + str(numero3)
elif numero3 >= numero2 and numero2 >= numero1:
    resultado = str(numero3) + " " + str(numero2) + " " + str(numero1)
elif numero1 >= numero3 and numero2 <= numero3: 
    resultado = str(numero1) + " " + str(numero3) + " " + str(numero2)  
elif numero2 >= numero1 and numero1 >= numero3: 
    resultado= str(numero2) + " " + str(numero1) + " " + str(numero3)  
# Salidas
print(resultado)
