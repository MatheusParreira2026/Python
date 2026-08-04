class BiscoitoCoracao:
    def __init__(self):
        self.tamanho = 0
        self.massa = ""
        self.peso = 0
        self.cobertura = ""
        self.cozido = bool
        self.temperatura = 0

        def cozinhar():
            self.massa = "chocolate"
            self.cobertura = "morango"
            self.cozido = True
            self.temperatura = 180

        def congelar():
            self.temperatura = -50

        # def mensagem()
        # def cobrir():
        # def confeitar():
        # def podeComer():
        # def comer():
