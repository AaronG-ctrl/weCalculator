from colorama import init, Fore, Back, Style

def suma():
	print("Usted ha seleccionado",Fore.GREEN ,Style.BRIGHT,"SUMAR",Style.RESET_ALL)
	print("")
	x1 = float(input("Introduce un número: "))
	x2 = float(input("Introduce otro número: "))
	print("")
	print("El resultado de su SUMA es :", Fore.GREEN ,Style.BRIGHT,x1 + x2,Style.RESET_ALL)


def resta():
	print("Usted ha seleccionado",Fore.GREEN ,Style.BRIGHT ,"RESTAR",Style.RESET_ALL)
	print("")
	x1 = float(input("Introduce un número: "))
	x2 = float(input("Introduce otro número: "))
	print("")
	print("El resultado de su RESTA es :" ,Fore.GREEN ,Style.BRIGHT,x1 - x2,Style.RESET_ALL)


def multi():
	print("Usted ha seleccionado",Fore.GREEN ,Style.BRIGHT,"MULTIPLICAR",Style.RESET_ALL)
	print("")
	x1 = float(input("Introduce un número: "))
	x2 = float(input("Introduce otro número: "))
	print("")
	print("El resultado de su MULITPLICACIÓN es :",Fore.GREEN ,Style.BRIGHT,x1 * x2,Style.RESET_ALL)

def divi():
	print("Usted ha seleccionado",Fore.GREEN ,Style.BRIGHT, "DIVIDIR",Style.RESET_ALL)
	print("")
	x1 = float(input("Introduce un número: "))
	x2 = float(input("Introduce otro número: "))
	print("")	
	if x1 == 0 or x2 == 0:
		print(Fore.RED , Style.BRIGHT,"La operación introducida no es valida",Style.RESET_ALL)
		print("")
	else:
		print("El resultado de su DIVISIÓN es :",Fore.GREEN ,Style.BRIGHT ,x1 / x2,Style.RESET_ALL)

def poten():
	print("Usted ha seleccionado",Fore.GREEN ,Style.BRIGHT,"POTENCIA DE UN NÚMERO",Style.RESET_ALL)
	print("")
	x1 = float(input("Introduce la base: "))
	x2 = float(input("Introduce el exponente: "))
	print("")
	print("El resultado de su POTENCIA es :",Fore.GREEN ,Style.BRIGHT ,x1 ** x2,Style.RESET_ALL)

def divisores():
	print("Usted ha seleccionado",Fore.GREEN ,Style.BRIGHT,"DIVISORES",Style.RESET_ALL)
	print("")
	i=1
	x = float(input("Introduce un número: "))
	print("")
	if x == 0:
		print(Fore.RED , Style.BRIGHT,"El numero introducido no es valido",Style.RESET_ALL)
	else:	
		while i  <= 12:
			if x % i == 0:
				print(x,"/",i,"=",Fore.GREEN ,Style.BRIGHT, round(x/i,1),Style.RESET_ALL)
				i = i + 1
			else:
				print(x,"/",i,"=",Fore.RED , Style.BRIGHT, round(x/i,1),Style.RESET_ALL)
				i = i + 1
					

def tablas():
	print("Usted ha seleccionado" ,Fore.GREEN ,Style.BRIGHT, "TABLAS DE MULTIPLICAR",Style.RESET_ALL)
	print("")
	x = float(input("Introduce un número: "))
	xx = 1
	while xx <= 12:
		print(x ,"*",xx ,"=",Fore.GREEN ,Style.BRIGHT, x*xx ,Style.RESET_ALL)
		xx = xx + 1			







