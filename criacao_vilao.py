def nome_vilão():
    nome_vilão = input("Digite o nome do vilão: ")
    return nome_vilão


def classe_vilão():
    print("Classes disponíveis: Dragão, Bruxo, Goblin.")
    classe_inimigo = input("Digite a classe do vilão: ")

    if classe_inimigo.lower() not in ["dragão", "bruxo", "goblin"]:
        print("Classe inválida. Por favor, escolha entre Dragão, Bruxo ou Goblin.")
        return classe_vilão()

    return classe_inimigo


def criar_vilão():

    nome_inimigo = nome_vilão()
    classe_inimigo = classe_vilão()

    if classe_inimigo.lower() == "dragão":
        vida_vilão = 1000
        ataque_basico_vilão = "Garrada"
        ataque_especial_vilão = "Sopro de fogo"
        habilidade_especial_vilão = "Voo"

    elif classe_inimigo.lower() == "bruxo":
        vida_vilão = 500
        ataque_basico_vilão = "Magia Macabra"
        ataque_especial_vilão = "Necromancia"
        habilidade_especial_vilão = "Reviver Ancião"

    elif classe_inimigo.lower() == "goblin":
        vida_vilão = 400
        ataque_basico_vilão = "Adaga"
        ataque_especial_vilão = "Chamar Amigos"
        habilidade_especial_vilão = "Roubar"

    vilão = {
        "nome": nome_inimigo,
        "classe": classe_inimigo,
        "vida": vida_vilão,
        "ataque_basico": ataque_basico_vilão,
        "ataque_especial": ataque_especial_vilão,
        "habilidade_especial": habilidade_especial_vilão,
        "voo_dragao": False,
        "anciao": False,
        "inimigo_congelado": False,
        "inimigo_envenenado": False,
        "contagem_veneno": 0,
        "condição": False,
        "sangramento": False
    }

    return vilão