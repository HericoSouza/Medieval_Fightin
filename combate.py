import math
import random
import os
import time

import condicao
import oanciao


# LIMPEZA DE TELA - INICIO

def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# LIMPEZA DE TELA - FIM


def turno(personagem, alvo):

    ataque_basico = personagem["ataque_basico"]
    ataque_especial = personagem["ataque_especial"]
    habilidade_especial = personagem["habilidade_especial"]
    pocao_cura = personagem["pocao_cura"]
    pocao_mana = personagem["pocao_mana"]

    if personagem["modo_berserker"] == True:
        print(
            f"Você está com Modo Berserker Ativado! "
            f"Seu golpe de fúria causa mais dano por "
            f"{personagem['contagem_berserker']} golpes!"
        )

    print("\nEscolha sua ação:")
    print(f"1. Ataque Básico - Recupera 20 de Mana: {ataque_basico}")
    print(f"2. Ataque Especial - Custa 30 de Mana: {ataque_especial}")
    print(f"3. Habilidade Especial - 3 Usos: {habilidade_especial}")
    print(f"4. Poção de Cura - Cura 100 de vida: {pocao_cura}")    
    print(f"5. Poção de Mana - Cura 50 de Mana: {pocao_mana}")        
    print("====================================================")
    print(f"Vida atual: {personagem['vida']}")
    print(f"Mana atual: {personagem['mana']}")
    print("====================================================")

    escolha = input("Digite o número da ação desejada: ")

    # ATAQUE BÁSICO

    if escolha == "1":

        if ataque_basico == "espada":
            dano = random.randint(15, 25)

        elif ataque_basico == "bola de fogo":
            dano = random.randint(10, 30)

        elif ataque_basico == "arco e flecha":
            dano = random.randint(20, 25)

        personagem["mana"] += 20

        time.sleep(8)
        limpar_tela()

        print(f"\nVocê usou {ataque_basico}!")
        print(f"Causou {dano} de dano.")
        print("Mana recuperada: +20")
        print(f"Mana atual: {personagem['mana']}")

        return dano

    # ATAQUE ESPECIAL

    elif escolha == "2":

        if personagem["mana"] < 30:
            print("\nVocê não possui mana suficiente!")
            time.sleep(8)
            limpar_tela()
            return turno(personagem, alvo)

        personagem["mana"] -= 30

        if ataque_especial == "golpe de fúria":

            if personagem["modo_berserker"] == True:

                dano = random.randint(70, 100)

                personagem["contagem_berserker"] -= 1

                if personagem["contagem_berserker"] <= 0:

                    personagem["contagem_berserker"] = 0
                    personagem["modo_berserker"] = False

                    print(
                        "Você sente a Fúria Berserk saindo "
                        "de seu corpo. Seu ataque voltou "
                        "ao dano normal!"
                    )

            else:

                dano = random.randint(30, 50)

        elif ataque_especial == "raio de gelo":

            dano = random.randint(25, 35)

            alvo["inimigo_congelado"] = True
            alvo["condição"] = True

            print("O inimigo foi congelado!")

        elif ataque_especial == "chuva de flechas":

            dano = random.randint(45, 50)

        time.sleep(8)
        limpar_tela()

        print(f"\nVocê usou {ataque_especial}!")
        print(f"Causou {dano} de dano.")
        print(f"Mana restante: {personagem['mana']}")

        return dano

    # HABILIDADE ESPECIAL

    elif escolha == "3":

        if habilidade_especial == "modo berserker":

            personagem["modo_berserker"] = True
            personagem["contagem_berserker"] = 3

            time.sleep(8)
            limpar_tela()

            print("\nModo Berserker ativado!")
            print("Seus ataques agora causam mais dano.")

            return 0

        elif habilidade_especial == "meteoro arcano":

            if personagem["mana"] < 50:

                print("\nVocê não possui mana suficiente!")

                time.sleep(8)
                limpar_tela()

                return turno(personagem, alvo)

            personagem["mana"] -= 50

            dano = random.randint(80, 120)

            print("\nVocê invocou um meteoro arcano!")
            print(f"Causou {dano} de dano.")
            print(f"Mana restante: {personagem['mana']}")

            time.sleep(8)
            limpar_tela()

            return dano

        elif habilidade_especial == "envenenamento":

            alvo["inimigo_envenenado"] = True
            alvo["contagem_veneno"] = 3
            alvo["condição"] = True

            print("\nVocê envenenou o inimigo!")
            print("Ele sofrerá dano ao longo do tempo.")

            time.sleep(8)
            limpar_tela()

            return 0
    elif escolha == "4":
        personagem['vida'] += 100
        print("Você recuperou 100 de vida!")
        personagem["pocao_cura"] -= 1
        dano = 0
        return dano

    elif escolha == "5":
        personagem['mana'] += 50
        print("Você recuperou 50 de Mana!")
        personagem["pocao_mana"] -= 1
        dano = 0
        return dano

    # ESCOLHA INVÁLIDA

    else:

        print("\nEscolha inválida. Tente novamente.")

        time.sleep(8)
        limpar_tela()

        return turno(personagem, alvo)


