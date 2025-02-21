from FILa_Prioridade import (Fila, FilaPrioridade)

class AppFila:
    def __init__(self):
        self.f = Fila()
        self.fp = FilaPrioridade()

if __name__ == '__main__':
    app = AppFila()
    while True:
        print('\n===================MENU======================\n')
        print('1 - Chegada de pessoa para atendimento normal')
        print('2 - Chegada de pessoa para atendimento prioritário')
        print('3 - Atendimento de uma pessoa')
        print('4 - Listar todas as pessoas da(s) fila(s)')
        print('5 - Gerar estatísticas sobre os atendimentos realizados: ')
        print('6 - SAIR \n=============================================================')
        resp = int(input("\nDigite a opção desejada: "))
        match resp:

            case 1:
                nome = input("\nDigite o seu nome: ")
                idade = int(input("Digite o seu idade: "))
                if idade < 60:
                    app.f.enqueue(nome,idade, 6)
                else:
                    print('\nPessoa realocada para a fila prioritária!')
                    app.fp.enqueuePP(nome,idade, 0)
            case 2:
                
                nome = input("\nDigite o seu nome: ")
                idade = int(input("Digite o seu idade: "))
                app.fp.listarprioridades()
                prio = int(input("Digite o numero da prioridade: "))
                if (idade > 60) or (prio > 0):
                    app.fp.enqueuePP(nome, idade, prio)
                else:
                    app.f.enqueue(nome,idade, 6)
                    print('\nPessoa realocada para a fila normal!')
            case 3:
                if app.fp.quant != 0:
                    print(f'\nAtender: {app.fp.dequeuePP()}')
                else:
                    if app.f.quant != 0:
                        print(f'\nAtender: {app.f.dequeue()}')
                    else:
                        print("A fila está vazia!")
                    
            case 4:
                print(f'\nPessoas Normais: {app.f}\n')
                print(f'Pessoas com Prioridade: {app.fp}\n')
            case 5:
                print('\nTamanho das Filas:')
                print(f'\nQuantidade de pessoas na fila normal: {app.f.size()}')
                print(f'Quantidade de pessoas na fila prioritária: {app.fp.sizePP()}')
                total = app.f.cont + app.fp.cont

                print('\nPorcentagem de atendimento: ')
                if app.fp.cont == 0:
                    print('Não houve nenhum atendimento da fila com prioridade até o momento. ')
                else:
                    print(f"\n%Atendimento Prioritario: {round((app.fp.cont / total) * 100,2)} %")
                if app.f.cont == 0:
                    print('Não houve nenhum atendimento da fila normal até o momento. ')
                else:
                    print(f"%Atendimento Normal: {round((app.f.cont / total) * 100, 2)} %\n")
                    
            case 6:
                if (app.f.isEmpty() and app.fp.isEmptyPP()) is False:
                    print('\nAinda há pessoas para serem atendidas!')
                    continue
                else:
                    break
            case others:
                print("\nOpção inválida!")

    print('\nTamanho das Filas\n')
    print(f'Quantidade de pessoas na fila normal: {app.f.cont}')
    print(f'Quantidade de pessoas na fila prioritária: {app.fp.cont}')

    total = app.f.cont + app.fp.cont
    print('\nPorcentagem de pessoas das listas:')
    if app.fp.cont == 0:
        print('Não houve nenhum atendimento da fila com prioridade. ')
    else:
        print(f"\n%Atendimento Prioritario: {round((app.fp.cont / total) * 100,2)} %")
    if app.f.cont == 0:
        print('Não houve nenhum atendimento da fila normal. ')
    else:
        print(f"%Atendimento Normal: {round((app.f.cont / total) * 100, 2)} %\n")