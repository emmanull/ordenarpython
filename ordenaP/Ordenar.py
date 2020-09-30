
oracion=["El","perro","come"] 
des = []
ordenada = []

archivo = open("datos.txt","r")
#paso 3: vamos a leer los datos del txt
for i in archivo.readlines():
   des.append(i)
print("                    Frase del txt              ")
print(des)



for item in oracion:
    for item2 in des:
        if item in item2:
            ordenada.append(item)

            
print("                       Lista ordenada                 ")
print(ordenada)

