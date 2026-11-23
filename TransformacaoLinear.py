# Importei na biblioteca python, o numpy, ou seja, não será necessário o uso da classe Matrix e Vector
# Pois a própria biblioteca já tem, poupando na construção das demais matrizes transformação linear.
import numpy as np
# Foi utilizado a biblioteca numpy, para ser mais prático trabalhar com Álgebra Linear
# Sem precisa reutilizar as classes Matrix e Vector, pois a própria biblioteca já tem, poupando
# na construção das matrizes transformação linear.




class transformacao_linear:

    @staticmethod

    def translacao_2d(ponto, vetor_translacao):

        ponto_homogeneo = np.array([ponto[0], ponto[1], 1])

        dx, dy = vetor_translacao[0], vetor_translacao[1]
 
        matriz_translacao = np.array([
            [1, 0, dx],
            [0, 1, dy],
            [0, 0, 1]
        ])

        resultado = np.dot(matriz_translacao, ponto_homogeneo)

        return resultado[:2]

    @staticmethod
    def translacao_3d(ponto, vetor_translacao):

        ponto_homogeneo = np.array([ponto[0], ponto[1], ponto[2], 1])


        dx, dy, dz = vetor_translacao[0], vetor_translacao[1], vetor_translacao[2]

        matriz_translacao = np.array([
            [1, 0, 0, dx],
            [0, 1, 0, dy],
            [0, 0, 0, 1]
        ])

        resultado = matriz_translacao @ ponto_homogeneo
     
        return resultado [:3]

    @staticmethod
  
    def rotacao_2d(ponto_homogeneo, angulo):
     
        angulo_rad = np.radians(angulo)
      
        c, s = np.cos(angulo_rad), np.sin(angulo_rad)
       
        matriz_rotacao = np.array([[c, -s, 0],
                                    [s, c, 0],
                                    [0, 0, 1]])
        ponto = np.array(ponto_homogeneo)
        
        
        execucaodarotacao = matriz_rotacao @ ponto

        return execucaodarotacao
  

    @staticmethod
    def rotacao_3d(ponto_homogeneo, angulo_x, angulo_y, angulo_z):

        angulo_x_rad = np.radians(angulo_x)
        angulo_y_rad = np.radians(angulo_y)
        angulo_z_rad = np.radians(angulo_z)

   
        cx, sx = np.cos(angulo_x_rad), np.sin(angulo_x_rad)
        cy, sy = np.cos(angulo_y_rad), np.sin(angulo_y_rad)
        cz, sz = np.cos(angulo_z_rad), np.sin(angulo_z_rad)


  
        Rx = np.array([
            [1, 0, 0, 0],
            [0, cx, -sx, 0],
            [0, sx, cx, 0],
            [0, 0, 0, 1]
        ])
    
        Ry = np.array([
            [cy, 0, sy, 0],
            [0, 1, 0, 0],
            [-sy, 0, cy, 0],
            [0, 0, 0, 1]
        ])

        Rz = np.array([[cz, -sz, 0, 0],
                       [sz, cz, 0, 0],
                       [0, 0, 1, 0],
                       [0, 0, 0, 1]])

        ponto = np.array(ponto_homogeneo) 

        if len(ponto) == 3:
            ponto = np.append(ponto, 1.0)

        executarotacao = Rz @(Ry @ (Rx @ ponto))
        return executarotacao


    @staticmethod
    def _projetar_no_eixo(vetor, dimensao, matriz_projecao):
  
        coordenadas = np.asarray(vetor, dtype=float).reshape(-1)
        if coordenadas.size not in (dimensao, dimensao + 1):
            raise ValueError(
                f"Esperado um vetor com {dimensao} coordenadas cartesianas "
                f"ou {dimensao + 1} coordenadas homogêneas."
            )

   
        ponto_homogeneo = np.append(coordenadas[:dimensao], 1.0)
        resultado = matriz_projecao @ ponto_homogeneo
        return resultado[:dimensao]

    @staticmethod
    def projection2DX(vector):
        matriz = np.array([
            [1, 0, 0],
            [0, 0, 0],
            [0, 0, 1]
        ], dtype=float)
        return transformacao_linear._projetar_no_eixo(vector, 2, matriz)

    @staticmethod
    def projection2DY(vector):

        matriz = np.array([
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ], dtype=float)
        return transformacao_linear._projetar_no_eixo(vector, 2, matriz)

    @staticmethod
    def projection3DX(vector):

        matriz = np.array([
            [1, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 1]
        ], dtype=float)
        return transformacao_linear._projetar_no_eixo(vector, 3, matriz)

    @staticmethod
    def projection3DY(vector):

        matriz = np.array([
            [0, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 1]
        ], dtype=float)
        return transformacao_linear._projetar_no_eixo(vector, 3, matriz)

    @staticmethod
    def projection3DZ(vector):
  
        matriz = np.array([
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ], dtype=float)
        return transformacao_linear._projetar_no_eixo(vector, 3, matriz)


    @staticmethod
    def shearing(vector, kx, ky):

        coordenadas = np.asarray(vector, dtype=float).reshape(-1)
        if coordenadas.size not in (2, 3):
            raise ValueError(
                "Esperado um vetor com 2 coordenadas cartesianas "
                "ou 3 coordenadas homogêneas."
            )

     
        ponto_homogeneo = np.append(coordenadas[:2], 1.0)
   
        matriz_cisalhamento = np.array([
            [1, kx, 0],
            [ky, 1, 0],
            [0, 0, 1]
        ], dtype=float)
        resultado = matriz_cisalhamento @ ponto_homogeneo
        return resultado[:2]
  
    def reflection2DX(vector):
        matrix = [
            [1, 0, 0],
            [0, -1, 0],
            [0, 0, 1]
        ]

        vt = []

        for i in range(3):
            somatorio = 0

            for j in range(3):
                somatorio += matrix[i][j] * vector[j]

            vt.append(somatorio)

        return vt

    def reflection2DY(vector):
        matrix = [
            [-1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ]

        vt = []

        for i in range(3):
            somatorio = 0

            for j in range(3):
                somatorio += matrix[i][j] * vector[j]

            vt.append(somatorio)

        return vt

    def reflection3DX(vector):
        matrix = [
            [1, 0, 0, 0],
            [0, -1, 0, 0],
            [0, 0, -1, 0],
            [0, 0, 0, 1]
        ]

        vt = []

        for i in range(4):
            somatorio = 0

            for j in range(4):
                somatorio += matrix[i][j] * vector[j]

            vt.append(somatorio)

        return vt

    def reflection3DY(vector):
        matrix = [
            [-1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, -1, 0],
            [0, 0, 0, 1]
        ]

        vt = []

        for i in range(4):
            somatorio = 0

            for j in range(4):
                somatorio += matrix[i][j] * vector[j]

            vt.append(somatorio)

        return vt

    def reflection3DZ(vector):
        matrix = [
            [-1, 0, 0, 0],
            [0, -1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ]

        vt = []

        for i in range(4):
            somatorio = 0

            for j in range(4):
                somatorio += matrix[i][j] * vector[j]

            vt.append(somatorio)

        return vt









