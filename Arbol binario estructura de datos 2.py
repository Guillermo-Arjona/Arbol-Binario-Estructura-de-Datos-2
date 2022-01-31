import os

class node():
    def __init__(self, dato):
        self.left = None
        self.right = None
        self.dato = dato

class arbol():
    def __init__(self):
        self.root = None
        
    def insert(self, a, dato):
        if a == None:
            a = node(dato)
        else:
            d = a.dato
            if dato < d:
                a.left = self.insert(a.left, dato)
            else:
                a.right = self.insert(a.right, dato)
        return a

    def Enorden(self, a):
        if a == None:
            return None
        else:
            self.Enorden(a.left)
            print(a.dato)
            self.Enorden(a.right)

    def Preorden(self, a):
        if a == None:
            return None
        else:
            print(a.dato)
            self.Preorden(a.left)
            self.Preorden(a.right)

    def Postorden(self, a):
        if a == None:
            return None
        else:
            self.Postorden(a.left)
            self.Postorden(a.right)
            print(a.dato)

    def buscar(self, dato, a):
        if a == None:
            return None
        else:
            if dato == a.dato:
                return a.dato
            else:
                if dato < a.dato:
                    return self.buscar(dato, a.left)
                else:
                    return self.buscar(dato, a.right)

tree = arbol()

while True:
    os.system("cls")
    print("Arbol Binario")
    opc = input("\n1.-Digite el nodo \n2.-En orden \n3.-Pre orden \n4.-Post orden \n5.-Buscar nodo \n6.-Salir \n")

    if opc == '1':
        nodo = input("\nEscriba el nodo -> ")
        if nodo.isdigit():
            nodo = int(nodo)
            tree.root = tree.insert(tree.root, nodo)
        else:
            print("\nSolo se le permite digitos...")
    elif opc == '2':
        if tree.root == None:
            print("El orden es")
        else:
            tree.Enorden(tree.root)
    elif opc == '3':
        if tree.root == None:
            print("El pre orden es")
        else:
            tree.Preorden(tree.root)
    elif opc == '4':
        if tree.root == None:
            print("Vacio")
        else:
            tree.Postorden(tree.root)
    elif opc == '5':
        nodo = input("\nIngresa el nodo a buscar -> ")
        if nodo.isdigit():
            nodo = int(nodo)
            if tree.buscar(nodo, tree.root) == None:
                print("\nNodo no existente...")
            else:
                print("\nNodo encontrado -> ",tree.buscar(nodo, tree.root), " si existe...")
        else:
            print("\nIngresa solo digitos...")        
    elif opc == '6':
        print("\nSaliendo...\n")
        os.system("pause")
        break
    else:
        print("\nElige una opcion correcta...")
    print()
    os.system("pause")

print()