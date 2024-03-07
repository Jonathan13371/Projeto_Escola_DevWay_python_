from alunoDAO import AlunoDAO
from aluno import Aluno
import os 




class PesquisarAluno():

    def __init__(self):
        
        self.__usu = Aluno()
        self.__usuDAO = AlunoDAO()
        

        opcao = 'S'
        while opcao != 'N':
                print(50 * '=')
                print('Escola DevWay'.center(50))
                print('Área Do Professor - Pesquisar Alunos'.center(50))
                print(50 * '=')
                print('')
                self.__usu.nomeAluno = input('Digite o nome do aluno que deseja pesquisar: ')
                self.__usuDAO.usu = self.__usu
        
                listaPes = self.__usuDAO.pesquisarAluno()
                for(idAluno,nomeAluno,loginAluno,senhaAluno) in listaPes:
                    print("==========================================")
                    print('ID do Aluno:    '  + str(idAluno))
                    print("Nome  do Aluno: " + nomeAluno)
                    print("Login do Aluno: " + loginAluno)
                    print("Senha do Aluno: " + senhaAluno)

                    print("==========================================")
                else:
                     listaPes.fetchone()
                     qtdItens = listaPes.rowcount.numerator
                if qtdItens == 0:
                    os.system('cls')
                    print("==========================================")
                    print("      Aluno Não encontrado !!! ")
                    print("==========================================")
                    
               
                opcao = input("Deseja pesquisar outro Aluno [S/N]? ").upper()
                os.system('cls')

        
        self.__usuDAO.fecharConexao()