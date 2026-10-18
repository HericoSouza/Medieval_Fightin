# Medieval Fightin' — Alpha

Medieval Fightin' é um RPG textual com interface Tkinter e combate por turnos. Esta versão contém três histórias independentes. Em cada partida, o jogador cria um personagem, escolhe uma única missão e atravessa sete encontros na sequência: três combates, um mini-Boss, dois combates e um Boss final.

## Executar

Com Python 3 instalado, abra o terminal dentro desta pasta e execute:

```powershell
python "Medieval Fightin'.py"
```

A interface utiliza Tkinter, que normalmente acompanha a instalação do Python para Windows. Nenhuma biblioteca externa é necessária.

## Histórias

- **A Gangue do Dente Partido**: a perseguição a uma gangue de goblins, com goblins montados, mercenários, um troll rebelde e o Goblin-Chefe.
- **O Culto sob as Lápides**: uma investigação sobre ladrões de túmulos que conduz a um culto necromântico, ao Médico da Peste e ao Bruxo.
- **A Lenda das Cinzas**: esqueletos em evolução, Vharjir e o dragão ancestral Vharzun.

Cada história tem diálogos, inimigos, recompensas e um companheiro recrutável. O companheiro ataca imediatamente depois do protagonista em cada turno. Na batalha contra goblins montados, o jogador pode atacar separadamente o goblin ou sua montaria.

Ao concluir uma história, a interface apresenta o aviso de fim da Alpha. Para jogar outra missão, reinicie e crie outro personagem.

## Arquivos principais

- `Medieval Fightin'.py`: inicializa a interface.
- `interface.py`: interface Tkinter e fluxo da aventura.
- `missoes.py`: diálogos, sete encontros e loots exclusivos de cada história.
- `entidades.py`: personagens, companheiros, inimigos normais e Bosses.
- `combate.py`: regras de turno, ações, ataques, condições e seleção de alvos.
- `progressao.py`: XP, níveis, loot e recuperação entre encontros.
- `configuracao.py`: atributos iniciais, danos, poções e curva de progressão.
- `criacao_personagem.py`: criação do personagem a partir do nome e classe.
- `condicao.py`: processamento de veneno, congelamento e sangramento.

## Progressão da Alpha

Os encontros concedem XP por vitória. A distribuição atual foi pensada para levar o personagem do nível 1 ao nível 5 durante a história completa. Os valores podem ser alterados em `missoes.py` e `configuracao.py`. Os loots de cada encontro também alteram atributos, poções, ouro ou defesa.

A interface é deliberadamente simples: o texto da história fica na parte superior e, na parte inferior, aparecem barras de vida, mana, experiência, poções, defesa, ouro, companheiro, inimigos e ações de combate.
