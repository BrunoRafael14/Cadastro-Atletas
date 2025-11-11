class Atleta:
    def __init__ (self, nome, idade, posição, altura, peso, equipe):
        self.__nome = nome
        self.__idade = idade
        self.__posição = posição
        self.__altura = altura
        self.__peso = peso
        self.__equipe = equipe

        @property
        def nome(self):
            return self.__nome
        @property
        def idade(self):        
            return self.__idade
        @property
        def posição(self):
            return self.__posição
        @property
        def altura(self):
            return self.__altura
        @property
        def peso(self):
            return self.__peso
        @property
        def equipe(self):
            return self.__equipe