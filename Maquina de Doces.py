# Definindo os produtos e seus preços
produtos = {
    '1': {'nome': 'Chocolate', 'preco': 2.50},
    '2': {'nome': 'Bala', 'preco': 1.00},
    '3': {'nome': 'Chiclete', 'preco': 0.75},
    '4': {'nome': 'Pipoca', 'preco': 3.00}
}

# Função para exibir as opções de produtos
def exibir_opcoes():
    print("Escolha um produto:")
    for chave, produto in produtos.items():
        print(f"{chave}: {produto['nome']} - R${produto['preco']}")

# Função para processar a escolha do usuário
def processar_escolha(escolha, valor_disponivel, carrinho):
    if escolha in produtos:
        produto_escolhido = produtos[escolha]
        preco_produto = produto_escolhido['preco']

        if valor_disponivel >= preco_produto:
            troco = valor_disponivel - preco_produto
            print(f"Você comprou {produto_escolhido['nome']}! Troco: R${troco:.2f}")
            carrinho.append(produto_escolhido['nome'])
            return preco_produto
        else:
            print("Valor insuficiente. Inserir mais dinheiro.")
            return 0
    else:
        print("Opção inválida. Tente novamente.")
        return 0

# Função principal
def main():
    valor_inserido = float(input("Insira o valor na máquina: "))
    total = valor_inserido
    carrinho = []

    while True:
        exibir_opcoes()

        escolha_usuario = input("Digite o número do produto desejado (ou 's' para sair): ")

        if escolha_usuario.lower() == 's':
            break

        valor_produto = processar_escolha(escolha_usuario, total, carrinho)

        if valor_produto > 0:
            total -= valor_produto

        print(f"Valor disponível: R${total:.2f}")

    print("Obrigado por usar a máquina de doces!")

    if carrinho:
        print("Produtos comprados:")
        for produto in carrinho:
            print(produto)
    else:
        print("Nenhum produto foi comprado.")

# Executar o programa
if __name__ == "__main__":
    main()
