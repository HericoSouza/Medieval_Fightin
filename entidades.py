import random

from configuracao import STATUS_PERSONAGENS


class Combatente:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.vida_maxima = vida
        self.defesa = 0
        self.veneno_turnos = 0
        self.veneno_dano = (4, 8)
        self.sangramento_turnos = 0
        self.congelado_turnos = 0


class Personagem(Combatente):
    def __init__(self, nome, classe):
        status = STATUS_PERSONAGENS[classe]
        super().__init__(nome, status["vida"])
        self.classe = classe
        self.categoria = "Personagem"
        self.mana = status["mana"]
        self.mana_maxima = status["mana"]
        self.pocao_cura = status["pocao_cura"]
        self.pocao_mana = status["pocao_mana"]
        self.defesa = status["defesa"]
        self.nivel = 1
        self.experiencia = 0
        self.experiencia_proximo_nivel = 100
        self.bonus_dano = 0
        self.ouro = 0
        self.modo_berserker = False
        self.contagem_berserker = 0
        self.ataques_realizados = 0


class Guerreiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome, "Guerreiro")


class Mago(Personagem):
    def __init__(self, nome):
        super().__init__(nome, "Mago")


class Arqueiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome, "Arqueiro")


class Companheiro(Combatente):
    def __init__(self, nome, titulo, vida, dano, dano_especial, especial, personalidade):
        super().__init__(nome, vida)
        self.titulo = titulo
        self.categoria = "Companheiro"
        self.vida_maxima = vida
        self.dano = dano
        self.dano_especial = dano_especial
        self.especial = especial
        self.personalidade = personalidade
        self.defesa = 1
        self.turnos_ativos = 0

    def atacar(self, nivel_personagem, inimigos):
        alvos = [inimigo for inimigo in inimigos if inimigo.vida > 0]
        if not alvos or self.vida <= 0:
            return None
        alvo = random.choice(alvos)
        self.turnos_ativos += 1
        escala = max(0, nivel_personagem - 1) * 2
        especial = self.turnos_ativos % 3 == 0
        dano_minimo, dano_maximo = self.dano_especial if especial else self.dano
        dano = random.randint(dano_minimo, dano_maximo) + escala
        return alvo, dano, especial


class Inimigo(Combatente):
    def __init__(self, nome, tipo, vida, dano, categoria="Inimigo normal", ataque="Ataque", montaria=None, defesa=0, especial=None):
        super().__init__(nome, vida)
        self.tipo = tipo
        self.classe = tipo
        self.categoria = categoria
        self.dano = tuple(dano)
        self.ataque = ataque
        self.especial = especial
        self.defesa = defesa
        self.turnos_ativos = 0
        self.montaria = montaria
        self.montaria_ativa = montaria is not None
        self.montaria_vida = montaria["vida"] if montaria else 0
        self.montaria_vida_maxima = self.montaria_vida
        self.congelado_turnos = 0
        self.veneno_turnos = 0
        self.veneno_dano = (4, 8)
        self.sangramento_turnos = 0
        self.veneno_no_jogador = False
        self.esqueletos = False


class InimigoNormal(Inimigo):
    def __init__(self, nome, tipo, vida, dano, ataque="Ataque", montaria=None, defesa=0, especial=None):
        super().__init__(nome, tipo, vida, dano, "Inimigo normal", ataque, montaria, defesa, especial)


class Boss(Inimigo):
    def __init__(self, nome, tipo, vida, dano, ataque="Ataque", defesa=1, especial=None):
        super().__init__(nome, tipo, vida, dano, "Boss", ataque, None, defesa, especial)


class Esqueleto(InimigoNormal):
    def __init__(self, nome="Esqueleto"):
        super().__init__(nome, "esqueleto", 45, (6, 10), "Espada enferrujada")


class Dragao(Boss):
    def __init__(self, nome="Dragão"):
        super().__init__(nome, "vharzun", 440, (18, 27), "Garra ancestral", 2)


class Bruxo(Boss):
    def __init__(self, nome="Bruxo"):
        super().__init__(nome, "necromante", 360, (14, 22), "Magia macabra", 1)


class GoblinChefe(Boss):
    def __init__(self, nome="Goblin-Chefe"):
        super().__init__(nome, "goblin_chefe", 360, (15, 22), "Machado de guerra", 1)


Goblin = GoblinChefe


class Anciao(Combatente):
    def __init__(self):
        super().__init__("O Ancião Antigo", 200)
        self.categoria = "Invocação"


class CriadorAnciao:
    def criar_anciao(self):
        return Anciao()
