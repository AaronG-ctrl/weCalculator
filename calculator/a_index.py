from a_modu import *
from colorama import init, Fore, Back, Style
import sys
import os
init()
i=1
exe=1
respuesta="si"
#---------------------------------------------------------------------------------------------------------------------------#

print(Fore.BLUE ,Style.BRIGHT,"#########################################")
print(Fore.BLUE ,Style.BRIGHT,"############", Fore.WHITE ,Style.BRIGHT,"Bienvenido" ,Fore.BLUE ,Style.BRIGHT, "#############")
print(Fore.BLUE ,Style.BRIGHT,"#########################################", Style.RESET_ALL)
print("")

while respuesta=="si":
		print ( ''' 
	CALCULADORA BASICA ----->

1) SUMAR
2) RESTAR
3) MULTIPLICAR
4) DIVIDIR
5) POTENCIAS
6) DIVISORES
7) TABLAS DE MULTIPLICAR
8) SALIR''')

		print("")
		opcion = int(input("OPCION: "))
		print("")

		if opcion == 1:
			suma() 
		elif opcion == 2:
			resta()
		elif opcion == 3:
			multi()
		elif opcion == 4:
			divi()
		elif opcion == 5:
			poten()
		elif opcion == 6:
			divisores()
		elif opcion == 7:
			tablas()
		elif opcion == 8:
			print("Has seleccionado SALIR")
			print("Cerrando programa...")
			sys.exit()
		else:
			print(Fore.RED , Style.BRIGHT,"ERROR:",Style.RESET_ALL, "La opción introducida no es valida")
			print(" Inténtelo de nuevo")	

		print("")	
		respuesta=input("Desea continuar haciendo operaciones? [si/no]:")	
		os.system("cls")




