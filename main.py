class Tarefa:
    def __init__(self, nome, prioridade, geral=False):
        self.nome = nome
        self.prioridade = prioridade
        self.geral = geral

class Fila:
    def __init__(self):
        self.itens = []

    def enfileirar(self, item):
        self.itens.append(item)

    def enfileirarPrioridade(self, item):
        self.itens.insert(0, item)

    def ordenar(self):
        self.itens.sort(key=lambda t: -t.prioridade)

    def remover(self):
        if not self.isEmpty():
            return self.itens.pop(0)
        return None

    def isEmpty(self):
        return len(self.itens) == 0

    def mostrar(self):
        for tarefa in self.itens:
            tipo = "URGENTE" if tarefa.prioridade == 10 else ""
            print(f"  [{tarefa.prioridade}] {tarefa.nome} {tipo}")

class Pilha:
    def __init__(self):
        self.itens = []

    def push(self, item):
        self.itens.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.itens.pop()
        return None

    def peek(self):
        if not self.isEmpty():
            return self.itens[-1]
        return None

    def isEmpty(self):
        return len(self.itens) == 0

    def mostrar(self):
        for tarefa in reversed(self.itens):
            print(f"    [{tarefa.prioridade}] {tarefa.nome}")

class Astronauta:
    def __init__(self, nome, funcao):
        self.nome = nome
        self.funcao = funcao
        self.fila = Fila()
        self.historico = Pilha()

    def adicionarTarefa(self, tarefa):
        if tarefa.prioridade == 10:
            self.fila.enfileirarPrioridade(tarefa)
        else:
            self.fila.enfileirar(tarefa)

    def executarTarefas(self):
        print(f"\n{'='*55}")
        print(f"  {self.nome} | {self.funcao}")
        print(f"{'='*55}")

        while not self.fila.isEmpty():
            tarefa = self.fila.remover()
            self.historico.push(tarefa)
            print(f"  EXECUTADA: [{tarefa.prioridade}] {tarefa.nome}")

    def mostrarHistorico(self):
        print(f"\n  Histórico de {self.nome}:")
        self.historico.mostrar()

class MissionScheduler:
    def __init__(self, astronautas, tarefas):
        self.astronautas = astronautas
        self.tarefas = tarefas

    def distribuir(self):
        universais = [t for t in self.tarefas if t.geral]
        missao = sorted(
            [t for t in self.tarefas if not t.geral],
            key=lambda t: -t.prioridade
        )

        print("\n  TAREFAS UNIVERSAIS (todos os astronautas):")
        for t in universais:
            print(f"    [{t.prioridade}] {t.nome}")
            for astronauta in self.astronautas:
                astronauta.adicionarTarefa(Tarefa(t.nome, t.prioridade, True))

        print("\n  DISTRIBUIÇÃO DE TAREFAS DE MISSÃO:")
        for i, tarefa in enumerate(missao):
            astronauta = self.astronautas[i % len(self.astronautas)]
            astronauta.adicionarTarefa(tarefa)
            print(f"    [{tarefa.prioridade}] {tarefa.nome} → {astronauta.nome}")

        for astronauta in self.astronautas:
            astronauta.fila.ordenar()

    def mostrarFilas(self):
        print(f"\n{'='*55}")
        print("  FILAS ORGANIZADAS POR ASTRONAUTA")
        print(f"{'='*55}")
        for astronauta in self.astronautas:
            print(f"\n  {astronauta.nome}:")
            astronauta.fila.mostrar()

    def executar(self):
        for astronauta in self.astronautas:
            astronauta.executarTarefas()

    def mostrarResumo(self):
        print(f"\n{'='*55}")
        print("  HISTÓRICO GERAL DA MISSÃO")
        print(f"{'='*55}")
        for astronauta in self.astronautas:
            astronauta.mostrarHistorico()

tarefas = [
    Tarefa("Monitorar níveis de oxigênio e CO₂",               10, False),
    Tarefa("Verificar sistema de reciclagem de água",          10, False),
    Tarefa("Checagem dos sistemas de suporte à vida",           9, False),
    Tarefa("Monitorar níveis de radiação",                      9, False),
    Tarefa("Fazer exercício físico diário",                     9, True),
    Tarefa("Exame médico diário",                               8, True),
    Tarefa("Manutenção nos painéis solares",                    8, False),
    Tarefa("Testar sistemas de backup",                         8, False),
    Tarefa("Dormir o ciclo completo de sono",                   8, True),
    Tarefa("Controle térmico da nave",                          7, False),
    Tarefa("Manutenção preventiva nos motores",                 7, False),
    Tarefa("Verificar integridade estrutural da nave",          7, False),
    Tarefa("Atualizar software de navegação",                   7, False),
    Tarefa("Preparar e consumir refeições",                     7, True),
    Tarefa("Gerenciar resíduos da nave",                        7, True),
    Tarefa("Reunião diária de equipe",                          7, True),
    Tarefa("Comunicação com a Terra",                           7, False),
    Tarefa("Coletar dados científicos",                         6, False),
    Tarefa("Enviar relatórios para a Terra",                    6, False),
    Tarefa("Higiene pessoal",                                   6, True),
    Tarefa("Monitorar ingestão calórica",                       6, True),
    Tarefa("Cuidar da horta hidropônica",                       6, False),
    Tarefa("Sessão de bem-estar psicológico",                   6, True),
    Tarefa("Meditação e relaxamento",                           5, True),
    Tarefa("Manutenção de equipamentos EVA",                    5, False),
    Tarefa("Observações astronômicas",                          5, False),
    Tarefa("Tempo de lazer controlado",                         4, True),
    Tarefa("Inventário de suprimentos",                         4, False),
    Tarefa("Atualizar diário de bordo",                         3, True),
    Tarefa("Planejar atividades em Marte",                      2, False),
]

astronautas = [
    Astronauta("John Michael Osbourne", "Comandante da Missão"),
    Astronauta("Robert Plant", "Especialista em Comunicações"),
    Astronauta("Jimmy Page", "Cientista Chefe"),
    Astronauta("David Gilmour", "Engenheiro de Sistemas"),
]

scheduler = MissionScheduler(astronautas, tarefas)
scheduler.distribuir()
scheduler.mostrarFilas()
scheduler.executar()

