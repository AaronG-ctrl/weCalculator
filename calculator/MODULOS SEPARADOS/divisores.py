

def divisores():

	i=1
	x = float(input("Introduce un número: "))
	if x == 0:
		print("El numero introducido no es valido")
	else:	
		while i  <= 12:
			print(x,"/",i,"=", round(x/i,1))
			i = i + 1
			

divisores()	



	   
