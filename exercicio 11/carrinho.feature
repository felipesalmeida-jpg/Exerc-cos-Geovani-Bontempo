# language: pt
Funcionalidade: Carrinho de compras
  Como um cliente da loja
  Eu quero adicionar produtos ao carrinho
  Para ver o valor total da minha compra atualizado

  Cenário: Adicionar produto com estoque suficiente
    Dado que o carrinho está vazio
    Quando o cliente adiciona 2 unidades de um produto com estoque de 10 e preço de 50 reais
    Então o total do carrinho deve ser 100 reais
    E o carrinho deve ter 2 itens

  Cenário: Adicionar produto sem estoque suficiente
    Dado que o carrinho está vazio
    Quando o cliente adiciona 5 unidades de um produto com estoque de 3 e preço de 50 reais
    Então o sistema deve exibir o erro "Estoque insuficiente"
    E o total do carrinho deve ser 0 reais
    E o carrinho deve ter 0 itens