# TURNO DO VILÃO

def turno_vilão(personagem, vilão):

    dano = 0

    # DRAGÃO

    if vilão["classe"].lower() == "dragão":

        ataque = random.choice(
            ["Garrada", "Voo", "Sopro de fogo"]
        )

        if ataque == "Garrada":

            dano = random.randint(20, 40)

            print(f"\nO Dragão usou {ataque}!")
            print(f"Causou {dano} de dano.")

        elif ataque == "Voo":

            vilão["voo_dragao"] = True
            dano = 0
            vilão["vida"] += 30

            print("\nO Dragão levantou voo e os céus o agraciaram!")
            print("Ele não causou dano neste turno.")

        elif ataque == "Sopro de fogo":

            dano = random.randint(60, 90)

            print("\nO Dragão usou Sopro de fogo!")
            print(f"Causou {dano} de dano.")

    # BRUXO

    elif vilão["classe"].lower() == "bruxo":

        ataque = random.choice(
            [
                "Magia Macabra",
                "Necromancia",
                "Reviver Ancião"
            ]
        )

        if ataque == "Magia Macabra":

            dano = random.randint(15, 30)

            print(f"\nO Bruxo usou {ataque}!")
            print(f"Causou {dano} de dano.")

        elif ataque == "Necromancia":

            vilão["esqueletos"] = True
            dano = random.randint(20, 35)

            print("\nO Bruxo usou Necromancia!")
            print("Esqueletos foram invocados!")
            print(f"Causou {dano} de dano.")

        elif ataque == "Reviver Ancião":

            dano = 0

            print("\nO Bruxo usou Reviver Ancião!")
            print("O Ancião foi invocado!")

            return dano, True

    # GOBLIN

    elif vilão["classe"].lower() == "goblin":

        ataque = random.choice(
            [
                "Adaga",
                "Chamar Amigos",
                "Roubar"
            ]
        )

        if ataque == "Adaga":

            dano = random.randint(10, 15)

            personagem["personagem_sangramento"] = True
            personagem["condição"] = True
            personagem["contagem_sangramento"] = 3

            print("\nO Goblin usou Adaga!")
            print(f"Causou {dano} de dano.")
            print("Você começou a sangrar!")

        elif ataque == "Chamar Amigos":

            vilão["vida"] += 30
            dano = 0

            print("\nO Goblin chamou seus amigos!")
            print("O Goblin recuperou 30 de vida.")

        elif ataque == "Roubar":

            dano = 0

            print("\nO Goblin tentou roubar uma habilidade!")

            roubo = random.choice(
                [
                    "meteoro arcano",
                    "sopro do dragão",
                    "invocar ancião",
                    "golpe de fúria"
                ]
            )

            if roubo == "meteoro arcano":

                dano = random.randint(80, 120)

                print("\nGoblin invocou um meteoro arcano!")
                print(f"Causou {dano} de dano.")

            elif roubo == "sopro do dragão":

                dano = random.randint(60, 90)

                print("\nO Goblin usou Sopro do Dragão!")
                print(f"Causou {dano} de dano.")

            elif roubo == "invocar ancião":

                dano = 0

                print(
                    "\nO Goblin fez um ritual Macabro "
                    "e usou Reviver Ancião!"
                )

                print("O Ancião foi invocado!")

                return dano, True

            elif roubo == "golpe de fúria":

                dano = random.randint(70, 100)

                print(
                    "\nO Goblin se enraivece, ficando "
                    "completamente vermelho, e liberta "
                    "a sua fúria roubada!"
                )

                print(f"Causou {dano} de dano.")

    time.sleep(12)
    limpar_tela()

    return dano, False


# TURNO DO ANCIÃO

def turno_anciao(anciao, personagem, vilão):

    print("TURNO DO ANCIÃO")

    alvo = random.choice(
        ["personagem", "vilão"]
    )

    dano = random.randint(80, 120)

    if alvo == "personagem":

        personagem["vida"] -= dano

        if personagem["vida"] < 0:
            personagem["vida"] = 0

        print(
            f"\nO Ancião atacou "
            f"{personagem['nome']}!"
        )

        print(f"Causou {dano} de dano.")

        print(
            f"{personagem['nome']} "
            f"agora tem "
            f"{personagem['vida']} de vida."
        )

    elif alvo == "vilão":

        vilão["vida"] -= dano

        if vilão["vida"] < 0:
            vilão["vida"] = 0

        print(
            f"\nO Ancião atacou "
            f"{vilão['nome']}!"
        )

        print(f"Causou {dano} de dano.")

        print(
            f"{vilão['nome']} "
            f"agora tem "
            f"{vilão['vida']} de vida."
        )

    time.sleep(12)
    limpar_tela()


