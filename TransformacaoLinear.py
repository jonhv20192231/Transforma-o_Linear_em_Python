
import numpy as np

# -- Translação 2D e 3D (João Victor)


class transformacao_linear:
    """
    Classe para realizar transformações lineares em 2D e 3D.
    """

    @staticmethod
    def translacao_2d(ponto, vetor_translacao):
        """
        Realiza a translação de um ponto em 2D.

        :param ponto: Lista ou array com as coordenadas do ponto (x, y).
        :param vetor_translacao: Lista ou array com o vetor de translação (dx, dy).
        :return: Novo ponto após a translação.
        """
        # ponto vai usar biblioteca numpy para fazer a soma, onde terá as coordenadas como array ou lista
        ponto = np.array(ponto)
        # Vetor translação irá usar a biblioteca numpy, com array ou lista pra fazer a translação
        vetor_translacao = np.array(vetor_translacao)
        execucaodatranslacao = ponto + vetor_translacao
        return execucaodatranslacao

    @staticmethod
    def translacao_3d(ponto, vetor_translacao):
        """

        Seguirá a mesma lógica, contudo agora estaremos trabalhando com 3D.

        """
        ponto = np.array(ponto)
        vetor_translacao = np.array(vetor_translacao)
        execucaodatranslacao = ponto + vetor_translacao
        return execucaodatranslacao


ponto2D = [1, 2]  # <- o valor em 2D que você colocará caso professor peça
# <- O valor da translação que será feita  caso professor peça
vetor_translacao2D = [3, 4]

print(transformacao_linear.translacao_2d(
    ponto2D, vetor_translacao2D))  # Saída: [4 6]


ponto3D = [4, 6, 8]  # <- o valor em 3D que você colocará caso professor peça
# <- O valor da translação que será feita  caso professor peça
vetor_translacao3D = [8, 12, 16]


print(transformacao_linear.translacao_3d(
    ponto3D, vetor_translacao3D))  # Saída: [12 18 24]
