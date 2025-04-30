def ejercicio():
    
    f = int(input("Fecha (DDMMAAAA): "))
    
    print("Dia: ",int(f/1000000)," / Mes: ",int(f/10000)-int(f/1000000)*100," / Año: ",f-int(f/10000)*10000)

ejercicio()