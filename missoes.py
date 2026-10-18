MISSOES = {
    "goblins": {
        "titulo": "A Gangue do Dente Partido",
        "subtitulo": "Uma região aterrorizada por saqueadores",
        "descricao": "Investigue os ataques às vilas e acabe com a gangue de goblins.",
        "introducao": "Há semanas, vilas inteiras são saqueadas durante a noite. Os sobreviventes falam de goblins organizados, mercenários a soldo e carroças cheias de espólios. O nome da gangue é Dente Partido. O mercador conhece a estrada por onde eles costumam passar, mas aconselha você a não confundir coragem com imprudência.",
        "companheiro": {
            "nome": "Aiko Suzuki",
            "titulo": "Ronin das Duas Katanas",
            "vida": 125,
            "dano": (15, 22),
            "dano_especial": (25, 34),
            "especial": "Corte Cruzado",
            "personalidade": "Aiko é uma ronin japonesa, reservada no primeiro contato, espirituosa quando ganha confiança e sempre atenta às saídas. A máscara de oni cobre parte do rosto; as duas katanas nunca deixam de estar ao alcance das mãos.",
            "dialogo": "Aiko Suzuki limpa uma das katanas na manga do casaco. — Você também está atrás do Dente Partido? Ótimo. Eles levaram comida, dinheiro e gente da minha última vila. Eu luto melhor acompanhada, mas não preciso que ninguém me salve. Se formos juntos, cubra meu lado esquerdo.",
            "aceitar": "Aiko ajeita a máscara de oni. — Fechado. Eu vou logo depois de você. E tente não acertar minhas katanas; elas custaram caro.",
            "recusar": "Aiko dá de ombros, sem se ofender. — Certo. Se mudar de ideia, estarei seguindo as mesmas pegadas. Não faça nada heroico demais."
        },
        "encontros": [
            {
                "titulo": "1. Saqueadores da estrada",
                "tipo": "combate",
                "intro": "A estrada termina numa carroça tombada. Três goblins discutem sobre quem ficará com uma caixa de provisões. Um deles percebe sua presença e ergue uma faca torta. — Olha só, a entrega veio andando! Peguem tudo e deixem o resto para os corvos!",
                "xp": 35,
                "inimigos": [
                    {"nome": "Batedor goblin", "tipo": "goblin", "vida": 38, "dano": [5, 9], "ataque": "Faca de saqueador"},
                    {"nome": "Saqueador goblin", "tipo": "goblin", "vida": 42, "dano": [5, 9], "ataque": "Porrete curto"},
                    {"nome": "Atirador goblin", "tipo": "goblin_atirador", "vida": 34, "dano": [6, 10], "ataque": "Funda de pedra"}
                ],
                "loot": {"nome": "Bolsa de moedas roubadas", "texto": "Entre os espólios, você encontra uma bolsa que os goblins ainda não dividiram.", "efeitos": {"ouro": 15}}
            },
            {
                "titulo": "2. Caçadores montados",
                "tipo": "combate",
                "intro": "O caminho atravessa uma planície seca. Dois goblins avançam montados em javalis de guerra, rindo enquanto fazem as criaturas revirarem a terra. — Quem chegar primeiro fica com as botas do viajante! — grita um deles. As montarias são rápidas, mas parecem mais assustadas do que leais.",
                "xp": 50,
                "inimigos": [
                    {"nome": "Goblin montado 1", "tipo": "goblin_montado", "vida": 46, "dano": [7, 11], "ataque": "Lança curta", "montaria": {"nome": "Javali de guerra 1", "vida": 30}},
                    {"nome": "Goblin montado 2", "tipo": "goblin_montado", "vida": 46, "dano": [7, 11], "ataque": "Lança curta", "montaria": {"nome": "Javali de guerra 2", "vida": 30}}
                ],
                "loot": {"nome": "Fivela de aço", "texto": "Uma fivela de mercenário, bem melhor que os equipamentos dos goblins, ainda está presa à sela abandonada.", "efeitos": {"defesa": 1}}
            },
            {
                "titulo": "3. Lâminas a soldo",
                "tipo": "combate",
                "intro": "Perto de uma ponte, você encontra um acampamento improvisado. Os homens ali não usam os trapos dos goblins: são mercenários equipados e pagos para manter a estrada fechada. O capitão gira uma moeda entre os dedos. — Não temos nada contra você. Mas fomos pagos para que não passe. Isso costuma resolver a conversa.",
                "xp": 75,
                "inimigos": [
                    {"nome": "Mercenário espadachim", "tipo": "mercenario", "vida": 58, "dano": [8, 13], "ataque": "Espada de aluguel", "defesa": 1},
                    {"nome": "Mercenário besteiro", "tipo": "mercenario_atirador", "vida": 48, "dano": [8, 12], "ataque": "Besta leve"}
                ],
                "loot": {"nome": "Estojo de primeiros socorros", "texto": "O estojo dos mercenários contém um frasco intacto e algumas ataduras.", "efeitos": {"pocao_cura": 1}}
            },
            {
                "titulo": "4. Mini-Boss: O prisioneiro quebrou as correntes",
                "tipo": "mini_boss",
                "intro": "O acampamento principal fica numa pedreira. Lá, a gangue mantinha um troll capturado para abrir portões e intimidar aldeões. Agora as correntes estão partidas e os goblins jazem espalhados pelo chão. A criatura vira para você, ofegante. — Mais um pequeno que veio pôr uma corrente em mim? Então venha tentar.",
                "xp": 125,
                "inimigos": [
                    {"nome": "Brakk, o Troll Cativo", "tipo": "troll", "vida": 225, "dano": [12, 19], "ataque": "Porrete de pedreira", "especial": "Fúria da pedreira", "defesa": 2}
                ],
                "loot": {"nome": "Amuleto de pedra rachada", "texto": "O troll deixa para trás um amuleto antigo. Você o prende ao equipamento; a pedra absorve parte do impacto dos golpes.", "efeitos": {"defesa": 1, "pocao_mana": 1}}
            },
            {
                "titulo": "5. A guarda de elite",
                "tipo": "combate",
                "intro": "A trilha leva a uma fortificação feita com carroças saqueadas. Dois goblins vestem armaduras humanas remendadas e carregam armas melhores do que deveriam ter. Um deles aponta a lâmina para você. — O chefe não quer visitas. E nós queremos nosso pagamento, então facilite as coisas.",
                "xp": 95,
                "inimigos": [
                    {"nome": "Veterano do Dente Partido", "tipo": "goblin_elite", "vida": 78, "dano": [10, 15], "ataque": "Machado reforçado", "defesa": 2},
                    {"nome": "Guarda de escudo", "tipo": "goblin_elite", "vida": 86, "dano": [9, 14], "ataque": "Golpe de escudo", "defesa": 3}
                ],
                "loot": {"nome": "Machado de aço goblin", "texto": "O armamento do veterano está bem equilibrado. Você consegue reaproveitar o aço para reforçar seu próprio dano.", "efeitos": {"bonus_dano": 3}}
            },
            {
                "titulo": "6. O exército do Dente Partido",
                "tipo": "combate",
                "intro": "Atrás das paliçadas, o acampamento inteiro se mobiliza. Goblins correm entre tendas, carregam escudos de madeira e tentam formar uma linha de defesa. O número deles impressiona, mas a disciplina é fraca. Aiko, se estiver com você, respira fundo: — Não deixe que nos cerquem. Quebremos a linha e sigamos em frente.",
                "xp": 130,
                "inimigos": [
                    {"nome": "Soldado goblin 1", "tipo": "goblin_soldado", "vida": 42, "dano": [6, 10], "ataque": "Lança de campanha"},
                    {"nome": "Soldado goblin 2", "tipo": "goblin_soldado", "vida": 42, "dano": [6, 10], "ataque": "Lança de campanha"},
                    {"nome": "Soldado goblin 3", "tipo": "goblin_soldado", "vida": 42, "dano": [6, 10], "ataque": "Arco curto"},
                    {"nome": "Soldado goblin 4", "tipo": "goblin_soldado", "vida": 42, "dano": [6, 10], "ataque": "Porrete de guerra"}
                ],
                "loot": {"nome": "Carroça de suprimentos", "texto": "Depois do confronto, você separa os mantimentos que ainda podem ser usados.", "efeitos": {"pocao_cura": 1, "pocao_mana": 1, "ouro": 20}}
            },
            {
                "titulo": "7. Boss: O Goblin-Chefe",
                "tipo": "boss",
                "intro": "No centro do acampamento, o Goblin-Chefe está sentado sobre um trono feito de portas roubadas. Ele levanta, decepcionado com a queda de seu exército. — Todas aquelas vilas, todo aquele ouro… e vocês aparecem para estragar meu futuro? Eu mesmo vou acabar com isso!",
                "xp": 240,
                "inimigos": [
                    {"nome": "Grishnak, o Dente Partido", "tipo": "goblin_chefe", "vida": 350, "dano": [14, 21], "ataque": "Machado do chefe", "especial": "Comando brutal", "defesa": 2}
                ],
                "loot": {"nome": "Tesouro do Dente Partido", "texto": "O tesouro do chefe permite comprar mantimentos para os sobreviventes e reforçar seu equipamento.", "efeitos": {"bonus_dano": 4, "ouro": 65}}
            }
        ],
        "final": "Com Grishnak derrotado, os goblins perdem o comando e se dispersam. As vilas ainda terão muito a reconstruir, mas as estradas voltam a pertencer aos viajantes. Aiko guarda as katanas e olha para o horizonte. — Não foi uma má jornada. Para alguém que quase me acertou duas vezes, até que você aprende rápido."
    },
    "culto": {
        "titulo": "O Culto sob as Lápides",
        "subtitulo": "Uma investigação entre túmulos violados e magia antiga",
        "descricao": "Siga os ladrões de túmulos até um culto que serve a uma criatura ancestral.",
        "introducao": "O cemitério de Santa Vigília foi violado em várias noites seguidas. No começo, acreditaram que fossem ladrões atrás de joias. Depois, os túmulos vazios começaram a caminhar. Um padre desesperado entrega a você uma página arrancada de um livro funerário. Há um nome escrito no rodapé: o Bruxo que lidera o culto.",
        "companheiro": {
            "nome": "Joseph Valentine",
            "titulo": "Mágico de Rua do Véu",
            "vida": 112,
            "dano": (13, 20),
            "dano_especial": (23, 32),
            "especial": "Dobra Espacial",
            "personalidade": "Joseph Valentine é um mágico de rua inglês de sorriso fácil, luvas gastas e truques que às vezes desafiam a lógica. Ele dobra pequenos trechos do espaço para desviar ataques ou fazer uma lâmina surgir onde ninguém esperava.",
            "dialogo": "Um homem de cartola bate as mãos, e uma moeda desaparece entre elas. — Joseph Valentine, ilusionista, prestidigitador e, aparentemente, o único sujeito sóbrio neste cemitério. Aquilo ali não é uma encenação. Se você vai atrás do culto, eu vou junto. Quero descobrir quem está puxando as cordas antes que alguém transforme minha cabeça em decoração de túmulo.",
            "aceitar": "Joseph abre um sorriso. — Excelente! Você cuida da parte de apanhar de coisas mortas; eu cuido de fazer o espaço se arrepender de existir. Depois discutimos a divisão do mérito.",
            "recusar": "Joseph faz uma reverência exagerada. — Como preferir. Vou manter uma distância respeitável. Quer dizer, uma distância espacialmente respeitável. Nunca sei onde vou parar."
        },
        "encontros": [
            {
                "titulo": "1. Ladrões entre os túmulos",
                "tipo": "combate",
                "intro": "À luz de lanternas cobertas, três ladrões tentam retirar um caixão de uma cripta. Um deles segura um saco de joias, outro usa uma pá como arma. — Não é o que parece! — diz o terceiro. Ele olha para os cadáveres espalhados. — Certo, é exatamente o que parece. Não deixaremos testemunhas.",
                "xp": 35,
                "inimigos": [
                    {"nome": "Arrombador de túmulos", "tipo": "ladrao", "vida": 36, "dano": [5, 8], "ataque": "Pá curta"},
                    {"nome": "Coveiro corrupto", "tipo": "ladrao", "vida": 40, "dano": [5, 9], "ataque": "Faca de trabalho"},
                    {"nome": "Ladrão de relíquias", "tipo": "ladrao_atirador", "vida": 32, "dano": [5, 8], "ataque": "Besta improvisada"}
                ],
                "loot": {"nome": "Bolsa de joias funerárias", "texto": "Você recolhe as moedas que não pertencem aos mortos e guarda o restante para devolver às famílias.", "efeitos": {"ouro": 18}}
            },
            {
                "titulo": "2. A última defesa dos ladrões",
                "tipo": "combate",
                "intro": "Encurralado, o líder dos ladrões puxa uma corrente presa ao altar. Símbolos escuros brilham nas lápides e três esqueletos se levantam. — Eu disse que tinha um plano B! — ele grita, já correndo para longe. Os mortos não parecem interessados em distinguir culpados de curiosos.",
                "xp": 50,
                "inimigos": [
                    {"nome": "Esqueleto da cripta 1", "tipo": "esqueleto", "vida": 40, "dano": [6, 10], "ataque": "Garras ósseas"},
                    {"nome": "Esqueleto da cripta 2", "tipo": "esqueleto", "vida": 40, "dano": [6, 10], "ataque": "Espada funerária"},
                    {"nome": "Esqueleto da cripta 3", "tipo": "esqueleto", "vida": 40, "dano": [6, 10], "ataque": "Mandíbula cerrada"}
                ],
                "loot": {"nome": "Frasco de éter", "texto": "Entre os pertences dos ladrões há um tônico que recupera a concentração mágica.", "efeitos": {"pocao_mana": 1}}
            },
            {
                "titulo": "3. Os fiéis do véu negro",
                "tipo": "combate",
                "intro": "Uma escadaria escondida leva a uma câmara sob o cemitério. Cultistas encapuzados desenham círculos ao redor de ossos antigos. Uma mulher fecha o livro quando vê você. — O ciclo está quase completo. Não vamos permitir que um estranho interrompa aquilo que nem os reis conseguiram destruir.",
                "xp": 75,
                "inimigos": [
                    {"nome": "Acólito do véu", "tipo": "cultista", "vida": 46, "dano": [7, 11], "ataque": "Punhal ritual"},
                    {"nome": "Devoto das cinzas", "tipo": "cultista", "vida": 50, "dano": [7, 11], "ataque": "Estilhaço sombrio"},
                    {"nome": "Guardião do círculo", "tipo": "cultista", "vida": 48, "dano": [7, 12], "ataque": "Bastão cerimonial"}
                ],
                "loot": {"nome": "Símbolo de proteção funerária", "texto": "O símbolo perde o brilho maligno e se transforma num pequeno talismã protetor.", "efeitos": {"defesa": 1, "pocao_cura": 1}}
            },
            {
                "titulo": "4. Mini-Boss: O Médico da Peste",
                "tipo": "mini_boss",
                "intro": "O corredor termina num consultório improvisado. Frascos borbulham sobre mesas, e um homem com máscara de bico separa instrumentos ensanguentados. — Finalmente, um paciente que veio por vontade própria. Não se preocupe: a dor é apenas uma informação que o corpo ainda não aprendeu a interpretar.",
                "xp": 125,
                "inimigos": [
                    {"nome": "Doutor Malrec, o Médico da Peste", "tipo": "medico_peste", "vida": 215, "dano": [10, 17], "ataque": "Bisturi contaminado", "especial": "Névoa pestilenta", "defesa": 1}
                ],
                "loot": {"nome": "Máscara filtrante", "texto": "A máscara do médico foi limpa de seus encantamentos. Você aproveita os filtros e as tiras resistentes para reforçar sua proteção.", "efeitos": {"defesa": 2, "pocao_cura": 1}}
            },
            {
                "titulo": "5. A festa dos que não respiram",
                "tipo": "combate",
                "intro": "Além do consultório, uma sala decorada com lanternas de abóbora parece uma celebração grotesca. Um zumbi cambaleia para fora de um armário; uma múmia se ergue de uma mesa; uma criatura costurada solta um gemido metálico. Joseph, se estiver com você, suspira: — Já fiz festas piores. Nenhuma tinha tantos convidados mortos.",
                "xp": 95,
                "inimigos": [
                    {"nome": "Zumbi da festa", "tipo": "zumbi", "vida": 58, "dano": [8, 12], "ataque": "Mordida apodrecida"},
                    {"nome": "Jackenstein", "tipo": "jackenstein", "vida": 78, "dano": [10, 15], "ataque": "Punhos costurados", "defesa": 1},
                    {"nome": "Múmia errante", "tipo": "mumia", "vida": 62, "dano": [8, 13], "ataque": "Faixas sufocantes"}
                ],
                "loot": {"nome": "Caixa de tônicos", "texto": "A caixa contém dois frascos guardados para os membros mais importantes do culto.", "efeitos": {"pocao_mana": 1, "pocao_cura": 1}}
            },
            {
                "titulo": "6. O vice-líder do culto",
                "tipo": "combate",
                "intro": "Uma porta de ferro abre para uma biblioteca subterrânea. O vice-líder do culto, Edric Voss, espera diante de um livro acorrentado. — Malrec falhou, então? Que pena. Ele sempre foi muito dedicado aos detalhes. Eu, por outro lado, prefiro resultados. E o meu mestre está prestes a acordar.",
                "xp": 130,
                "inimigos": [
                    {"nome": "Edric Voss, vice-líder", "tipo": "vice_culto", "vida": 175, "dano": [12, 18], "ataque": "Lâmina ritual", "especial": "Maldição curta", "defesa": 1}
                ],
                "loot": {"nome": "Chave de osso negro", "texto": "A chave abre a última porta e traz um encantamento útil para suas armas.", "efeitos": {"bonus_dano": 3, "ouro": 25}}
            },
            {
                "titulo": "7. Boss: O Bruxo Necromante",
                "tipo": "boss",
                "intro": "No coração do santuário, o Bruxo está ajoelhado diante de uma fenda sem fundo. Uma voz antiga pulsa do outro lado. Ele se vira com calma. — Você não compreende o que tenta impedir. A morte não é uma prisão; é uma porta. E eu serei lembrado como aquele que a abriu.",
                "xp": 240,
                "inimigos": [
                    {"nome": "Valerius Noct, o Necromante", "tipo": "necromante", "vida": 360, "dano": [14, 22], "ataque": "Magia macabra", "especial": "Sifão de almas", "defesa": 2}
                ],
                "loot": {"nome": "Tomo do Limiar", "texto": "O tomo para de sussurrar quando o Bruxo cai. Suas páginas restantes contêm fórmulas para ampliar sua reserva mágica.", "efeitos": {"mana_maxima": 25, "bonus_dano": 3}}
            }
        ],
        "final": "O ritual se desfaz, e a presença do outro lado da fenda desaparece nas profundezas. Os mortos voltam ao silêncio. Joseph gira a cartola entre os dedos. — Bem, isso certamente não estava no programa. Se alguém perguntar, foi uma apresentação privada e absolutamente sem reembolso."
    },
    "cinzas": {
        "titulo": "A Lenda das Cinzas",
        "subtitulo": "Os mortos despertam enquanto uma prisão antiga enfraquece",
        "descricao": "Descubra por que os esqueletos estão evoluindo e enfrente a linhagem de Vharzun.",
        "introducao": "Há séculos, Vharzun, o Devorador de Brasas, foi aprisionado sob o Monte Escarlate. Agora, animais desaparecem, guerreiros mortos se levantam e vilarejos amanhecem cobertos de cinzas. As primeiras criaturas vistas nas estradas eram esqueletos comuns. As mais recentes carregam armaduras e brasas nas órbitas. Algo está chamando os mortos para a montanha.",
        "companheiro": {
            "nome": "Kaleb Johnson",
            "titulo": "Lanceiro da Fronteira",
            "vida": 135,
            "dano": (16, 23),
            "dano_especial": (27, 36),
            "especial": "Estocada do Trovão",
            "personalidade": "Kaleb Johnson é um lanceiro bruto, carismático e barulhento, com um senso de humor difícil de silenciar. Por trás das piadas e dos ombros largos, ele conhece as lendas da fronteira e não abandona quem luta ao seu lado.",
            "dialogo": "Um lanceiro sentado sobre uma pedra se levanta com um estalo nas costas. — Kaleb Johnson. Eu ia dizer que sou o melhor lanceiro desta região, mas meu último torneio terminou com uma cabra roubando meu almoço. Então digamos que sou o segundo melhor. Estou indo atrás das cinzas que cobriram minha aldeia. Você parece precisar de uma lança extra. E de piadas melhores.",
            "aceitar": "Kaleb gira a lança e quase deixa a ponta cair no próprio pé. — Perfeito! Eu vou logo depois de você. Se aparecer um dragão, tente mantê-lo ocupado enquanto eu invento um plano brilhante. Ou um plano. Qualquer plano.",
            "recusar": "Kaleb dá uma risada curta. — Justo. Vou seguir por perto, então. Se ouvir alguém contando uma piada muito boa, provavelmente sou eu. Se for muito ruim, também sou eu."
        },
        "encontros": [
            {
                "titulo": "1. Ossos na estrada velha",
                "tipo": "combate",
                "intro": "Ao pôr do sol, três esqueletos emergem de uma vala coberta de cinzas. Restos de uniformes indicam que foram soldados de uma guerra antiga. Um deles ainda segura uma espada partida. O som dos ossos se chocando parece responder a um chamado que vem da montanha.",
                "xp": 35,
                "inimigos": [
                    {"nome": "Esqueleto errante 1", "tipo": "esqueleto", "vida": 35, "dano": [5, 8], "ataque": "Espada partida"},
                    {"nome": "Esqueleto errante 2", "tipo": "esqueleto", "vida": 35, "dano": [5, 8], "ataque": "Garras ósseas"},
                    {"nome": "Esqueleto errante 3", "tipo": "esqueleto", "vida": 35, "dano": [5, 8], "ataque": "Escudo rachado"}
                ],
                "loot": {"nome": "Broche do vigia", "texto": "O broche de um antigo sentinela ainda contém uma pequena proteção contra impactos.", "efeitos": {"defesa": 1}}
            },
            {
                "titulo": "2. Flechas sem arqueiro",
                "tipo": "combate",
                "intro": "A estrada passa por uma torre de vigia abandonada. Flechas de osso atingem a terra antes que você veja os arqueiros: dois esqueletos estão presos às ameias, movendo-se como se uma mão invisível puxasse seus braços. Kaleb, se estiver com você, se esconde atrás de uma pedra. — Não gosto de inimigos que continuam de serviço depois de mortos. Péssima ética de trabalho.",
                "xp": 50,
                "inimigos": [
                    {"nome": "Arqueiro ósseo 1", "tipo": "arqueiro_osseo", "vida": 44, "dano": [7, 11], "ataque": "Flecha de osso"},
                    {"nome": "Arqueiro ósseo 2", "tipo": "arqueiro_osseo", "vida": 44, "dano": [7, 11], "ataque": "Flecha de osso"}
                ],
                "loot": {"nome": "Aljava encantada", "texto": "As flechas se desfazem, mas o estojo mantém uma energia que reforça os ataques.", "efeitos": {"bonus_dano": 2, "pocao_cura": 1}}
            },
            {
                "titulo": "3. Guardiões revestidos",
                "tipo": "combate",
                "intro": "Perto da entrada da montanha, dois guerreiros esqueléticos vestem placas de armadura soldadas aos ossos. Brasas brilham por baixo das costelas. Não há comando verbal, apenas o ruído sincronizado de duas espadas sendo erguidas ao mesmo tempo.",
                "xp": 75,
                "inimigos": [
                    {"nome": "Guardião de costelas de ferro", "tipo": "esqueleto_armadurado", "vida": 58, "dano": [8, 12], "ataque": "Espada carbonizada", "defesa": 2},
                    {"nome": "Guardião da brasa fria", "tipo": "esqueleto_armadurado", "vida": 58, "dano": [8, 12], "ataque": "Lâmina de fuligem", "defesa": 2}
                ],
                "loot": {"nome": "Núcleo de osso incandescente", "texto": "O núcleo pulsa uma última vez e libera energia que pode ser armazenada em uma poção.", "efeitos": {"pocao_mana": 1}}
            },
            {
                "titulo": "4. Mini-Boss: Vharjir, o Filho das Brasas",
                "tipo": "mini_boss",
                "intro": "A passagem se abre numa câmara onde uma criatura dracônica de ossos escuros repousa sobre rocha derretida. Vharjir, filho de Vharzun, não tem carne, mas brasas percorrem sua coluna como sangue. Ele abre as asas incompletas. — O pai sente cada osso que vocês quebram. Ajoelhe-se, e talvez eu permita que seus restos sirvam à nossa linhagem.",
                "xp": 125,
                "inimigos": [
                    {"nome": "Vharjir, o Filho das Brasas", "tipo": "vharjir", "vida": 245, "dano": [14, 21], "ataque": "Garras de cinza", "especial": "Sopro ósseo", "defesa": 2}
                ],
                "loot": {"nome": "Escama dracônica fossilizada", "texto": "A escama não se desfaz. Presa ao equipamento, ela ajuda a amortecer golpes poderosos.", "efeitos": {"defesa": 2, "vida_maxima": 10}}
            },
            {
                "titulo": "5. Cavaleiros da última vigília",
                "tipo": "combate",
                "intro": "A subida termina num corredor de estátuas. Dois cavaleiros esqueléticos se desprendem dos pedestais, cada um com um brasão apagado no peito. Eles foram os últimos guardiões da prisão e continuam cumprindo o juramento, embora já não se lembrem de quem juraram proteger.",
                "xp": 95,
                "inimigos": [
                    {"nome": "Cavaleiro da última vigília", "tipo": "cavaleiro_osseo", "vida": 76, "dano": [10, 15], "ataque": "Espada de juramento", "defesa": 2},
                    {"nome": "Sentinela do selo", "tipo": "cavaleiro_osseo", "vida": 76, "dano": [10, 15], "ataque": "Lança rachada", "defesa": 2}
                ],
                "loot": {"nome": "Brasão dos guardiões", "texto": "O brasão antigo se encaixa sobre sua proteção e torna seus ataques mais precisos.", "efeitos": {"bonus_dano": 3}}
            },
            {
                "titulo": "6. A guarda evoluída",
                "tipo": "combate",
                "intro": "Na antecâmara final, três guerreiros ósseos carregam armas que queimam sem consumir combustível. Eles se movem em formação, protegendo o portal da prisão. Kaleb aperta a lança. — Certo, esses parecem o tipo de sujeito que não aceita uma conversa amigável. Eu tentei uma vez. Com um barril. Não terminou bem.",
                "xp": 130,
                "inimigos": [
                    {"nome": "Veterano da cinza 1", "tipo": "esqueleto_veterano", "vida": 66, "dano": [9, 14], "ataque": "Machado de osso", "defesa": 1},
                    {"nome": "Veterano da cinza 2", "tipo": "esqueleto_veterano", "vida": 66, "dano": [9, 14], "ataque": "Lança de brasa", "defesa": 1},
                    {"nome": "Veterano da cinza 3", "tipo": "esqueleto_veterano", "vida": 66, "dano": [9, 14], "ataque": "Espada carbonizada", "defesa": 1}
                ],
                "loot": {"nome": "Kit de expedição do sentinela", "texto": "O kit guardado pelos sentinelas contém poções intactas e algumas peças ainda úteis.", "efeitos": {"pocao_cura": 1, "pocao_mana": 1, "ouro": 20}}
            },
            {
                "titulo": "7. Boss: Vharzun, o Devorador de Brasas",
                "tipo": "boss",
                "intro": "O selo se rompe com um som semelhante ao de uma montanha rachando. Vharzun se ergue da câmara de magma, enorme, coberto por escamas negras e veios incandescentes. Seus olhos se fixam em você. — Pequeno guardião de uma era esquecida. Meu filho caiu, meus servos foram quebrados… e você chama isso de vitória? Venha. Eu lhe mostrarei por que até os reis temiam meu nome.",
                "xp": 240,
                "inimigos": [
                    {"nome": "Vharzun, o Devorador de Brasas", "tipo": "vharzun", "vida": 440, "dano": [18, 27], "ataque": "Garra ancestral", "especial": "Sopro de brasas", "defesa": 2}
                ],
                "loot": {"nome": "Coração de brasa selada", "texto": "A chama deixada por Vharzun se torna estável em suas mãos. Ela reforça suas armas sem consumir o usuário.", "efeitos": {"bonus_dano": 5, "vida_maxima": 15, "ouro": 50}}
            }
        ],
        "final": "Vharzun desaba, e o fogo da câmara diminui até restarem apenas brasas. O selo está destruído, mas o dragão não voltará a ameaçar a superfície. Kaleb apoia a lança no ombro. — Então… salvamos o mundo. Você acha que alguém vai pagar o jantar? Espero que sim. Prefiro enfrentar outro dragão a cozinhar."
    }
}
