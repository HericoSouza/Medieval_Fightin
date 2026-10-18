import tkinter as tk
from tkinter import ttk, messagebox

from missoes import MISSOES
from criacao_personagem import CriadorPersonagem
from entidades import Companheiro, Boss, InimigoNormal
from combate import SistemaCombate
from progressao import SistemaProgressao


class InterfaceJogo:
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Medieval Fightin' — Alpha")
        self.raiz.geometry("1120x820")
        self.raiz.minsize(900, 680)
        self.raiz.configure(bg="#17191f")
        self.estilo = ttk.Style()
        self.estilo.theme_use("clam")
        self.estilo.configure("Vida.Horizontal.TProgressbar", troughcolor="#343943", background="#a94343", bordercolor="#343943", lightcolor="#a94343", darkcolor="#a94343")
        self.estilo.configure("Mana.Horizontal.TProgressbar", troughcolor="#343943", background="#456fc1", bordercolor="#343943", lightcolor="#456fc1", darkcolor="#456fc1")
        self.estilo.configure("XP.Horizontal.TProgressbar", troughcolor="#343943", background="#b79a4b", bordercolor="#343943", lightcolor="#b79a4b", darkcolor="#b79a4b")
        self.estilo.configure("TCombobox", fieldbackground="#343943", background="#343943", foreground="#eeeeee", arrowcolor="#eeeeee")
        self.estilo.map("TCombobox", fieldbackground=[("readonly", "#343943")], foreground=[("readonly", "#eeeeee")], selectbackground=[("readonly", "#343943")], selectforeground=[("readonly", "#eeeeee")])
        self.personagem = None
        self.companheiro = None
        self.missao = None
        self.chave_missao = None
        self.indice_encontro = 0
        self.batalha = None
        self.companheiro_decidido = False
        self.alvos_por_rotulo = {}
        self.modo = "inicio"
        self.mostrar_inicio()

    def limpar_interface(self):
        for widget in self.raiz.winfo_children():
            widget.destroy()

    def mostrar_inicio(self):
        self.modo = "inicio"
        self.limpar_interface()
        base = tk.Frame(self.raiz, bg="#17191f", padx=36, pady=28)
        base.pack(fill="both", expand=True)
        tk.Label(base, text="MEDIEVAL FIGHTIN'", font=("Georgia", 25, "bold"), fg="#e6d7b0", bg="#17191f").pack(anchor="w")
        tk.Label(base, text="ALPHA  ·  RPG narrativo por turnos", font=("Segoe UI", 11), fg="#aaaeb7", bg="#17191f").pack(anchor="w", pady=(2, 20))

        ficha = tk.Frame(base, bg="#22252d", padx=18, pady=16)
        ficha.pack(fill="x", pady=(0, 14))
        tk.Label(ficha, text="Novo aventureiro", font=("Georgia", 15, "bold"), fg="#e6d7b0", bg="#22252d").grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 12))
        tk.Label(ficha, text="Nome", fg="#eeeeee", bg="#22252d", font=("Segoe UI", 10)).grid(row=1, column=0, sticky="w", padx=(0, 16), pady=5)
        self.entrada_nome = tk.Entry(ficha, font=("Segoe UI", 11), bg="#343943", fg="#ffffff", insertbackground="#ffffff", relief="flat")
        self.entrada_nome.grid(row=1, column=1, sticky="ew", ipady=5, pady=5)
        tk.Label(ficha, text="Classe", fg="#eeeeee", bg="#22252d", font=("Segoe UI", 10)).grid(row=2, column=0, sticky="w", padx=(0, 16), pady=5)
        self.classe_var = tk.StringVar(value="Guerreiro")
        self.classe_combo = ttk.Combobox(ficha, textvariable=self.classe_var, values=("Guerreiro", "Mago", "Arqueiro"), state="readonly", font=("Segoe UI", 10))
        self.classe_combo.grid(row=2, column=1, sticky="ew", pady=5, ipady=3)
        ficha.grid_columnconfigure(1, weight=1)

        tk.Label(base, text="Escolha uma história para esta nova aventura", font=("Georgia", 15, "bold"), fg="#e6d7b0", bg="#17191f").pack(anchor="w", pady=(8, 8))
        conteudo = tk.Frame(base, bg="#17191f")
        conteudo.pack(fill="both", expand=True)
        self.lista_missoes = tk.Listbox(conteudo, height=7, font=("Segoe UI", 11), bg="#22252d", fg="#eeeeee", selectbackground="#75613e", selectforeground="#ffffff", relief="flat", highlightthickness=1, highlightbackground="#343943", activestyle="none")
        self.lista_missoes.pack(side="left", fill="both", expand=True, padx=(0, 14))
        self.chaves_missoes = list(MISSOES.keys())
        for chave in self.chaves_missoes:
            self.lista_missoes.insert("end", MISSOES[chave]["titulo"])
        self.lista_missoes.selection_set(0)
        self.lista_missoes.bind("<<ListboxSelect>>", self.atualizar_descricao_missao)
        self.descricao_missao = tk.Label(conteudo, text="", justify="left", wraplength=330, anchor="nw", font=("Segoe UI", 11), fg="#d0d2d8", bg="#22252d", padx=16, pady=15)
        self.descricao_missao.pack(side="right", fill="both", expand=True)
        self.atualizar_descricao_missao()
        tk.Label(base, text="Cada partida acompanha apenas uma das três histórias. Ao concluir a Alpha, reinicie e crie outro personagem para conhecer as demais.", font=("Segoe UI", 9), fg="#aaaeb7", bg="#17191f", wraplength=940, justify="left").pack(anchor="w", pady=(14, 12))
        tk.Button(base, text="Começar aventura", command=self.iniciar_aventura, font=("Segoe UI", 11, "bold"), bg="#75613e", fg="#ffffff", activebackground="#8d754a", activeforeground="#ffffff", relief="flat", padx=18, pady=10).pack(anchor="e")

    def atualizar_descricao_missao(self, evento=None):
        selecao = self.lista_missoes.curselection()
        if not selecao:
            return
        chave = self.chaves_missoes[selecao[0]]
        missao = MISSOES[chave]
        self.descricao_missao.configure(text=f"{missao['subtitulo']}\n\n{missao['descricao']}\n\nCompanheiro possível: {missao['companheiro']['nome']}.")

    def iniciar_aventura(self):
        nome = self.entrada_nome.get().strip()
        if not nome:
            messagebox.showwarning("Novo aventureiro", "Digite o nome do personagem para continuar.")
            return
        selecao = self.lista_missoes.curselection()
        if not selecao:
            messagebox.showwarning("História", "Selecione uma das três histórias.")
            return
        try:
            self.personagem = CriadorPersonagem.criar_por_dados(nome, self.classe_var.get())
        except ValueError as erro:
            messagebox.showerror("Classe inválida", str(erro))
            return
        self.chave_missao = self.chaves_missoes[selecao[0]]
        self.missao = MISSOES[self.chave_missao]
        self.indice_encontro = 0
        self.companheiro = None
        self.companheiro_decidido = False
        self.batalha = None
        self.mostrar_tela_jogo()
        self.registrar("Bem-vindo ao Medieval Fightin'!\n")
        self.registrar("A aventura começa numa taverna movimentada. O cheiro de comida e cerveja se mistura ao som de conversas, risadas e dados rolando sobre as mesas. Você observa o painel de missões, até perceber que suas últimas moedas não vão durar para sempre.\n")
        self.registrar(f"Ao sair, você encontra o mercador.\n\nO Mercador — {self.personagem.nome}, certo? Um {self.personagem.classe.lower()}... bom, já vi escolhas piores. Tenho alguns itens que podem ajudar. Escolha um, e não me peça crédito depois.\n")
        self.modo = "loja"
        self.mostrar_botoes_loja()
        self.atualizar_status()

    def mostrar_tela_jogo(self):
        self.limpar_interface()
        topo = tk.Frame(self.raiz, bg="#17191f", padx=18, pady=10)
        topo.pack(side="top", fill="x")
        tk.Label(topo, text="MEDIEVAL FIGHTIN'", font=("Georgia", 17, "bold"), fg="#e6d7b0", bg="#17191f").pack(side="left")
        self.missao_label = tk.Label(topo, text=self.missao["titulo"], font=("Segoe UI", 10), fg="#aaaeb7", bg="#17191f")
        self.missao_label.pack(side="right")

        self.acoes_frame = tk.Frame(self.raiz, bg="#17191f", padx=18, pady=10)
        self.acoes_frame.pack(side="bottom", fill="x")

        status = tk.Frame(self.raiz, bg="#17191f", padx=18)
        status.pack(side="bottom", fill="x", pady=(0, 8))
        status.grid_columnconfigure(0, weight=3)
        status.grid_columnconfigure(1, weight=2)
        status.grid_columnconfigure(2, weight=3)

        self.cartao_personagem = self.criar_cartao_status(status, "PERSONAGEM", 0)
        self.cartao_companheiro = self.criar_cartao_status(status, "COMPANHEIRO", 1)
        self.cartao_inimigos = tk.Frame(status, bg="#22252d", padx=12, pady=8, highlightbackground="#343943", highlightthickness=1)
        self.cartao_inimigos.grid(row=0, column=2, sticky="nsew", padx=(5, 0))
        tk.Label(self.cartao_inimigos, text="CAMPO DE BATALHA", font=("Segoe UI", 9, "bold"), fg="#cbb98d", bg="#22252d").pack(anchor="w")
        self.inimigos_label = tk.Label(self.cartao_inimigos, text="Nenhum inimigo presente.", font=("Segoe UI", 9), fg="#eeeeee", bg="#22252d", justify="left", anchor="w", wraplength=320)
        self.inimigos_label.pack(fill="x", anchor="w", pady=(3, 5))
        self.alvo_var = tk.StringVar()
        self.alvo_combo = ttk.Combobox(self.cartao_inimigos, textvariable=self.alvo_var, state="readonly", font=("Segoe UI", 9))
        self.alvo_combo.pack(fill="x")

        historia_frame = tk.Frame(self.raiz, bg="#22252d", padx=12, pady=10)
        historia_frame.pack(side="top", fill="both", expand=True, padx=18, pady=(0, 10))
        tk.Label(historia_frame, text="HISTÓRIA E REGISTRO DA AVENTURA", font=("Segoe UI", 9, "bold"), fg="#cbb98d", bg="#22252d").pack(anchor="w", pady=(0, 6))
        texto_frame = tk.Frame(historia_frame, bg="#22252d")
        texto_frame.pack(fill="both", expand=True)
        barra = ttk.Scrollbar(texto_frame)
        barra.pack(side="right", fill="y")
        self.texto_historia = tk.Text(texto_frame, wrap="word", font=("Georgia", 11), bg="#22252d", fg="#e6e0d5", insertbackground="#ffffff", relief="flat", padx=7, pady=5, spacing1=2, spacing3=5, yscrollcommand=barra.set, state="disabled")
        self.texto_historia.pack(side="left", fill="both", expand=True)
        barra.configure(command=self.texto_historia.yview)
        self.atualizar_status()

    def criar_cartao_status(self, pai, titulo, coluna):
        frame = tk.Frame(pai, bg="#22252d", padx=12, pady=8, highlightbackground="#343943", highlightthickness=1)
        frame.grid(row=0, column=coluna, sticky="nsew", padx=(0 if coluna == 0 else 5, 0))
        tk.Label(frame, text=titulo, font=("Segoe UI", 9, "bold"), fg="#cbb98d", bg="#22252d").pack(anchor="w")
        nome = tk.Label(frame, text="", font=("Segoe UI", 10, "bold"), fg="#ffffff", bg="#22252d", anchor="w")
        nome.pack(fill="x", pady=(3, 1))
        vida_texto = tk.Label(frame, text="Vida", font=("Segoe UI", 8), fg="#d0d2d8", bg="#22252d", anchor="w")
        vida_texto.pack(fill="x")
        vida_barra = ttk.Progressbar(frame, style="Vida.Horizontal.TProgressbar", maximum=100, value=100)
        vida_barra.pack(fill="x", pady=(1, 4))
        mana_texto = tk.Label(frame, text="", font=("Segoe UI", 8), fg="#d0d2d8", bg="#22252d", anchor="w")
        mana_texto.pack(fill="x")
        mana_barra = ttk.Progressbar(frame, style="Mana.Horizontal.TProgressbar", maximum=100, value=100)
        mana_barra.pack(fill="x", pady=(1, 4))
        extra = tk.Label(frame, text="", font=("Segoe UI", 8), fg="#d0d2d8", bg="#22252d", anchor="w", justify="left")
        extra.pack(fill="x")
        return {"frame": frame, "nome": nome, "vida_texto": vida_texto, "vida_barra": vida_barra, "mana_texto": mana_texto, "mana_barra": mana_barra, "extra": extra}

    def registrar(self, texto):
        self.texto_historia.configure(state="normal")
        self.texto_historia.insert("end", texto.rstrip() + "\n\n")
        self.texto_historia.configure(state="disabled")
        self.texto_historia.see("end")

    def atualizar_status(self):
        if self.personagem is None or not hasattr(self, "cartao_personagem"):
            return
        p = self.personagem
        self.cartao_personagem["nome"].configure(text=f"{p.nome} · {p.classe} · Nv. {p.nivel}")
        self.cartao_personagem["vida_texto"].configure(text=f"Vida: {max(0, p.vida)}/{p.vida_maxima}")
        self.cartao_personagem["vida_barra"].configure(maximum=max(1, p.vida_maxima), value=max(0, p.vida))
        self.cartao_personagem["mana_texto"].configure(text=f"Mana: {max(0, p.mana)}/{p.mana_maxima}")
        self.cartao_personagem["mana_barra"].configure(maximum=max(1, p.mana_maxima), value=max(0, p.mana))
        if p.nivel < 5:
            xp_texto = f"XP: {p.experiencia}/{p.experiencia_proximo_nivel}"
            xp_max = max(1, p.experiencia_proximo_nivel)
        else:
            xp_texto = "Nível máximo da Alpha"
            xp_max = 1
        self.cartao_personagem["extra"].configure(text=f"{xp_texto}\nPoções: {p.pocao_cura} cura · {p.pocao_mana} mana\nDefesa: {p.defesa} · Dano extra: +{p.bonus_dano} · Ouro: {p.ouro}")

        if self.companheiro is None:
            self.cartao_companheiro["nome"].configure(text="Você está viajando sozinho")
            self.cartao_companheiro["vida_texto"].configure(text="Vida: —")
            self.cartao_companheiro["vida_barra"].configure(maximum=100, value=0)
            self.cartao_companheiro["mana_texto"].configure(text="Sem companheiro")
            self.cartao_companheiro["mana_barra"].configure(maximum=100, value=0)
            self.cartao_companheiro["extra"].configure(text="Você ainda pode aceitar companhia após o primeiro combate.")
        else:
            c = self.companheiro
            self.cartao_companheiro["nome"].configure(text=f"{c.nome} · {c.titulo}")
            self.cartao_companheiro["vida_texto"].configure(text=f"Vida: {max(0, c.vida)}/{c.vida_maxima}")
            self.cartao_companheiro["vida_barra"].configure(maximum=max(1, c.vida_maxima), value=max(0, c.vida))
            self.cartao_companheiro["mana_texto"].configure(text="Pronto para lutar" if c.vida > 0 else "Fora de combate")
            self.cartao_companheiro["mana_barra"].configure(maximum=100, value=100 if c.vida > 0 else 0)
            self.cartao_companheiro["extra"].configure(text=f"Ataque: {c.dano[0]}–{c.dano[1]}\nTécnica: {c.especial}")

        if self.batalha is not None:
            vivos = self.batalha.inimigos_vivos()
            linhas = []
            for inimigo in vivos:
                if inimigo.montaria_ativa:
                    linhas.append(f"• {inimigo.nome}: {inimigo.vida}/{inimigo.vida_maxima} PV | {inimigo.montaria['nome']}: {inimigo.montaria_vida}/{inimigo.montaria_vida_maxima} PV")
                else:
                    categoria = "Boss" if inimigo.categoria == "Boss" else "Inimigo"
                    linhas.append(f"• {inimigo.nome} ({categoria}): {inimigo.vida}/{inimigo.vida_maxima} PV")
            self.inimigos_label.configure(text="\n".join(linhas) if linhas else "Todos os inimigos foram derrotados.")
            self.atualizar_lista_alvos()
        else:
            self.inimigos_label.configure(text="Nenhum combate em andamento.")
            self.alvo_combo.configure(values=())
            self.alvo_var.set("")

    def atualizar_lista_alvos(self):
        if self.batalha is None:
            return
        alvos = self.batalha.obter_alvos()
        self.alvos_por_rotulo = {rotulo: (inimigo, parte) for inimigo, parte, rotulo in alvos}
        rotulos = list(self.alvos_por_rotulo.keys())
        selecionado = self.alvo_var.get()
        self.alvo_combo.configure(values=rotulos)
        if selecionado not in self.alvos_por_rotulo:
            self.alvo_var.set(rotulos[0] if rotulos else "")

    def limpar_acoes(self):
        for widget in self.acoes_frame.winfo_children():
            widget.destroy()

    def adicionar_botao(self, texto, comando, destaque=False):
        cor = "#75613e" if destaque else "#343943"
        botao = tk.Button(self.acoes_frame, text=texto, command=comando, font=("Segoe UI", 9, "bold" if destaque else "normal"), bg=cor, fg="#ffffff", activebackground="#8d754a", activeforeground="#ffffff", relief="flat", padx=12, pady=9, wraplength=175)
        botao.pack(side="left", padx=(0, 7), pady=2, fill="x", expand=True)

    def mostrar_botoes_loja(self):
        self.limpar_acoes()
        tk.Label(self.acoes_frame, text="Escolha um benefício inicial:", fg="#e6d7b0", bg="#17191f", font=("Segoe UI", 10, "bold")).pack(anchor="w", pady=(0, 6))
        self.adicionar_botao("3 poções de cura + 3 de mana", lambda: self.escolher_item_mercador("pocoes"), True)
        self.adicionar_botao("Arma reforçada (+5 dano)", lambda: self.escolher_item_mercador("arma"))
        self.adicionar_botao("Vestimenta resistente (+20 vida, +1 defesa)", lambda: self.escolher_item_mercador("armadura"))

    def escolher_item_mercador(self, item):
        if item == "pocoes":
            self.personagem.pocao_cura += 3
            self.personagem.pocao_mana += 3
            mensagem = "Você escolheu as poções extras. O mercador coloca três frascos de cada tipo na sua mochila."
        elif item == "arma":
            self.personagem.bonus_dano += 5
            mensagem = "Você escolheu a arma reforçada. O mercador testa o fio e a coloca em suas mãos."
        else:
            self.personagem.vida_maxima += 20
            self.personagem.vida += 20
            self.personagem.defesa += 1
            mensagem = "Você escolheu a vestimenta resistente. O couro reforçado parece pesado, mas deve segurar um golpe ou dois."
        self.registrar(mensagem)
        self.registrar(f"{self.missao['titulo']}\n\n{self.missao['introducao']}")
        self.atualizar_status()
        self.mostrar_intro_encontro()

    def mostrar_intro_encontro(self):
        encontro = self.missao["encontros"][self.indice_encontro]
        self.modo = "historia"
        self.registrar(encontro["titulo"])
        self.registrar(encontro["intro"])
        self.limpar_acoes()
        self.adicionar_botao("Iniciar combate", self.iniciar_combate, True)

    def criar_inimigos_encontro(self, encontro):
        inimigos = []
        tipo_encontro = encontro["tipo"]
        for spec in encontro["inimigos"]:
            montaria = spec.get("montaria")
            defesa = spec.get("defesa", 0)
            especial = spec.get("especial")
            if tipo_encontro in ("mini_boss", "boss"):
                inimigo = Boss(spec["nome"], spec["tipo"], spec["vida"], tuple(spec["dano"]), spec.get("ataque", "Ataque"), defesa, especial)
            else:
                inimigo = InimigoNormal(spec["nome"], spec["tipo"], spec["vida"], tuple(spec["dano"]), spec.get("ataque", "Ataque"), montaria, defesa, especial)
            inimigos.append(inimigo)
        return inimigos

    def iniciar_combate(self):
        encontro = self.missao["encontros"][self.indice_encontro]
        inimigos = self.criar_inimigos_encontro(encontro)
        self.batalha = SistemaCombate(self.personagem, self.companheiro, inimigos)
        self.modo = "combate"
        self.registrar("O confronto começa. Escolha um alvo e selecione sua ação.")
        self.atualizar_status()
        self.mostrar_botoes_combate()

    def mostrar_botoes_combate(self):
        self.limpar_acoes()
        self.adicionar_botao("Ataque básico", lambda: self.executar_acao("basico"), True)
        self.adicionar_botao("Ataque especial", lambda: self.executar_acao("especial"))
        self.adicionar_botao("Habilidade", lambda: self.executar_acao("habilidade"))
        self.adicionar_botao("Poção de cura", lambda: self.executar_acao("cura"))
        self.adicionar_botao("Poção de mana", lambda: self.executar_acao("mana"))

    def executar_acao(self, acao):
        if self.batalha is None or self.modo != "combate":
            return
        alvo = self.alvos_por_rotulo.get(self.alvo_var.get())
        mensagens, resultado = self.batalha.executar_acao(acao, alvo)
        for mensagem in mensagens:
            self.registrar(mensagem)
        self.atualizar_status()
        if resultado == "vitoria":
            self.finalizar_encontro()
        elif resultado == "derrota":
            self.finalizar_derrota()

    def finalizar_encontro(self):
        encontro = self.missao["encontros"][self.indice_encontro]
        self.modo = "pos_combate"
        self.registrar(f"Vitória: {encontro['titulo']}.")
        sistema_progressao = SistemaProgressao()
        for mensagem in sistema_progressao.conceder_experiencia(self.personagem, encontro["xp"]):
            self.registrar(mensagem)
        loot = encontro["loot"]
        self.registrar(f"Loot encontrado: {loot['nome']}. {loot['texto']}")
        efeitos = sistema_progressao.aplicar_loot(self.personagem, loot)
        if efeitos:
            self.registrar("Efeitos: " + "; ".join(efeitos) + ".")
        if self.indice_encontro < 6:
            for mensagem in sistema_progressao.recuperar_entre_encontros(self.personagem, self.companheiro):
                self.registrar(mensagem)
        self.batalha = None
        self.atualizar_status()
        if self.indice_encontro == 0 and not self.companheiro_decidido:
            self.mostrar_oferta_companheiro()
        elif self.indice_encontro == 6:
            self.mostrar_fim_alpha()
        else:
            self.limpar_acoes()
            self.adicionar_botao("Continuar história", self.continuar_historia, True)

    def mostrar_oferta_companheiro(self):
        dados = self.missao["companheiro"]
        self.modo = "companheiro"
        self.registrar(dados["dialogo"])
        self.registrar("Você quer que essa pessoa acompanhe sua aventura? O companheiro agirá logo depois de você em cada turno.")
        self.limpar_acoes()
        self.adicionar_botao(f"Aceitar companhia: {dados['nome']}", self.aceitar_companheiro, True)
        self.adicionar_botao("Agradecer e seguir sozinho", self.recusar_companheiro)

    def aceitar_companheiro(self):
        dados = self.missao["companheiro"]
        self.companheiro = Companheiro(
            dados["nome"],
            dados["titulo"],
            dados["vida"],
            tuple(dados["dano"]),
            tuple(dados["dano_especial"]),
            dados["especial"],
            dados["personalidade"]
        )
        self.companheiro_decidido = True
        self.registrar(dados["aceitar"])
        self.registrar(dados["personalidade"])
        self.atualizar_status()
        self.avancar_encontro()

    def recusar_companheiro(self):
        dados = self.missao["companheiro"]
        self.companheiro_decidido = True
        self.registrar(dados["recusar"])
        self.avancar_encontro()

    def continuar_historia(self):
        self.avancar_encontro()

    def avancar_encontro(self):
        if self.indice_encontro >= 6:
            self.mostrar_fim_alpha()
            return
        self.indice_encontro += 1
        self.mostrar_intro_encontro()

    def mostrar_fim_alpha(self):
        self.modo = "fim"
        self.batalha = None
        self.registrar(self.missao["final"])
        self.registrar("FIM DA ALPHA\n\nVocê concluiu esta história. Para conhecer as outras histórias, reinicie o jogo e crie um novo personagem. Cada partida permite explorar apenas uma das três missões nesta versão Alpha.")
        self.limpar_acoes()
        self.adicionar_botao("Reiniciar e criar novo personagem", self.mostrar_inicio, True)
        self.adicionar_botao("Sair", self.raiz.destroy)
        self.atualizar_status()

    def finalizar_derrota(self):
        self.modo = "derrota"
        self.batalha = None
        self.registrar("Você caiu em combate. A jornada termina aqui, mas a Alpha ainda está aberta para novos testes. Reinicie para criar outro personagem e tentar novamente.")
        self.limpar_acoes()
        self.adicionar_botao("Reiniciar e criar novo personagem", self.mostrar_inicio, True)
        self.adicionar_botao("Sair", self.raiz.destroy)
        self.atualizar_status()


def iniciar_interface():
    raiz = tk.Tk()
    InterfaceJogo(raiz)
    raiz.mainloop()
