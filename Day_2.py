# calcular el total de la propina de una cuenta de restaurante teniendo en cuenta el total de personas que llegan a la mesa,
# el total de la cuenta y el tipo de propina que se le va a aplicar (15% o 18% o 20%) y el total de la cuenta con la propina aplicada
# ademas de mostrar el total a pagar por cada persona 

cuenta = float(input("Ingrese el total de la cuenta: "))
cuenta_personas = int(input("Ingrese el total de personas que llegan a la mesa: "))
cuenta_propina = float(input("Ingrese el tipo de propina que se le va a aplicar (15% o 18% o 20%): "))
cuenta_total = cuenta + (cuenta * cuenta_propina / 100) + int(cuenta_personas)
print("El total de la cuenta con la propina aplicada es: " + str(cuenta_total))
print("El total a pagar por cada persona es: " + str(cuenta_total / cuenta_personas))
