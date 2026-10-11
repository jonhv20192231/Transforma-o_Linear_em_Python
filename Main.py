

from TransformacaoLinear import transformacao_linear

import numpy as np

# Nessa main, use para printar os resultados das funções que construímos na classe TransformaçãoLinear
# Faça questões relacionadas a 2D ou 3D e use o código desenvolvido como base para testar se está
# funcionando perfeitamente.

# -- Translação 2D e 3D (João Victor)

# -- Translação 2D -----------
ponto2D = [1, 2]   #<----- Altere os valores aqui caso o professor peça 
vetor_translacao2D = [3, 4] #<----- Altere os valores aqui caso o professor peça
print("--------translação em 2D dx e dy:----------------")
print("\n")
print("Ponto original: ", ponto2D)
print("Vetor de translação: ", vetor_translacao2D)
print("Transação em 2D:", transformacao_linear.translacao_2d(
    ponto2D, vetor_translacao2D))  # Saída: [4 6]


# -- Translação 3D -----------
ponto3D = [4, 6, 8]
vetor_translacao3D = [8, 12, 16]

print("--------translação em 3D dx, dy e dz:----------------")
print("\n")
print("Ponto original: ", ponto3D)
print("Vetor de translação: ", vetor_translacao3D)
print("Transação em 3D:", transformacao_linear.translacao_3d(
    ponto3D, vetor_translacao3D))  # Saída: [12 18 24]
