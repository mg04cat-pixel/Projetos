#Lista Base
livros = []

while True:
    print("Bem vindo a Biblioteca dos Sonhos! O que você deseja?\n1. Cadastrar Livro\n2. Consultar Livro\n3. Empréstimo\n4. Conferir Acervo\n5. Sair")
    escolha = input("Digite uma opção: ")

    #Cadastrar
    if escolha == '1':
        print("Você está cadastrando um livro na Biblioteca dos Sonhos!")
        titulo = input("Digite o título do livro: ").lower()
        autor = input("Digite o autor do livro: ").lower()
        livros.append(titulo+' - '+autor) #Adicionando a lista 'livros'
        print("Voltando ao menu!")
    #Consulta
    elif escolha == '2':
        print("Você está consultando um livro na Biblioteca dos Sonhos!")
        busca = input("Digite um título ou autor: ").lower()
        encontrados = [livro for livro in livros if busca in livro]
        for livro in livros:
            if busca in livro:
                print("Livro encontrado:", livro)
                break
        else:
            print("Lamentamos, livro não encontrado!")
        print("Voltando ao menu!")
    #Empréstimo
    elif escolha == '3':
        print("Você está solicitando um empréstimo na Biblioteca dos Sonhos!")
        emprestimo = input("Digite o título do livro para empréstímo: ").lower()
        for i in range(len(livros)):
            if emprestimo in livros[i].lower():
                if "[Emprestado]" in livros[i]:
                    print("Desculpe, este livro já foi emprestado!")
                else:
                    livros[i] = livros[i] + "[Emprestado]"
                    print("Livro emprestado com sucesso!")
                break
        else:
            print("Livro não encontrado!")
        print("Voltando ao menu!")
    #Conferir Acervo
    elif escolha == '4':
        print("Você está conferindo o acervo da Biblioteca dos Sonhos!")
        if len(livros) == 0:
            print("Nenhum livro foi cadastrado!")
        else:
            for livro in livros:
                print(livro)
    #Sair
    elif escolha == '5':
        print("Fechando a Biblioteca dos Sonhos. Até mais!")
        break
    else:
        print("Opção inválida!")
        print("Voltando ao menu!")
