from TransformacaoLinear import transformacao_linear

import numpy as np

# Nessa main, use para printar os resultados das funções que construímos na classe TransformaçãoLinear
# Faça questões relacionadas a 2D ou 3D e use o código desenvolvido como base para testar se está
# funcionando perfeitamente.

# -- Translação 2D e 3D (João Victor)

# Transção 2D (João Victor) 
print("--------Translação 2D--------")

ponto2D = [1, 2, 1]  # <- o valor em 2D que você colocará caso professor peça


vetor_translacao2D = [3, 4, 0] # <- O valor da translação que será feita  caso professor peça

print("Vetor 2D: ", ponto2D)

print("dx = ", ponto2D[0], "dy = ",
      ponto2D[1],)
print("vetor_translacao = ", vetor_translacao2D)

print("Transformação linear translação feita:", transformacao_linear.translacao_2d(
    ponto2D, vetor_translacao2D))


print("\n--------Translação 3D--------")

# Translação 3D (João Victor) 
ponto3D = [4, 6, 8, 1] # <- o valor em 3D que você colocará caso professor peça


vetor_translacao3D = [8, 12, 16, 0] # <- O valor da translação que será feita  caso professor peça

print("Ponto3D: ", ponto3D)

print("dx = ", ponto3D[0], "dy = ", ponto3D[1],
      "dz = ", ponto3D[2],)

print("vetor_translacao = ", vetor_translacao3D)

print("Transformação linear translação feita: ", transformacao_linear.translacao_3d(
    ponto3D, vetor_translacao3D))

# Rotação 2D (João Victor)

print("\n--------Rotação 2D--------")

pontorotacao2D = [5, 9, 1] # <- o valor em 2D que você colocará caso professor peça
angulo_rotacao = 90  # <- O valor do ângulo de rotação que será

print("Ponto da rotação2D: ", pontorotacao2D)
print("dx = ", pontorotacao2D[0], "dy = ",
      pontorotacao2D[1], "ângulo = ", angulo_rotacao)
print("Rotação que será feita: ", angulo_rotacao)

print("Transformação linear Rotação2D feita:", transformacao_linear.rotacao_2d(
    pontorotacao2D, angulo_rotacao))


print("\n--------Rotação 3D--------")
# Rotação 3D (João Victor) 


pontorotacao3D = [2, 4, 6] # <- o valor em 3D que você colocará caso professor peça


angulo_rotacao_x = 30 # <- O valor do ângulo de rotação em torno do eixo X que será feito caso professor peça


angulo_rotacao_y = 45 # <- O valor do ângulo de rotação em torno do eixo Y que será feito caso professor peça

angulo_rotacao_z = 60 # <- O valor do ângulo de rotação em torno do eixo Z que será feito caso professor peça


print("Ponto da rotação3D: ", pontorotacao3D)
print("dx = ", pontorotacao3D[0], "dy = ",
      pontorotacao3D[1], "dz = ", pontorotacao3D[2])

print("Ângulos da rotação dos eixos dx, dy e dz: ")
print( "ângulo x = ", angulo_rotacao_x,
      "ângulo y = ", angulo_rotacao_y, "ângulo z = ", angulo_rotacao_z)

print("Novo ponto após sofrer rotações nos eixos x, y e z: ")
print(transformacao_linear.rotacao_3d(
pontorotacao3D, angulo_rotacao_x, angulo_rotacao_y, angulo_rotacao_z))


# Projeção 2D e 3D - Mauricio

# Projeção 2D (Mauricio) 
print("\n--------Projeção 2D--------")
ponto_projecao2D = [4, 3] # <- o valor em 2D que você colocará caso professor peça
print("Ponto original:", ponto_projecao2D)
print("Projeção no eixo X:", transformacao_linear.projection2DX(
    ponto_projecao2D))  
print("Projeção no eixo Y:", transformacao_linear.projection2DY(
    ponto_projecao2D))  

# Projeção 3D (Mauricio) 
print("\n--------Projeção 3D--------")
ponto_projecao3D = [2, 3, 4] # <- o valor em 3D que você colocará caso professor peça
print("Ponto original:", ponto_projecao3D)
print("Projeção no eixo X:", transformacao_linear.projection3DX(
    ponto_projecao3D)) 
print("Projeção no eixo Y:", transformacao_linear.projection3DY(
    ponto_projecao3D))  
print("Projeção no eixo Z:", transformacao_linear.projection3DZ(
    ponto_projecao3D)) 


# =========================================================================
# -------------------->  CISALHAMENTO 2D (Pablo José)  <-------------------
# =========================================================================
print("\n--------Cisalhamento 2D--------")
ponto_cisalhamento2D = [2, 3] # <- o valor em 2D que você colocará caso professor peça
kx, ky = 1, 0
print("Ponto original:", ponto_cisalhamento2D, "| kx =", kx, "ky =", ky)
print("Cisalhamento:", transformacao_linear.shearing(
    ponto_cisalhamento2D, kx, ky))  

kx, ky = 0, 2
print("Ponto original:", ponto_cisalhamento2D, "| kx =", kx, "ky =", ky)
print("Cisalhamento:", transformacao_linear.shearing(
    ponto_cisalhamento2D, kx, ky))  

kx, ky = 1, 2
print("Ponto original:", ponto_cisalhamento2D, "| kx =", kx, "ky =", ky)
print("Cisalhamento:", transformacao_linear.shearing(
    ponto_cisalhamento2D, kx, ky))  
# ------------------------->  FIM DO CISALHAMENTO  <--------------------------

# ------------------------->       Reflexão        <--------------------------

# Reflexão2D (Matheus) 
print("\n--------Reflexão 2D--------")
v2 = [3, 2, 1] # <- o valor em 2D que você colocará caso professor peça
v3 = [3, 2, 4, 1] # <- o valor em 3D que você colocará caso professor peça

print("Reflexão 2D no eixo X:", transformacao_linear.reflection2DX(v2))
print("Reflexão 2D no eixo Y:", transformacao_linear.reflection2DY(v2))

# Reflexão 3D (Matheus) 

print("\n--------Reflexão3D--------")

print("Reflexão 3D no eixo X:", transformacao_linear.reflection3DX(v3))
print("Reflexão 3D no eixo Y:", transformacao_linear.reflection3DY(v3))
print("Reflexão 3D no eixo Z:", transformacao_linear.reflection3DZ(v3))
