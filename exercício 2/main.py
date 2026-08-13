# main.py

# --- Exercício 1 ---
def pode_dirigir(idade):
    return idade >= 18

# --- Exercício 2 ---
def calcular_desconto(valor, percentual):
    if percentual > 50:
        percentual = 50
    desconto = valor * (percentual / 100)
    return valor - desconto

# --- Exercício 3 ---
def cadastrar_senha(senha):
    if len(senha) < 8:
        raise ValueError("Senha muito curta")
    return "Senha cadastrada com sucesso!"

# --- Exercício 4 ---
class CarrinhoDeCompras:
    def __init__(self):
        self.itens = []
        
    def adicionar_item(self, item):
        self.itens.append(item)
        
    def remover_item(self, item):
        if item not in self.itens:
            raise ValueError("Item não encontrado")
        self.itens.remove(item)
        
    def listar_itens(self):
        return self.itens