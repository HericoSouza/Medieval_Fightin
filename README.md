<div align="center">

# ⚔️ Medieval Fightin' 🔥

### Uma aventura medieval em RPG textual, construída em Python

**Três histórias. Sete encontros por missão. Escolhas, companheiros e batalhas por turnos.**

<p>
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Interface-Tkinter-6B8E23?style=for-the-badge" alt="Tkinter">
  <img src="https://img.shields.io/badge/Status-Alpha-orange?style=for-the-badge" alt="Status Alpha">
  <img src="https://img.shields.io/badge/Projeto-Educacional-7851A9?style=for-the-badge" alt="Projeto educacional">
</p>

[**Jogar**](#-instalação-e-execução) · [**Conhecer as histórias**](#-as-três-missões) · [**Entender o código**](#-estrutura-do-projeto)

</div>

---

## 📜 Sobre o projeto

**Medieval Fightin'** é um RPG de texto com interface gráfica feita em **Tkinter**, desenvolvido como um projeto pessoal de estudo da linguagem Python.

A ideia é unir uma aventura de fantasia medieval a exercícios práticos de **lógica de programação**, **utilização da matemática** e **programação orientada a objetos (POO)**. O jogo serve como um espaço para experimentar regras, modelar personagens, organizar sistemas e testar o equilíbrio entre habilidades, inimigos e recompensas.

Esta é uma versão **Alpha**: o jogo já reúne três missões jogáveis, combates por turnos, companheiros, progressão e uma interface gráfica simples, mas suas mecânicas e seus valores ainda podem mudar durante os testes.

## 🎯 Objetivos de aprendizado

- **Lógica de programação:** decisões, condições, repetições, fluxo das missões e regras de combate.
- **Matemática aplicada:** faixas aleatórias de dano, pontos de vida e mana, experiência, níveis, recompensas e balanceamento de dificuldade.
- **Programação orientada a objetos:** classes para personagens, inimigos e companheiros; atributos e comportamentos próprios; organização das responsabilidades em módulos.
- **Interface gráfica:** uso do Tkinter, eventos de botões, atualização de status e apresentação de texto em uma janela.
- **Organização de software:** separar dados das missões, configurações, entidades, combate, condições e progressão para facilitar futuras alterações.

## 🧭 As três missões

Cada partida começa com a criação de um personagem e a escolha de **uma** das três histórias. Todas seguem a mesma estrutura de progressão narrativa: **3 combates → 1 mini-Boss → 2 combates → 1 Boss final**.

### 🟢 1. A Gangue do Dente Partido

Vilas inteiras estão sendo saqueadas por uma gangue de goblins. Para descobrir quem está organizando os ataques, o aventureiro terá de enfrentar saqueadores, goblins montados, mercenários e um exército de goblins.

- **Mini-Boss:** um Troll capturado pela gangue que se rebelou contra seus captores.
- **Boss final:** o Goblin-Chefe.
- **Companheira opcional:** **Aiko Suzuki**, uma ronin forasteira que luta com duas katanas e usa uma máscara de oni.
- **Mecânica especial:** nos encontros com goblins montados, é possível escolher atacar o goblin ou a montaria. Se a montaria for derrotada, o goblin continua lutando a pé; se o goblin cair primeiro, a montaria foge.

### 🟣 2. O Culto sob as Lápides

O que parece começar com roubos em um cemitério revela uma conspiração necromântica. A investigação leva o aventureiro de ladrões de túmulos a cultistas e criaturas macabras, até chegar aos responsáveis por invocar uma força ancestral.

- **Mini-Boss:** o Médico da Peste.
- **Boss final:** o Bruxo Necromante.
- **Companheiro opcional:** **Joseph Valentine**, um mágico de rua inglês com poderes místicos relacionados ao espaço.
- **Atmosfera:** cemitérios violados, mortos-vivos, rituais e magia proibida.

### 🔴 3. A Lenda das Cinzas

Há séculos, **Vharzun, o Devorador de Brasas**, está aprisionado nas profundezas do Monte Escarlate. A prisão enfraquece, os animais desaparecem e guerreiros mortos voltam a caminhar. O aventureiro precisa descobrir por que os esqueletos estão evoluindo e impedir o retorno do dragão ancestral.

- **Mini-Boss:** **Vharjir**, o Filho das Brasas.
- **Boss final:** **Vharzun**, o Devorador de Brasas.
- **Companheiro opcional:** **Kaleb Johnson**, um lanceiro da fronteira bruto, carismático e bem-humorado.
- **Tema dos encontros:** esqueletos e suas evoluções, de guerreiros comuns a guardiões antigos.

## 🗡️ Como funciona o jogo

- **Criação de personagem:** escolha o nome e uma classe — Guerreiro, Mago ou Arqueiro.
- **Combate por turnos:** selecione ataques e habilidades, escolha alvos e gerencie os recursos disponíveis.
- **Status de combate:** vida, mana, defesa e efeitos como veneno, sangramento e congelamento.
- **Companheiros:** cada missão oferece um aliado opcional. Se recrutado, ele participa dos combates e age logo após o protagonista.
- **Progressão:** os encontros concedem experiência e recompensas. A progressão da Alpha foi planejada para levar o personagem do nível 1 ao nível 5 durante uma história.
- **Loot:** os encontros podem entregar poções, moedas ou melhorias permanentes.
- **Recuperação entre encontros:** o personagem e seu companheiro podem recuperar parte dos recursos antes do próximo desafio.
- **Fim da Alpha:** após concluir uma história, o jogo apresenta uma mensagem de encerramento. Para conhecer as outras missões, reinicie e crie um novo personagem.

## 🖥️ Interface

A interface foi construída com **Tkinter**, biblioteca gráfica disponível com muitas instalações padrão do Python.

O texto narrativo e o registro do combate ficam na área superior. Na parte inferior, a janela apresenta status do personagem e do companheiro, nível e experiência, recursos, inimigos, alvos e botões de ação.

A proposta visual é intencionalmente simples: esta Alpha prioriza a experimentação das regras e da estrutura do jogo antes de investir em arte, animações ou efeitos mais elaborados.

## 📦 Instalação e execução

### Requisitos

- Windows recomendado para seguir os passos abaixo.
- Python 3 instalado.
- Tkinter disponível na instalação do Python.

O projeto não exige bibliotecas externas adicionais para executar a interface básica.

### 1. Baixe o projeto

Baixe o repositório pelo GitHub usando **Code → Download ZIP**, ou clone-o com Git:

```powershell
git clone https://github.com/HericoSouza/Medieval_Fightin.git
cd Medieval_Fightin
```

### 2. Confira a instalação do Python

Abra o PowerShell ou o terminal do VS Code e execute:

```powershell
python --version
```

Para verificar se o Tkinter está disponível:

```powershell
python -m tkinter
```

Se o comando abrir uma pequena janela de demonstração, o Tkinter está disponível. Feche a janela de demonstração antes de continuar.

### 3. Inicie o jogo

No terminal, dentro da pasta do projeto, execute:

```powershell
python "Medieval Fightin'.py"
```

A janela do Medieval Fightin' será aberta. Digite o nome do personagem, escolha a classe, selecione uma missão e comece a aventura.

> **Dica:** se `python` não for reconhecido no terminal, confira a instalação do Python e a opção de adicioná-lo ao `PATH` durante a instalação.

## 🗂️ Estrutura do projeto

| Arquivo | Responsabilidade |
|---|---|
| `Medieval Fightin'.py` | Ponto de entrada; inicia a interface. |
| `interface.py` | Janela Tkinter, botões, apresentação da história e atualização dos status. |
| `missoes.py` | Histórias, diálogos, encontros, inimigos, XP e loot de cada missão. |
| `entidades.py` | Classes do protagonista, companheiros, inimigos normais e Bosses. |
| `combate.py` | Turnos, ações, dano, alvos, condições e regras de batalha. |
| `condicao.py` | Processamento dos efeitos de status durante o combate. |
| `progressao.py` | Experiência, níveis, recompensas, loot e recuperação entre encontros. |
| `configuracao.py` | Atributos iniciais, dano, poções e parâmetros de progressão. |
| `criacao_personagem.py` | Criação do personagem de acordo com o nome e a classe escolhida. |
| `Medieval Fightin'.spec` | Arquivo de especificação para um possível empacotamento com PyInstaller. |
| `icone.ico` | Ícone do projeto. |

## ⚖️ Balanceamento e configuração

Os valores de balanceamento ficam centralizados principalmente em `configuracao.py`, enquanto os dados de cada missão — incluindo diálogos, encontros, experiência e loot — ficam em `missoes.py`.

Esse arranjo facilita testar mudanças sem precisar espalhar números por todos os módulos. Como o jogo está em Alpha, valores de dano, vida, experiência, recompensas e recuperação podem ser ajustados a partir dos resultados dos testes.

## 🚧 Estado da Alpha e próximos passos

Esta versão é um protótipo jogável para estudo e experimentação. O foco atual é validar o fluxo das histórias, o funcionamento dos combates, a progressão e o equilíbrio entre as classes e os encontros.

Possíveis melhorias futuras incluem novos inimigos e habilidades, mais itens, ajustes de balanceamento, testes automatizados e melhorias graduais na interface.

**Importante:** cada partida permite jogar uma missão. Ao terminar, reinicie o jogo e crie um novo personagem para conhecer uma das outras histórias.

## 👨‍💻 Sobre o desenvolvimento

Medieval Fightin' é um projeto pessoal desenvolvido por **[Hérico Souza](https://github.com/HericoSouza)** com o objetivo de praticar Python por meio de um jogo construído gradualmente. As mecânicas e os sistemas servem como exercícios práticos de lógica, matemática aplicada e programação orientada a objetos.

Feedback e sugestões são bem-vindos: a ideia da Alpha é aprender, testar, ajustar e evoluir o projeto etapa por etapa.

---

<div align="center">

**Obrigado por conhecer o Medieval Fightin'!** ⚔️

*Uma Alpha em construção — cada batalha é também um aprendizado.*

</div>
