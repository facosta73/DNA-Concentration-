print("Cálculo de concentración de DNA genómico")

absorbancia_dna=float(input("Por favor, introducir absorbacia a 260nm: "))
factor_dilucion=int(input("Ingrese el factor de dilución: "))

def calculo_concentracion(abs_dna_260, f_dilucion):

	print (abs_dna_260*50*f_dilucion)
	
print("La concentración de su DNA es: ")
calculo_concentracion(absorbancia_dna,factor_dilucion)


print("ng/uL")
print("ug/mL")




