class Equipe:
    def __init__ (self, nome: str):
        self.__nome = nome
        usuarios = []
        atletas = []

    @property
    def nome(self):
        return self.__nome

    def adicionar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def adicionar_atleta(self, atleta):
        self.atleta.append(atleta)