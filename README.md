# Medieval Fightin' 🗡️🔥

> *"Medieval Fightin' é um jogo feito inteiramente por mim, como uma forma de estudo da linguagem de Python. Ele é um simulador de combate, utilizando apenas texto para suas representações gráficas."*

---

> [!WARNING]
> Como este jogo foi desenvolvido exclusivamente com o objetivo de **aprendizado e prática da linguagem Python**, o sistema de combate atualmente **não está balanceado** e continuará passando por ajustes e balanceamentos de atributos, danos e habilidades ao longo do tempo.

---

## 📋 Sobre o Jogo

**Medieval Fightin'** é um jogo de estratégia em turnos desenvolvido via terminal. O projeto funciona como um simulador de combate textual onde o jogador cria um personagem com classe própria e enfrenta vilões em uma batalha com gerenciamento de recursos, mecânicas de efeitos de status e eventos imprevisíveis no meio do combate.

---

## 🎮 Funcionalidades e Mecânicas

* **Criação de Personagem Personalizada:** Escolha o nome e a classe do seu herói:
  * **Guerreiro:** Alta vida e uso de *Modo Berserker* para potencializar ataques.
  * **Mago:** Alta mana e feitiços de dano massivo (*Meteoro Arcano*, *Raio de Gelo*).
  * **Arqueiro:** Equilíbrio de atributos e capacidade de envenenar inimigos.
* **Variedade de Inimigos:**
  * **Dragão:** Voa para se curar/proteger e ataca com sopros de fogo devastadores.
  * **Bruxo:** Invoca esqueletos e realiza rituais para trazer o *Ancião Antigo* à batalha.
  * **Goblin:** Capaz de roubar e utilizar habilidades especiais lendárias.
* **Sistema de Combate Dinâmico:**
  * Interface totalmente textual via terminal com limpeza automática de tela.
  * Gestão de **Mana** e **Vida** com uso estratégico de poções.
  * **Efeitos de Status (Condições):** Sangramento, envenenamento e congelamento que afetam diretamente o turno dos combatentes.
  * **Invocação do Ancião:** Um terceiro combatente imprevisível que entra na luta e pode atacar tanto o herói quanto o vilão.

---

## 📁 Estrutura do Projeto

```text
.
├── Medieval Fightin'.py   # Arquivo principal (Ponto de entrada do jogo)
├── criacao_personagem.py # Lógica de criação de classe e atributos do herói
├── criacao_vilao.py      # Lógica de criação dos inimigos (Dragão, Bruxo, Goblin)
├── combate.py            # Motor principal do combate e alternância de turnos
├── condicao.py           # Processamento dos efeitos de status (Veneno, Sangramento, etc.)
└── oanciao.py            # Estrutura de dados e atributos do Ancião
