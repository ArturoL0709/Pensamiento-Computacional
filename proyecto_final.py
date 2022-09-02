"""""
Proyecto de pensamiento computacional 
"Calculadora química para gases ideales "PV=nRT"

"""""
from tkinter import Y


R=0.08205


ecuacion=int(input("Seleccione un valor descnocido para la ecuación del gas ideal 1.P 2.V 3.n 4.T "))
#Ecuación para la presión de un Gas "V"
if ecuacion==1:
    print("Ingrese los demás datos del problema: 1.n 2.T 3.V")
    n=float(input("Ingresa el número de moles "))
    T=float(input("Ingresa la temperatura en en °C " ))
    v=float(input("Ingresa el volumen en L "))
    P=((n)*(R)*(T+273)/(v))
    print("La presión es:", P )
else:
    print("Valor no valido, reinicie el programa")
#Ecuación para el Volumen de un gas "V"
if ecuacion==2:
 print("Ingrese los demás datos del problema: 1.n 2.T 3.P")
 n=float(input("Ingresa el número de moles "))
 T=float(input("Ingresa la temperatura en en °C " ))
 P=float(input("Ingresa la presión en atm  "))
 V=((n)*(R)*(T+273)/P)
 print("El volumen es:", V )

#Ecuación para Numero de moles "n"
if ecuacion==3:
 print("Ingrese los demás datos del problema: 1.n 2.T 3.P")
 T=float(input("Ingresa la temperatura en en °C " ))
 P=float(input("Ingresa la presión en atm  "))
 V=float(input("Ingresa el volumen en L "))
 n=((P*V)/(R*T+273))
 print("El múmero de moles es:", n )

#Funcion de T para temperatura

def suma(a=273+Y):
    return (a+Y)


 
 














