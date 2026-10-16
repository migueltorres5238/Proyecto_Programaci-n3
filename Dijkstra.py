"""
TItulo: Algoritmo de Dijkstra
Nombre completo: Miguel Angel Torres Monroy
Fecha de Entrega: 15 de octubre del 2026
Descripción: Se implemento el algoritmo dijkstra para encontrar la ruta mas corta con ponderaciones.
"""

# Clase de Nodo
class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vecinos = {}

    # Función para guardad vecinos y peso
    def agregar_vecino(self, vecino, peso):
        self.vecinos[vecino] = peso

# Clase para la creación de Grafo
class Grafo:
    def __init__(self):
        self.nodos = {}

    def agregar_nodo(self, nombre):
        if nombre not in self.nodos:
            self.nodos[nombre] = Nodo(nombre)

    def agregar_arista(self, origen, destino, peso):
        self.agregar_nodo(origen)
        self.agregar_nodo(destino)
        self.nodos[origen].agregar_vecino(destino, peso)
        self.nodos[destino].agregar_vecino(origen, peso)


    def dijkstra(self, inicio, destino):
        distancias = {}
        anteriores = {}
        visitados = set()

        for nombre in self.nodos:
            distancias[nombre] = float("inf")
            anteriores[nombre] = None

        distancias[inicio] = 0

        while len(visitados) < len(self.nodos):
            # Buscar el nodo más cercano
            nodo_actual = None
            menor_distancia = float("inf")

            for nombre in self.nodos:

                if nombre not in visitados:

                    if distancias[nombre] < menor_distancia:
                        menor_distancia = distancias[nombre]
                        nodo_actual = nombre

            if nodo_actual is None:
                break

            # Si llegamos al destino, terminamos
            if nodo_actual == destino:
                break

            visitados.add(nodo_actual)

            # Revisar vecinos
            nodo = self.nodos[nodo_actual]

            for vecino, peso in nodo.vecinos.items():

                nueva_distancia = (
                    distancias[nodo_actual] + peso
                )

                if nueva_distancia < distancias[vecino]:

                    distancias[vecino] = nueva_distancia
                    anteriores[vecino] = nodo_actual

        # Construir el camino
        camino = []
        actual = destino

        while actual is not None:
            camino.append(actual)
            actual = anteriores[actual]

        camino.reverse()
        return distancias[destino], camino

red = Grafo()

# Red de estaciones (el peso son minutos de viaje)
red.agregar_arista("A", "B", 4)
red.agregar_arista("A", "C", 2)
red.agregar_arista("B", "C", 5)
red.agregar_arista("B", "D", 10)
red.agregar_arista("C", "E", 3)
red.agregar_arista("E", "D", 4)
red.agregar_arista("D", "F", 11)
red.agregar_arista("E", "F", 9)

inicio = "A"
destino = "F"

costo, ruta = red.dijkstra(inicio, destino)

if costo is None:
    print("No hay ruta entre", inicio, "y", destino)
else:
    print("Ruta mas corta de", inicio, "a", destino + ":", " -> ".join(ruta))
    print("Costo total:", costo)

    # Mostrar el paso por cada estacion
    print("\nRecorrido paso a paso:")
    suma = 0
    for i in range(len(ruta) - 1):
        a = ruta[i]
        b = ruta[i + 1]
        peso = red.nodos[a].vecinos[b]
        suma += peso
        print(a, "->", b, "Costo:", peso, "Suma:", suma)