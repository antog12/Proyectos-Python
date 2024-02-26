nombre=input("Nombre del empleado: ")
ingresos=input("Cuanto ha vendido este mes?: ")
ingresos=float(ingresos)
comisiones=ingresos*0.13
comisiones=round(comisiones,2)

print(f"A {nombre}, por la venta de {ingresos} euros, le corresponde en comisiones: {comisiones} euros")