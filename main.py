class AtividadeFisica:
    def __init__(self, tipo: str, duracao: int, calorias_gastas: float, data: str):
        self.tipo = tipo
        self.duracao = duracao
        self.calorias_gastas = calorias_gastas
        self.data = data

    def info(self):
        return f'Tipo: {self.tipo}, Duração: {self.duracao}min, Calorias: {self.calorias_gastas} {self.data}'


class Alimento:
    def __init__(self, nome: str, calorias: float, porcao: float):
        self.nome = nome
        self.calorias = calorias
        self.porcao = porcao

    def info(self):
        return f'Alimento: {self.nome}, Calorias: {self.calorias}Kcarl, Porção: {self.porcao}'


class UsuarioSaude:
    def __init__(self, nome: str):
        self.nome = nome
        self.atividades = []
        self.alimentacao = []

    def registrar_atividade(self, atividade: AtividadeFisica):
        self.atividades.append(atividade)
        return f'Atividade "{atividade.tipo}" registrada com sucesso'

    def registrar_alimento(self, alimento: Alimento):
        self.alimentacao.append(alimento)
        return f'Alimento "{alimento.nome}" registrada com sucesso'

    def calorias_totais(self):
        calorias_gastas = sum(atividade.calorias_gastas for atividade in self.atividades)
        calorias_consumidas = sum(alimento.calorias for alimento in self.alimentacao)
        return calorias_consumidas - calorias_gastas


class GerenciadorSaude:
    def __init__(self):
        self.usuarios = {}

    def criar_usuario(self, nome):
        if nome in self.usuarios:
            return 'Erro: usuário já cadastrado'
        self.usuarios[nome] = UsuarioSaude(nome)
        return f'Usuário {nome} cadastrado com sucesso'

    def buscar_usuario(self, nome):
        return self.usuarios.get(nome, 'Usuário não encontrado')

    def listar_usuarios(self):
        if not self.usuarios:
            return 'Nenhum usuário cadastrado.'
        return '\n'.join(f'- {nome}' for nome in self.usuarios)


# Criando o gerenciador e um usuário
gerenciador = GerenciadorSaude()
print(gerenciador.criar_usuario("Marciel"))

# Buscando usuário
usuario = gerenciador.buscar_usuario("Marciel")
if isinstance(usuario, UsuarioSaude):
    atividade = AtividadeFisica("Corrida", 30, 300, "2024-11-25")
    print(usuario.registrar_atividade(atividade))

    alimento = Alimento("Maçã", 95, 150)
    print(usuario.registrar_alimento(alimento))

    print(f"Saldo calórico: {usuario.calorias_totais()} kcal")
else:
    print(usuario)
