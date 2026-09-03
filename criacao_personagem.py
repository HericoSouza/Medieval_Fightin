def nome_personagem():
    nome = input("Digite o nome do personagem: ")
    return nome


def classe_personagem():
    print("Classes disponíveis: Guerreiro, Mago, Arqueiro.")
    classe = input("Digite a classe do personagem: ")

    if classe.lower() not in ["guerreiro", "mago", "arqueiro"]:
        print("Classe inválida. Por favor, escolha entre Guerreiro, Mago ou Arqueiro.")
        return classe_personagem()

    return classe


def criar_personagem():

    nome_principal = nome_personagem()
    classe_principal = classe_personagem()

    if classe_principal.lower() == "guerreiro":
        vida = 150
        mana = 50
        ataque_basico = "espada"
        ataque_especial = "golpe de fúria"
        habilidade_especial = "modo berserker"

    elif classe_principal.lower() == "mago":
        vida = 100
        mana = 150
        ataque_basico = "bola de fogo"
        ataque_especial = "raio de gelo"
        habilidade_especial = "meteoro arcano"

    elif classe_principal.lower() == "arqueiro":
        vida = 120
        mana = 80
        ataque_basico = "arco e flecha"
        ataque_especial = "chuva de flechas"
        habilidade_especial = "envenenamento"

    personagem = {
        "nome": nome_principal,
        "classe": classe_principal,
        "vida": vida,
        "mana": mana,
        "contagem_berserker": 0,
        "ataque_basico": ataque_basico,
        "ataque_especial": ataque_especial,
        "habilidade_especial": habilidade_especial,
        "modo_berserker": False,
        "personagem_sangramento": False,
        "contagem_sangramento": False,
        "condição": False,
        "pocao_cura": 3,
        "pocao_mana": 3
    }

    return personagem