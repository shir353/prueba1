#Solicitar al usuario ingrese supeso en kilogrammos y su estatura en metros,luego calcular su IMC y mostrar 
#el IMC utilizando la formula IMC= peso/altura 2
# mostrar los reultados de IMC
#Clasificar el estado de peso de la persona segun la OMS
#RAngo de IMC clasificacion
# IMC  menos a 18.5 peso bajo
# IMC 18.5 a 25 peso normal 
# IMC 25 a 29.9 sobreperso
# IMC 30 o mas Obesidad

peso  = float(input("Ingrese su peso en kilogramos:"))
altura = float(input("Ingrese su estatura en metros:"))

IMC = peso/ (altura**2)

if IMC <18.5:
    print("BAjo Peso")
    
elif IMC <=18.5 and IMC < 25:
    print("peso Nomral")

elif IMC >= 25.0 and IMC< 30:    
    print("Sobrepeso")
    
elif IMC >=30:
    print("Obesidad")
