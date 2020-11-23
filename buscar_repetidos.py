#palabras = "mama se llevo las pilas que caradura mama se llevo las pilas que tanto duran"

#listapalabras = palabras.split()

#frecuenciapalab = []
#for w in listapalabras:
#    frecuenciapalab.append(listapalabras.count(w))

#print("Cadena\n" + palabras +"\n")
#print("Lista\n" + str(listapalabras) + "\n")
#print("Frecuencias\n" + str(frecuenciapalab) + "\n")
#print("Pares\n" + str(list(zip(listapalabras, frecuenciapalab))))


cadena = input("Escribe lo que quieras: ")
subcadena = ""


for i in cadena.split():
    if subcadena.find(" " + i + " ") >= 0:
         print (i, "esta repetida")
         
    subcadena = subcadena + " " + i + " "
    print (subcadena)