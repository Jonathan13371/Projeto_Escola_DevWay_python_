import os
from cadastrarNotas import CadastrarNotas
from pesquisarNotas import PesquisarNotas
from alterarNotas import AlterarNotas
from excluirNotas import ExcluirNotas
class GestaoNotas():
    def __init__(self):
            opcao = 0
            while opcao != 5:
                print(50 * '=')
                print('Escola DevWay'.center(50))
                print('Área Do Professor - Notas'.center(50))
                print(50 * '=')
                print('')
                print('')

                print('1 - Cadastrar Notas')
                print('2 - Pesquisar Notas ')
                print('3 - Alterar Notas ')
                print('4 - Excluir Notas')
                print('5 - Voltar')

                opcao = int(input(''))
                os.system('cls')
                if opcao == 1 : 
                    os.system('cls')  
                    telaC= CadastrarNotas()

                if opcao == 2:
                    telaP = PesquisarNotas()
                if opcao == 3:
                    telaA = AlterarNotas()

                if opcao == 4:
                    telaE =ExcluirNotas()