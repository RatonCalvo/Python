import random
   n=input("ingrese numero de filas: ")
   m=input("ingrese numero de columnas: ")
   b=random.randint(1,6))
   q=input("ingrese el numero de escaleras que quiere: ")
   w=input("ingrese el numero de serpientes que quiere: ")

   def tablero():
      lista = []
      for i in range((n*m)+1):
         i+=0
         lista.append(i)
      return lista 
   algo=tablero()
   print(algo)
   u=input("ingrese numero de jugadores: ")
   def jugadores():
      nombres = []
      for nombre in range(1,u+1):
        g=raw_input("Nombre jugador"+" "+str(nombre)+": ")
        print(g)
        nombres.append(g)
      return nombres 
   nl=jugadores()
   print(nl)
   def casillas_serpiente(w):
     c_s=[]
     i=0
     while i < w :
         g=int(random.randint(1,(n*m)))
         if g not in c_s:
            i+=1
            c_s.append(g)
         return(c_s)
     vu=serpiente(w)
    def casillas_escalera(q,vu):
     c_e=[]
     i=0
     while i < q :
        h=int(random.randint(1,(n*m)+1))
         if h not in c_e and h not in vu:
            i+=1
            c_e.append(h)
       return(c_e)
    ju=escalera(q,vu)
