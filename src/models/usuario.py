class Usuario:
    def __init__ (self, nome:str, email:str, senha:str, equipe:str):
        self.__nome = nome
        self.__email = email
        self.__senha = senha
        self.__equipe = equipe

    @property
    def nome(self):
        return self.__nome
    @property
    def email(self):
        return self.__email
    @property
    def senha(self):
        return self.__senha
    @property
    def equipe(self):
        return self.__equipe