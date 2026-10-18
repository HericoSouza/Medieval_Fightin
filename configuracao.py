STATUS_PERSONAGENS = {
    "Guerreiro": {"vida": 150, "mana": 50, "pocao_cura": 3, "pocao_mana": 3, "defesa": 1},
    "Mago": {"vida": 100, "mana": 150, "pocao_cura": 3, "pocao_mana": 3, "defesa": 0},
    "Arqueiro": {"vida": 120, "mana": 80, "pocao_cura": 3, "pocao_mana": 3, "defesa": 0}
}

VALORES_POCOES = {"cura": 55, "mana": 40}

PROGRESSAO = {
    "nivel_maximo": 5,
    "xp_por_nivel": {1: 100, 2: 150, 3: 200, 4: 250},
    "vida_por_nivel": 20,
    "mana_por_nivel": 10,
    "dano_por_nivel": 5,
    "xp_encontros": [35, 50, 75, 125, 95, 130, 240],
    "recuperacao_vida_percentual": 0.10,
    "recuperacao_mana_percentual": 0.10,
    "recuperacao_companheiro_percentual": 0.15
}

DANOS_PERSONAGENS = {
    "Guerreiro": {"basico": (16, 24), "especial": (30, 44), "especial_custo": 20, "habilidade_custo": 0},
    "Mago": {"basico": (12, 25), "especial": (22, 34), "especial_custo": 25, "habilidade": (65, 90), "habilidade_custo": 50},
    "Arqueiro": {"basico": (17, 25), "especial": (32, 44), "especial_custo": 25, "veneno": (4, 8), "habilidade_custo": 0}
}

CONDICOES = {
    "veneno": {"dano_minimo": 4, "dano_maximo": 8, "duracao": 3},
    "sangramento": {"dano_minimo": 4, "dano_maximo": 8, "duracao": 2},
    "congelamento": {"duracao": 1}
}

RECOMPENSAS = {
    "moedas_iniciais": 20,
    "moedas_por_encontro": 0
}
