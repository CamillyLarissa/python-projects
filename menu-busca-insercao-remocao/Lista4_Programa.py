def menu():
    print('\n----------------MENU --------------------')
    print('1 - Inserir pessoa ')
    print('2 - Listar pessoas cadastradas')
    print('3 - Buscar pessoa por CPF')
    print('4 - Buscar pessoa por Telefone')
    print('5 - Remover pessoa por CPF')
    print('6 - SAIR')
    print('----------------------------------------\n')
    resp = int(input('Digite a sua opção: \n'))
    return resp

def inserir_alunos():
    cpf = input('Digite o CPF: ')
    with open("pessoas.txt", "r") as arquivo:
            for linha in arquivo:
                cpfAluno, nome, endereco, telefones = linha.strip().split(";")
                if cpf == cpfAluno:
                    print('CPF já existente!')
                    return

    nome = input('Digite o nome: ')
    endereco = input('Digite o endereço: ')
    telefones = input("Digite os telefones da pessoa (separados por vírgula): ").split(",")

    pessoa_str = f"{cpf};{nome};{endereco};{','.join(telefones)}\n"

    arquivo = open('pessoas.txt', 'a')
    arquivo.writelines(pessoa_str)
    arquivo.close
    print("Aluno cadastrado com sucesso!")

def listar_alunos():
    try:
        with open("pessoas.txt", "r") as arquivo:
                print("----------------------------------------")
                print("              Lista de Alunos           ")
                print("----------------------------------------")
                for linha in arquivo:
                    cpf, nome, endereco, telefone = linha.strip().split(";")
                    print(f"CPF: {cpf}, Nome: {nome}, Endereço: {endereco}, Telefone: {', '.join(telefone.split(','))}")
                    print("----------------------------------------")
    except FileNotFoundError:
        print("Arquivo não encontrado!")

def buscarPorCpf():
    cpf_busca = input('Digite o cpf do aluno a ser pesquisado: ')
    try:
        with open("pessoas.txt", "r") as arquivo:
                for linha in arquivo:
                    cpf, nome, endereco, telefone = linha.strip().split(";")
                    if cpf == cpf_busca:
                        print(f"CPF: {cpf}, Nome: {nome}, Endereço: {endereco}, Telefone: {', '.join(telefone.split(','))}")
                        return
                print("Pessoa não encontrada!.")
    except FileNotFoundError:
        print("Arquivo não encontrado!.")


def buscarPorTelefone():
    telefone_busca = input("Digite o telefone do aluno a ser pesquisado: ")
    try:
        with open("pessoas.txt", "r") as arquivo:
                for linha in arquivo:
                    cpf, nome, endereco, telefone = linha.strip().split(";")
                    if telefone == telefone_busca:
                        print(f"CPF: {cpf}, Nome: {nome}, Endereço: {endereco}, Telefone: {', '.join(telefone.split(','))}")
                        return
                print("Pessoa não encontrada!.")
    except FileNotFoundError:
        print("Arquivo não encontrado!.")

def removerPorCpf():
    cpf_busca = input('Digite o cpf do aluno a ser pesquisado: ')
    removido = False
    try:
        with open("pessoas.txt", "r") as arquivo:
            linhas = arquivo.readlines()
        with open("pessoas.txt", "w") as arquivo:
                for linha in linhas:
                    if cpf_busca not in linha:
                         arquivo.write(linha)  
                    else:
                         removido = True            
                if removido is False:
                     print('Pessoa não encontrada!.')
                else:
                     print("Pessoa removida com sucesso!.")
                    
    except FileNotFoundError:
        print("Arquivo não encontrado!.")

if __name__ == '__main__':
    while True:
        op = menu()
        match op:
            case 1:
                inserir_alunos()

            case 2:
                listar_alunos()

            case 3:
                buscarPorCpf()

            case 4:
                buscarPorTelefone()

            case 5:
                removerPorCpf()

            case 6:
                print('Saindo...')
                break
            case _:
                print('Opção inválida!')     