# COMBATE

def combate(personagem, vilão, ancião):

    anciao = None

    atacante = random.choice(
        ["personagem", "vilão"]
    )

    print("          COMBATE INICIADO")

    print(
        f"{personagem['nome']} "
        f"({personagem['classe']}) "
        f"VS "
        f"{vilão['nome']} "
        f"({vilão['classe']})"
    )

    print(f"\nPrimeiro a agir: {atacante}")

    while (
        personagem["vida"] > 0
        and
        (
            vilão["vida"] > 0
            or
            (
                anciao is not None
                and
                anciao["vida"] > 0
            )
        )
    ):

        # TURNO DO PERSONAGEM

        if atacante == "personagem":

            print("SEU TURNO")

            # ESCOLHA DO ALVO

            if (
                anciao is not None
                and
                anciao["vida"] > 0
                and
                vilão["vida"] > 0
            ):

                print("\nEscolha seu alvo:")
                print("1. Vilão", vilão['nome'], " - ", vilão['vida'])
                print("2. Ancião - ", ancião['vida'])

                alvo = input(
                    "Digite o número do alvo: "
                )

                while alvo not in ["1", "2"]:

                    print("\nEscolha inválida.")

                    alvo = input(
                        "Digite o número do alvo: "
                    )

                if alvo == "1":

                    alvo_personagem = vilão

                else:

                    alvo_personagem = anciao

            elif vilão["vida"] > 0:

                alvo_personagem = vilão

            elif anciao is not None and anciao["vida"] > 0:

                alvo_personagem = anciao

            dano = turno(
                personagem,
                alvo_personagem
            )

            alvo_personagem["vida"] -= dano

            if alvo_personagem["vida"] < 0:
                alvo_personagem["vida"] = 0

            print(
                f"\n{alvo_personagem['nome']} "
                f"agora tem "
                f"{alvo_personagem['vida']} de vida."
            )

            if alvo_personagem["vida"] <= 0:

                print(
                    f"\n{alvo_personagem['nome']} "
                    f"foi derrotado!"
                )

            time.sleep(12)
            limpar_tela()

            # ESCOLHE O PRÓXIMO ATACANTE
            # O PERSONAGEM NÃO PODE REPETIR

            possibilidades = []

            if vilão["vida"] > 0:

                possibilidades.append("vilão")

            if (
                anciao is not None
                and
                anciao["vida"] > 0
            ):

                possibilidades.append("ancião")

            atacante = random.choice(
                possibilidades
            )

        # TURNO DO VILÃO

        elif atacante == "vilão":

            print("TURNO DO VILÃO")

            resultado = turno_vilão(
                personagem,
                vilão
            )

            dano = resultado[0]
            invocou_anciao = resultado[1]

            if invocou_anciao == True:

                if anciao is None:

                    anciao = oanciao.criar_anciao()

                print(
                    "\nO Ancião entrou no combate!"
                )

                time.sleep(12)
                limpar_tela()

            else:

                personagem["vida"] -= dano

                if personagem["vida"] < 0:
                    personagem["vida"] = 0

                print(
                    f"\n{personagem['nome']} "
                    f"agora tem "
                    f"{personagem['vida']} de vida."
                )

            # O VILÃO NÃO PODE REPETIR

            possibilidades = []

            if personagem["vida"] > 0:

                possibilidades.append("personagem")

            if (
                anciao is not None
                and
                anciao["vida"] > 0
            ):

                possibilidades.append("ancião")

            atacante = random.choice(
                possibilidades
            )

        # TURNO DO ANCIÃO

        elif atacante == "ancião":

            turno_anciao(
                anciao,
                personagem,
                vilão
            )

            # O ANCIÃO NÃO PODE REPETIR

            possibilidades = []

            if personagem["vida"] > 0:

                possibilidades.append("personagem")

            if vilão["vida"] > 0:

                possibilidades.append("vilão")

            if possibilidades:

                atacante = random.choice(
                    possibilidades
                )

    print("          COMBATE ENCERRADO")

    if personagem["vida"] <= 0:

        print(
            f"{personagem['nome']} foi derrotado!"
        )

        if vilão["vida"] > 0:

            print(f"{vilão['nome']} venceu!")

        elif anciao is not None and anciao["vida"] > 0:

            print("O Ancião venceu!")

    elif vilão["vida"] <= 0:

        if anciao is not None and anciao["vida"] > 0:

            print(
                f"{vilão['nome']} foi derrotado!"
            )

            print("O Ancião ainda está vivo!")

        else:

            print(
                f"{vilão['nome']} foi derrotado!"
            )

            print(
                f"{personagem['nome']} venceu!"
            )