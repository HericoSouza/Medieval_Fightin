from configuracao import PROGRESSAO


class SistemaProgressao:
    @staticmethod
    def conceder_experiencia(personagem, quantidade):
        mensagens = []
        if quantidade <= 0:
            return mensagens
        if personagem.nivel >= PROGRESSAO["nivel_maximo"]:
            mensagens.append(f"Recompensa: {quantidade} XP. Você já alcançou o nível máximo.")
            return mensagens

        personagem.experiencia += quantidade
        mensagens.append(f"Você recebeu {quantidade} XP.")

        while personagem.nivel < PROGRESSAO["nivel_maximo"]:
            necessario = PROGRESSAO["xp_por_nivel"][personagem.nivel]
            personagem.experiencia_proximo_nivel = necessario
            if personagem.experiencia < necessario:
                break

            personagem.experiencia -= necessario
            personagem.nivel += 1
            vida_ganha = PROGRESSAO["vida_por_nivel"]
            mana_ganha = PROGRESSAO["mana_por_nivel"]
            dano_ganho = PROGRESSAO["dano_por_nivel"]
            personagem.vida_maxima += vida_ganha
            personagem.mana_maxima += mana_ganha
            personagem.vida = min(personagem.vida_maxima, personagem.vida + vida_ganha)
            personagem.mana = min(personagem.mana_maxima, personagem.mana + mana_ganha)
            personagem.bonus_dano += dano_ganho
            mensagens.append(
                f"NÍVEL {personagem.nivel}! +{vida_ganha} de vida máxima, "
                f"+{mana_ganha} de mana máxima e +{dano_ganho} de dano."
            )

        if personagem.nivel < PROGRESSAO["nivel_maximo"]:
            personagem.experiencia_proximo_nivel = PROGRESSAO["xp_por_nivel"][personagem.nivel]
            mensagens.append(
                f"Experiência: {personagem.experiencia}/"
                f"{personagem.experiencia_proximo_nivel} XP para o próximo nível."
            )
        else:
            personagem.experiencia_proximo_nivel = 0
            mensagens.append("Você alcançou o nível máximo desta Alpha: 5.")

        return mensagens

    @staticmethod
    def aplicar_loot(personagem, loot):
        efeitos = loot.get("efeitos", {})
        mensagens = []

        if "pocao_cura" in efeitos:
            personagem.pocao_cura += efeitos["pocao_cura"]
            mensagens.append(f"+{efeitos['pocao_cura']} poção(ões) de cura")

        if "pocao_mana" in efeitos:
            personagem.pocao_mana += efeitos["pocao_mana"]
            mensagens.append(f"+{efeitos['pocao_mana']} poção(ões) de mana")

        if "ouro" in efeitos:
            personagem.ouro += efeitos["ouro"]
            mensagens.append(f"+{efeitos['ouro']} moedas")

        if "bonus_dano" in efeitos:
            personagem.bonus_dano += efeitos["bonus_dano"]
            mensagens.append(f"+{efeitos['bonus_dano']} de dano permanente")

        if "defesa" in efeitos:
            personagem.defesa += efeitos["defesa"]
            mensagens.append(f"+{efeitos['defesa']} de defesa permanente")

        if "vida_maxima" in efeitos:
            personagem.vida_maxima += efeitos["vida_maxima"]
            personagem.vida = min(
                personagem.vida_maxima,
                personagem.vida + efeitos["vida_maxima"]
            )
            mensagens.append(f"+{efeitos['vida_maxima']} de vida máxima")

        if "mana_maxima" in efeitos:
            personagem.mana_maxima += efeitos["mana_maxima"]
            personagem.mana = min(
                personagem.mana_maxima,
                personagem.mana + efeitos["mana_maxima"]
            )
            mensagens.append(f"+{efeitos['mana_maxima']} de mana máxima")

        return mensagens

    @staticmethod
    def recuperar_entre_encontros(personagem, companheiro):
        cura = max(1, int(personagem.vida_maxima * PROGRESSAO["recuperacao_vida_percentual"]))
        mana = max(1, int(personagem.mana_maxima * PROGRESSAO["recuperacao_mana_percentual"]))
        personagem.vida = min(personagem.vida_maxima, personagem.vida + cura)
        personagem.mana = min(personagem.mana_maxima, personagem.mana + mana)
        mensagens = [f"Durante a pausa, {personagem.nome} recupera {cura} de vida e {mana} de mana."]

        if companheiro is not None and companheiro.vida > 0:
            cura_companheiro = max(1, int(companheiro.vida_maxima * PROGRESSAO["recuperacao_companheiro_percentual"]))
            companheiro.vida = min(companheiro.vida_maxima, companheiro.vida + cura_companheiro)
            mensagens.append(f"{companheiro.nome} recupera {cura_companheiro} de vida.")

        return mensagens
