from typing import List

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        prefixo = [0]
        for numero in nums:
            prefixo.append(prefixo[-1] + numero)

        def ordena_e_conta(inicio, fim):
            if fim - inicio <= 1:
                return 0
            meio = (inicio + fim) // 2
            contagem = ordena_e_conta(inicio, meio) + ordena_e_conta(meio, fim)
            
            j = k = meio
            for esquerda in prefixo[inicio:meio]:
                while k < fim and prefixo[k] - esquerda < lower:
                    k += 1
                while j < fim and prefixo[j] - esquerda <= upper:
                    j += 1
                contagem += j - k

            prefixo[inicio:fim] = sorted(prefixo[inicio:fim])
            return contagem

        return ordena_e_conta(0, len(prefixo))
