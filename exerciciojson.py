import os
import json as manipjason


opc = ""
filename = R"D:\dev\python\nome.txt"
sair = 0

if os.path.exists(filename):
    with open(filename, 'r', encoding='utf-8') as manipfiler:
        conteudo = manipfiler.read()
        if conteudo:
            dicPessoa = manipjason.loads(conteudo)

while sair == 0:
    print("\n1 - Inserir uma ou mais pessoas")
    print("2 - Listar as pessoas")
    print("3 - Apagar uma ou mais pessoas")
    print("4 - Sair e gravar o ficheiro")
    print("5 - Sair sem gravar")
    opc = input("\nIntroduza a opção: ")

    match opc:
        case "1":
            while True:
                nome = input("\nInsira o nome: ")
                idade = int(input("Insira a idade: "))
                morada = input("Insira a morada: ")
                
                dicPessoa[nome] = {"idade": idade, "morada": morada}
                
                continuar = input("Deseja inserir outra pessoa? (s/n): ")
                
                while continuar != "s" and continuar != "S" and continuar != "n" and continuar != "N":
                    print("Opção inválida! Escreva apenas s ou n.")
                    continuar = input("Deseja inserir outra pessoa? (s/n): ")

        case "2":
            if not dicPessoa:
                print("Não existem pessoas registadas.")
            else:
                print("\n--- Lista de Pessoas ---")
                for nome, dados in dicPessoa.items():
                    print(f"Nome: {nome} | Idade: {dados['idade']} | Morada: {dados['morada']}")

        case "3":
            while True:
                if not dicPessoa:
                    print("O dicionário está vazio.")
                    break
                
                nome_apagar = input("Insira o nome da pessoa a apagar: ")
                if nome_apagar in dicPessoa:
                    del dicPessoa[nome_apagar]
                    print(f"'{nome_apagar}' foi removido com sucesso.")
                else:
                    print("Pessoa não encontrada.")
                
                continuar = input("Deseja apagar outra pessoa? (s/n): ").lower()
                if continuar != 's':
                    break

        case "4":
            with open(filename, 'w', encoding='utf-8') as manipfilew:
                manipjason.dump(dicPessoa, manipfilew, indent=4, ensure_ascii=False)
            print("Dados gravados com sucesso!")
            sair = 1

        case "5":
            sair = 1

        case _:
            print("Opção inválida.")