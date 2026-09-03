import random


def condição(vilão, personagem, ancião):

    dano_veneno = 0
    dano_sangramento = 0
    congelado = False
    #Condições do Personagem
    if personagem["personagem_sangramento"] == True:
        if personagem["contagem_sangramento"] > 0:
            print("Você está sangrando!")
            dano_sangramento = random.randint(5, 15)
            print(
                personagem["nome"],
                "perdeu",
                dano_sangramento,
                "de vida para o seu sangramento!"
            )
            personagem["vida"] -= dano_sangramento
            personagem["contagem_sangramento"] -= 1
            if personagem["contagem_sangramento"] <= 0:
                personagem["contagem_sangramento"] = 0
                personagem["personagem_sangramento"] = False
                print("Você curou-se do sangramento!")

    if personagem["personagem_sangramento"] == False:
        personagem["condição"] = False

    #Condições do Vilão
    if vilão["inimigo_congelado"] == True:
        print("O Inimigo está congelado!")
        print(vilão["nome"], "não conseguiu agir!")
        vilão["inimigo_congelado"] = False
        congelado = True

    if vilão["inimigo_envenenado"] == True:
        if vilão["contagem_veneno"] > 0:
            print("O Inimigo está envenenado!")
            dano_veneno = random.randint(5, 15)
            print(
                vilão["nome"],
                "perdeu",
                dano_veneno,
                "de vida para o veneno!"
            )
            vilão["vida"] -= dano_veneno
            vilão["contagem_veneno"] -= 1
            if vilão["contagem_veneno"] <= 0:
                vilão["contagem_veneno"] = 0
                vilão["inimigo_envenenado"] = False
                print("O inimigo curou-se do envenenamento!")
        else:
            vilão["inimigo_envenenado"] = False
            print("O inimigo curou-se do envenenamento!")
    if vilão["inimigo_congelado"] == False and vilão["inimigo_envenenado"] == False:
        vilão["condição"] = False

    return dano_veneno, congelado