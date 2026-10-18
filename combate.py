import random

from configuracao import DANOS_PERSONAGENS, VALORES_POCOES, CONDICOES
from condicao import SistemaCondicoes


class SistemaCombate:
    def __init__(self, personagem, companheiro, inimigos):
        self.personagem = personagem
        self.companheiro = companheiro
        self.inimigos = list(inimigos)
        self.condicoes = SistemaCondicoes()
        self.turno = 0
        self.encerrado = False
        self.resultado = None

    def inimigos_vivos(self):
        return [inimigo for inimigo in self.inimigos if inimigo.vida > 0]

    def obter_alvos(self):
        alvos = []
        for inimigo in self.inimigos_vivos():
            if inimigo.montaria_ativa and inimigo.montaria_vida > 0:
                alvos.append((inimigo, "montaria", f"{inimigo.montaria['nome']} — {inimigo.montaria_vida}/{inimigo.montaria_vida_maxima} PV"))
            alvos.append((inimigo, "corpo", f"{inimigo.nome} — {inimigo.vida}/{inimigo.vida_maxima} PV"))
        return alvos

    def estado(self):
        if self.personagem.vida <= 0:
            self.encerrado = True
            self.resultado = "derrota"
        elif not self.inimigos_vivos():
            self.encerrado = True
            self.resultado = "vitoria"
        return self.resultado

    def _aplicar_dano_alvo(self, inimigo, parte, dano, mensagens):
        if inimigo.vida <= 0:
            return
        if parte == "montaria" and inimigo.montaria_ativa:
            dano_real = max(1, dano - getattr(inimigo, "defesa_montaria", 0))
            inimigo.montaria_vida = max(0, inimigo.montaria_vida - dano_real)
            mensagens.append(f"Você causou {dano_real} de dano à montaria de {inimigo.nome}.")
            if inimigo.montaria_vida <= 0:
                inimigo.montaria_ativa = False
                inimigo.tipo = "goblin"
                inimigo.nome = inimigo.nome.replace("montado", "saqueador")
                inimigo.ataque = "Faca de saqueador"
                inimigo.dano = (5, 9)
                mensagens.append(f"A montaria de {inimigo.nome} cai e foge. O goblin continua lutando a pé.")
            return

        dano_real = max(1, dano - getattr(inimigo, "defesa", 0))
        inimigo.vida = max(0, inimigo.vida - dano_real)
        mensagens.append(f"{inimigo.nome} recebe {dano_real} de dano. Vida: {inimigo.vida}/{inimigo.vida_maxima}.")
        if inimigo.vida <= 0 and inimigo.montaria_ativa:
            inimigo.montaria_ativa = False
            mensagens.append(f"{inimigo.nome} cai. A montaria assustada foge para longe.")
        elif inimigo.vida <= 0:
            mensagens.append(f"{inimigo.nome} foi derrotado.")

    def _alvo_automatico(self):
        vivos = self.inimigos_vivos()
        return random.choice(vivos) if vivos else None

    def _dano_jogador(self, acao):
        classe = self.personagem.classe
        dados = DANOS_PERSONAGENS[classe]
        if acao == "basico":
            dano = random.randint(*dados["basico"])
            self.personagem.mana = min(self.personagem.mana_maxima, self.personagem.mana + 8)
            nome = {"Guerreiro": "Golpe de espada", "Mago": "Bola de fogo", "Arqueiro": "Flecha precisa"}[classe]
            return dano + self.personagem.bonus_dano, nome, True
        if acao == "especial":
            custo = dados["especial_custo"]
            if self.personagem.mana < custo:
                return None, f"Você precisa de {custo} de mana para usar o ataque especial.", False
            self.personagem.mana -= custo
            minimo, maximo = dados["especial"]
            if classe == "Guerreiro" and self.personagem.contagem_berserker > 0:
                minimo, maximo = 42, 60
                self.personagem.contagem_berserker -= 1
                if self.personagem.contagem_berserker <= 0:
                    self.personagem.contagem_berserker = 0
                    self.personagem.modo_berserker = False
                    nome = "Golpe de Fúria (último golpe berserker)"
                else:
                    nome = "Golpe de Fúria Berserker"
            else:
                nome = {"Guerreiro": "Golpe de Fúria", "Mago": "Raio de Gelo", "Arqueiro": "Chuva de Flechas"}[classe]
            return random.randint(minimo, maximo) + self.personagem.bonus_dano, nome, True
        return 0, "", True

    def executar_acao(self, acao, alvo_selecionado=None):
        if self.encerrado:
            return [], self.resultado
        mensagens = []
        alvos = self.obter_alvos()
        alvo = None
        parte = "corpo"
        if alvo_selecionado is not None:
            alvo, parte = alvo_selecionado
        elif alvos:
            alvo, parte, _ = alvos[0]

        precisa_alvo = acao in ("basico", "especial", "habilidade") and not (acao == "habilidade" and self.personagem.classe == "Guerreiro")
        if precisa_alvo and alvo is None:
            return ["Não há alvo disponível."], None

        condicao_msgs, pode_agir = self.condicoes.processar_inicio_turno(self.personagem)
        mensagens.extend(condicao_msgs)
        if self.personagem.vida <= 0:
            mensagens.append(f"{self.personagem.nome} não consegue continuar.")
            self.encerrado = True
            self.resultado = "derrota"
            return mensagens, self.resultado
        if not pode_agir:
            mensagens.append("Você perdeu a ação deste turno.")
            consumiu_turno = True
        else:
            consumiu_turno = True
            if acao == "basico":
                dano, nome_acao, _ = self._dano_jogador("basico")
                mensagens.append(f"Você usou {nome_acao} e causou {dano} de dano.")
                self._aplicar_dano_alvo(alvo, parte, dano, mensagens)
            elif acao == "especial":
                dano, nome_acao, valido = self._dano_jogador("especial")
                if not valido:
                    return [nome_acao], None
                mensagens.append(f"Você usou {nome_acao}.")
                if self.personagem.classe == "Mago":
                    if parte == "montaria":
                        alvo.congelado_turnos = max(alvo.congelado_turnos, 1)
                    else:
                        alvo.congelado_turnos = max(alvo.congelado_turnos, 1)
                    mensagens.append(f"{alvo.nome} foi envolvido pelo gelo.")
                self._aplicar_dano_alvo(alvo, parte, dano, mensagens)
            elif acao == "habilidade":
                if self.personagem.classe == "Guerreiro":
                    self.personagem.modo_berserker = True
                    self.personagem.contagem_berserker = 3
                    mensagens.append("Você assume o Modo Berserker. Seus próximos três golpes especiais causam dano aumentado.")
                elif self.personagem.classe == "Mago":
                    custo = DANOS_PERSONAGENS["Mago"]["habilidade_custo"]
                    if self.personagem.mana < custo:
                        return [f"Você precisa de {custo} de mana para invocar o Meteoro Arcano."], None
                    self.personagem.mana -= custo
                    dano = random.randint(*DANOS_PERSONAGENS["Mago"]["habilidade"]) + self.personagem.bonus_dano
                    mensagens.append(f"Você invoca o Meteoro Arcano e causa {dano} de dano.")
                    self._aplicar_dano_alvo(alvo, parte, dano, mensagens)
                elif self.personagem.classe == "Arqueiro":
                    alvo.veneno_turnos = CONDICOES["veneno"]["duracao"]
                    alvo.veneno_dano = DANOS_PERSONAGENS["Arqueiro"]["veneno"]
                    mensagens.append(f"Você envenenou {alvo.nome}. O veneno durará até três turnos do alvo.")
            elif acao == "cura":
                if self.personagem.pocao_cura <= 0:
                    return ["Você não possui poções de cura."], None
                if self.personagem.vida >= self.personagem.vida_maxima:
                    return ["Sua vida já está cheia; guarde a poção."], None
                antes = self.personagem.vida
                self.personagem.vida = min(self.personagem.vida_maxima, self.personagem.vida + VALORES_POCOES["cura"])
                recuperado = self.personagem.vida - antes
                self.personagem.pocao_cura -= 1
                mensagens.append(f"Você usou uma poção de cura e recuperou {recuperado} de vida.")
            elif acao == "mana":
                if self.personagem.pocao_mana <= 0:
                    return ["Você não possui poções de mana."], None
                if self.personagem.mana >= self.personagem.mana_maxima:
                    return ["Sua mana já está cheia; guarde a poção."], None
                antes = self.personagem.mana
                self.personagem.mana = min(self.personagem.mana_maxima, self.personagem.mana + VALORES_POCOES["mana"])
                recuperado = self.personagem.mana - antes
                self.personagem.pocao_mana -= 1
                mensagens.append(f"Você usou uma poção de mana e recuperou {recuperado} de mana.")
            else:
                return ["Ação desconhecida."], None

        if self.personagem.vida <= 0:
            self.encerrado = True
            self.resultado = "derrota"
            return mensagens, self.resultado

        if not self.inimigos_vivos():
            self.encerrado = True
            self.resultado = "vitoria"
            return mensagens, self.resultado

        if self.companheiro is not None and self.companheiro.vida > 0:
            ataque_companheiro = self.companheiro.atacar(self.personagem.nivel, self.inimigos_vivos())
            if ataque_companheiro:
                alvo_companheiro, dano_companheiro, especial = ataque_companheiro
                nome_ataque = self.companheiro.especial if especial else "Ataque de companheiro"
                mensagens.append(f"{self.companheiro.nome} age imediatamente depois de você: {nome_ataque}!")
                self._aplicar_dano_alvo(alvo_companheiro, "corpo", dano_companheiro, mensagens)

        if not self.inimigos_vivos():
            self.encerrado = True
            self.resultado = "vitoria"
            return mensagens, self.resultado

        self.turno += 1
        for inimigo in list(self.inimigos_vivos()):
            if self.personagem.vida <= 0:
                break
            if inimigo.vida <= 0:
                continue
            status_msgs, pode_inimigo_agir = self.condicoes.processar_inicio_turno(inimigo)
            mensagens.extend(status_msgs)
            if inimigo.vida <= 0:
                mensagens.append(f"{inimigo.nome} caiu por causa dos efeitos de status.")
                continue
            if not pode_inimigo_agir:
                continue
            dano, mensagem, efeito = self._acao_inimigo(inimigo)
            mensagens.append(mensagem)
            alvo_grupo = self._escolher_alvo_grupo()
            if alvo_grupo is None:
                continue
            if efeito and efeito.get("tipo") == "veneno":
                alvo_grupo.veneno_turnos = efeito["turnos"]
                alvo_grupo.veneno_dano = efeito["dano"]
                mensagens.append(f"{alvo_grupo.nome} foi envenenado.")
            if dano > 0:
                defesa = getattr(alvo_grupo, "defesa", 0)
                dano_real = max(1, dano - defesa)
                alvo_grupo.vida = max(0, alvo_grupo.vida - dano_real)
                mensagens.append(f"{alvo_grupo.nome} recebe {dano_real} de dano. Vida: {alvo_grupo.vida}/{alvo_grupo.vida_maxima}.")
                if alvo_grupo.vida <= 0:
                    mensagens.append(f"{alvo_grupo.nome} caiu e não pode mais lutar.")

        if self.personagem.vida <= 0:
            self.encerrado = True
            self.resultado = "derrota"
        elif not self.inimigos_vivos():
            self.encerrado = True
            self.resultado = "vitoria"

        return mensagens, self.resultado

    def _escolher_alvo_grupo(self):
        if self.companheiro is not None and self.companheiro.vida > 0 and random.random() < 0.35:
            return self.companheiro
        return self.personagem

    def _acao_inimigo(self, inimigo):
        inimigo.turnos_ativos += 1
        tipo = inimigo.tipo
        if tipo == "troll" and inimigo.turnos_ativos % 3 == 0:
            dano = random.randint(18, 25)
            return dano, f"{inimigo.nome} usa Fúria da pedreira e desfere um golpe brutal ({dano} de dano antes da defesa).", None
        if tipo == "medico_peste" and inimigo.turnos_ativos % 3 == 0:
            efeito = {"tipo": "veneno", "turnos": 2, "dano": (4, 7)}
            return random.randint(7, 12), f"{inimigo.nome} espalha Névoa pestilenta, causando dano e deixando uma nuvem venenosa no ar.", efeito
        if tipo == "vice_culto" and inimigo.turnos_ativos % 3 == 0:
            return random.randint(16, 22), f"{inimigo.nome} lança uma Maldição curta.", None
        if tipo == "vharjir" and inimigo.turnos_ativos % 3 == 0:
            return random.randint(22, 30), f"{inimigo.nome} solta um Sopro ósseo ardente.", None
        if tipo == "vharzun":
            ciclo = inimigo.turnos_ativos % 3
            if ciclo == 0:
                cura = min(24, inimigo.vida_maxima - inimigo.vida)
                inimigo.vida += cura
                return 0, f"{inimigo.nome} bate as asas e absorve calor do magma, recuperando {cura} de vida.", None
            if ciclo == 2:
                return random.randint(27, 36), f"{inimigo.nome} lança um Sopro de brasas.", None
        if tipo == "necromante" and inimigo.turnos_ativos % 3 == 0:
            return random.randint(20, 27), f"{inimigo.nome} usa Sifão de almas.", None
        if tipo == "goblin_chefe" and inimigo.turnos_ativos % 3 == 0:
            return random.randint(17, 24), f"{inimigo.nome} ordena um Comando brutal.", None
        dano = random.randint(*inimigo.dano)
        return dano, f"{inimigo.nome} ataca com {inimigo.ataque} ({dano} de dano antes da defesa).", None
