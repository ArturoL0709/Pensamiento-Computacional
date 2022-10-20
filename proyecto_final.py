"""""
Arturo López García
Proyecto de pensamiento computacional 
"Calculadora química para gases ideales "PV=nRT y vectores"

"""""


from sys import float_repr_style

#Variable 
R=0.08205

#Inicio del programa
def inicio ():
    print("Proyecto_Arturo_López_García_Calculadora")

inicio()

#Menu

ecuacion=int(input("Seleccione la opcioón que desea calcular si es sobtr la ecuación general de los gases nobles ó otra de las opciones disponibles 1.P 2.V 3.n 4.T // calcular neutrones 5 // Suma de vectores 6 // "))

#Ecuación para la presión de un Gas "V"
if ecuacion==1:
    def presion ():
        print("Ingrese los demás datos del problema: 1.n 2.T 3.V")
        n=float(input("Ingresa el número de moles "))
        T=float(input("Ingresa la temperatura en en °C " ))
        v=float(input("Ingresa el volumen en L "))
        P=((n)*(R)*(T+273)/(v))
        print("La presión es:", P )
        return P
    presion()

#Ecuación para el Volumen de un gas "V"

if ecuacion==2:
 def volumen ():
        print("Ingrese los demás datos del problema: 1.n 2.T 3.P")
        n=float(input("Ingresa el número de moles "))
        T=float(input("Ingresa la temperatura en en °C " ))
        P=float(input("Ingresa la presión en atm  "))
        V=((n)*(R)*(T+273)/P)
        print("El volumen es:", V )
        return V
 volumen()

#Ecuación para Numero de moles "n"

if ecuacion==3:
 def num_moles():    
        print("Ingrese los demás datos del problema        : 1.n 2.T 3.P")
        T=float(input("Ingresa la temperatura en en °C " ))
        P=float(input("Ingresa la presión en atm  "))
        V=float(input("Ingresa el volumen en L "))
        n=((P*V)/(R*T+273))
        print("El múmero de moles es:", n )
        return n
 num_moles()

#Funcion de T para temperatura

if ecuacion==4:
    def temperatura ():
        print("Igrese el valor de temperatura en °C para convertir a °K")
        t=float(input("Ingresa la temperatura en °C "))
        k=(t+273)
        print("La temperatura es:",k)
        return k
    temperatura ()

#Calcular numero de neutrones

if ecuacion==5:
    def num_neutrones():
        protones=int(input("Escriba el número de protones de su elemento "))
        masa_atomica=int(input("Escriba la masa atomica de su elemento "))
        neutrones=masa_atomica-protones
        print(f"El número de neutrones es {neutrones}")
        return(neutrones)
    num_neutrones()
    
#Vectores

if ecuacion==6:
    def vectores_suma():
        A=[]
        B=[]
        An=int(input("Introduzca el número de elementos del vector : "))
        for i in range(0, An):
            ele = int(input())
            A.append(ele) 
        Bn=int(input("Introduzca el número de elementos del vector : "))
        for i in range(0, Bn):
            eleb = int(input())
            B.append(eleb) 
        if len(A)==len(B):
            suma=[]
            for i in range(len(A)):
                suma.append (A[1]+B[1])
            print (suma)
            return suma
        else:
            return print("Vectores diferente tamaño, no se puede realizar")
    vectores_suma()

while ecuacion>6 or ecuacion<0:
    print("Reinicie el programa")
    break

    
 #Fin del programa








