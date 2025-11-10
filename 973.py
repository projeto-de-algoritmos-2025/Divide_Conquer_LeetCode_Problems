import random
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distancia(i):
            return points[i][0]**2 + points[i][1]**2

        def quickselect(esquerda, direita, k_menor):
            if esquerda >= direita:
                return
            indice_pivo = random.randint(esquerda, direita)
            distancia_pivo = distancia(indice_pivo)
            
            points[indice_pivo], points[direita] = points[direita], points[indice_pivo]
            armazena = esquerda
            for i in range(esquerda, direita):
                if distancia(i) < distancia_pivo:
                    points[armazena], points[i] = points[i], points[armazena]
                    armazena += 1
            points[armazena], points[direita] = points[direita], points[armazena]

            if k_menor < armazena:
                quickselect(esquerda, armazena - 1, k_menor)
            elif k_menor > armazena:
                quickselect(armazena + 1, direita, k_menor)

        quickselect(0, len(points) - 1, k)
        return points[:k]
