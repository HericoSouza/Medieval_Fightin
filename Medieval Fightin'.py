import math
import random
import os
import time

import criacao_vilao
import criacao_personagem
import combate
import oanciao


# ZONA DAS FUNÇÕES - INÍCIO

def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# ZONA DAS FUNÇÕES - FIM


# GAME START

personagem = criacao_personagem.criar_personagem()

vilão = criacao_vilao.criar_vilão()

ancião = oanciao.criar_anciao()

limpar_tela()

# Inicia o combate
combate.combate(personagem, vilão, ancião)