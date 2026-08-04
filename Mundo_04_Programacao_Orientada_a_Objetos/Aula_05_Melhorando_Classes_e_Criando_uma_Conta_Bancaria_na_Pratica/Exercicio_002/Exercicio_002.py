# Declaração de Classe
class Gafanhoto:
    """
    Essa classe cria um gafanhoto que é uma pessoa
    que tem nome e idade.
    Para criar uma nova pessoa, use:
    Variável = Gafanhoto(nome, idade)
    """
    def __init__(self, nome = "Vazio", idade = 0): # Método construtor
        # atributos de Instãncia
        self.nome = nome
        self.idade = idade

        # Métodos de Instância
    def aniversario(self):
        self.idade = self.idade + 1

    def __str__(self): # Dunder method
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."

    def __getstate__(self):
        return f"Estado: nome = {self.nome} ; idade = {self.idade}"


# Declaração de Objetos
g1 = Gafanhoto("Maria", 17)
g1.aniversario()
print(g1)
print(g1.__dict__) # Dunder Attribute
print(g1.__getstate__())
print(g1.__class__)
print(g1.__doc__)


g2 = Gafanhoto("Mauro", 53)
g2.aniversario()
print(g2)
print(g2.__dict__)
print(g2.__getstate__())
print(g2.__class__)
print(g2.__doc__)






