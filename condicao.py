import random

from configuracao import CONDICOES


class SistemaCondicoes:
    @staticmethod
    def processar_inicio_turno(combatente):
        mensagens = []
        pode_agir = True

        if getattr(combatente, "sangramento_turnos", 0) > 0:
            status = CONDICOES["sangramento"]
            dano = random.randint(status["dano_minimo"], status["dano_maximo"])
            combatente.vida = max(0, combatente.vida - dano)
            combatente.sangramento_turnos -= 1
            mensagens.append(f"{combatente.nome} sofre {dano} de dano por sangramento.")

        if getattr(combatente, "veneno_turnos", 0) > 0 and combatente.vida > 0:
            dano_minimo, dano_maximo = getattr(combatente, "veneno_dano", (4, 8))
            dano = random.randint(dano_minimo, dano_maximo)
            combatente.vida = max(0, combatente.vida - dano)
            combatente.veneno_turnos -= 1
            mensagens.append(f"{combatente.nome} sofre {dano} de dano pelo veneno.")

        if getattr(combatente, "congelado_turnos", 0) > 0 and combatente.vida > 0:
            combatente.congelado_turnos -= 1
            pode_agir = False
            mensagens.append(f"{combatente.nome} está congelado e perde o turno.")

        return mensagens, pode_agir
