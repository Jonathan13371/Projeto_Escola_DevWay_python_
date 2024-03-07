
from alunoDAO import AlunoDAO
from aluno import Aluno
import os 
class ExcluirAluno():
    

    def __init__(self):
        
        self.__usu = Aluno()
        self.__usuDAO = AlunoDAO()
        

        opcao = 'S'
        while opcao != 'N':
                print(50 * '=')
                print('Escola DevWay'.center(50))
                print('Área Do Professor - Excluir Alunos'.center(50))
                print(50 * '=')
                print('')
                
                
                
                self.__usu.nomeAluno = input('Digite o nome do aluno que deseja excluir: ')
                self.__usuDAO.usu = self.__usu

                listaPes = self.__usuDAO.pesquisarAluno()
                for(idAluno,nomeAluno,loginAluno,senhaAluno) in listaPes:
                    print("==========================================")
                    print('ID do Aluno: ' + str(idAluno))
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
                    opcao = input("Deseja Tentar Novamente [S/N]? ").upper()

                if qtdItens >= 1:
                    try:
                          self.__usu.idAluno = int(input('Digite o ID do Aluno que deseja excluir  '))
                    except ValueError :
                            print('insira um valor numerico para o ID Aluno:')
                            self.__usu.idAluno  = None

                    if self.__usu.idAluno  ==None:
                        while self.__usu.idAluno  ==None:
                         try:
                            self.__usu.idAluno =int(input('Digite o ID do Aluno que deseja excluir  '))
                         except ValueError:
                            print('insira um valor numerico para o ID Aluno:')
                    
                    
                    self.__usuDAO.usu = self.__usu
                    os.system('cls')
                    verfificar =self.__usuDAO.verificarID(self.__usu.idAluno) 
                    if verfificar == True:   

                        self.__usuDAO.excluirAlunoID()

                        print("==========================================")
                        print("      Aluno Excluido Com Sucesso !!! ")
                        print("==========================================")
                        
                        
                        opcao = input("Deseja excluir outro Aluno [S/N]? ").upper()
                        os.system('cls')
                    else:
                        print('Esse ID não pertence a esse aluno: ')    
                        opcao = input("Deseja Tentar Novamente [S/N]? ").upper()
                        os.system('cls')
                        

        
        self.__usuDAO.fecharConexao()