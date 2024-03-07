from cadastrarAluno import CadastrarAluno
from pesquisarAluno import PesquisarAluno
from alterarAluno import AlterarAluno
from exluirAluno import ExcluirAluno
import os


class GestaoAluno():

    def __init__(self):
            opcao = 0
            while opcao != 5:
                print(50 * '=')
                print('Escola DevWay'.center(50))
                print('Área Do Professor - Alunos'.center(50))
                print(50 * '=')
                print('')
                print('')

                print('1 - Cadastrar Aluno')
                print('2 - Pesquisar Aluno ')
                print('3 - Alterar Aluno ')
                print('4 - Excluir Aluno')
                print('5 - Voltar')

                opcao = int(input(''))
                os.system('cls')
                if opcao == 1 : 
                    os.system('cls')  
                    telaC= CadastrarAluno()

                if opcao == 2:
                    os.system('cls') 
                    telaP =PesquisarAluno()

                if opcao == 3:
                    os.system('cls') 
                    telaA = AlterarAluno()

                if opcao == 4:
                    os.system('cls') 
                    telaE=ExcluirAluno()