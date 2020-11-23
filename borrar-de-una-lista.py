L = [1, 2, 3, 4, 5, 6]

def eliminarEnLista(L):
    n=int(input("Ingrese el numero que desea eliminar de la lista: "))
    try:
        L.remove(n)
        print(L)
    except ValueError:
        print('{} no se encuentra en la lista'.format(n))
        
eliminarEnLista(L) 