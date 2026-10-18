from entidades import Guerreiro, Mago, Arqueiro


class CriadorPersonagem:
    CLASSES = {
        "guerreiro": Guerreiro,
        "mago": Mago,
        "arqueiro": Arqueiro
    }

    @staticmethod
    def criar_por_dados(nome, classe):
        classe_normalizada = classe.strip().lower()
        if classe_normalizada not in CriadorPersonagem.CLASSES:
            raise ValueError("Escolha Guerreiro, Mago ou Arqueiro.")
        return CriadorPersonagem.CLASSES[classe_normalizada](nome.strip())
