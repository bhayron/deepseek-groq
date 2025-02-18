# Inicialização do inventário (lista de dicionários)
inventario = []

def adicionar_livro():
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    ano = int(input("Digite o ano de publicação: "))
    preco = float(input("Digite o preço do livro: "))
    quantidade = int(input("Digite a quantidade em estoque: "))

    livro = {
        'titulo': titulo,
        'autor': autor,
        'ano': ano,
        'preco': preco,
        'quantidade': quantidade
    }

    inventario.append(livro)
    print("Livro adicionado com sucesso!")

def remover_livro():
    titulo = input("Digite o título do livro para remover: ")
    for livro in inventario:
        if livro['titulo'].lower() == titulo.lower():
            inventario.remove(livro)
            print("Livro removido com sucesso!")
            return
    print("Livro não encontrado no inventário.")

def listar_livros():
    if not inventario:
        print("O inventário está vazio!")
        return
    print("\n--- Inventário da Livraria ---")
    for indice, livro in enumerate(inventario, start=1):
        print(f"\nLivro {indice}:")
        for chave, valor in livro.items():
            print(f"{chave}: {valor}")

def buscar_livro():
    termo = input("Digite o título ou autor do livro para buscar: ")
    resultados = []
    for livro in inventario:
        if termo.lower() in livro['titulo'].lower() or termo.lower() in livro['autor'].lower():
            resultados.append(livro)
    if resultados:
        print("\nResultados da busca:")
        for indice, livro in enumerate(resultados, start=1):
            print(f"\nLivro {indice}:")
            for chave, valor in livro.items():
                print(f"{chave}: {valor}")
    else:
        print("Nenhum livro encontrado com esse critério.")

def main():
    while True:
        print("\n--- Menu da Livraria ---")
        print("1. Adicionar livro")
        print("2. Remover livro")
        print("3. Listar livros")
        print("4. Buscar livro")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_livro()
        elif opcao == "2":
            remover_livro()
        elif opcao == "3":
            listar_livros()
        elif opcao == "4":
            buscar_livro()
        elif opcao == "5":
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()