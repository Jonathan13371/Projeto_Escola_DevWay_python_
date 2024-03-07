

from alunoDAO import AlunoDAO
from aluno import Aluno
import os 




class ExcluirNotas():

    def __init__(self):
        
        self.__usu = Aluno()
        self.__usuDAO = AlunoDAO()
        

        opcao = 'S'
        while opcao != 'N':
                print(50 * '=')
                print('Escola DevWay'.center(50))
                print('Área Do Professor - Excluir Notas'.center(50))
                print(50 * '=')
                print('')
                
                
                
                self.__usu.nomeAluno = input('Digite o nome do aluno que deseja excluir a nota: ')
                self.__usuDAO.usu = self.__usu

                listaPes = self.__usuDAO.pesquisarAluno()
                for(idAluno,nomeAluno,loginAluno,senhaAluno) in listaPes:
                    print("==========================================")
                    print('ID do Aluno: ' + str(idAluno))
                    print("Nome  do Aluno: " + nomeAluno)
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

                else:

                    try:
                        self.__usuDAO.use.idAluno = int(input('Digite o ID do Aluno que deseja excluir a nota  '))
                    except ValueError :
                         print('insira um valor numerico para o ID Aluno:')
                         self.__usuDAO.use.idAluno = None

                    if self.__usuDAO.use.idAluno ==None:
                        while self.__usuDAO.use.idAluno ==None:
                         try:
                            self.__usuDAO.use.idAluno =int(input('Digite o ID do Aluno que deseja excluir a nota  '))
                         except ValueError:
                            print('insira um valor numerico para o ID Aluno:')

                    self.__usuDAO.usu = self.__usu
                    
                    verificarAluno = self.__usuDAO.verificarIDAluno(self.__usuDAO.use.idAluno)
                    if verificarAluno ==False:
                        print('Esse ID não pertence a esse Aluno ou o Aluno Ainda não tem notas para ser excluida !')
                        opcao = input("Deseja Tentar Novamente [S/N]? ").upper()
                        os.system('cls') 
                    
                    if verificarAluno ==True:
                        listaP = self.__usuDAO.pesquisarAlunoNotasID()
                        for(idNota,disciplina,media,faltas,idAluno) in listaP:
                            print("==========================================")
                            print("ID da Nota:    " + str( idNota))
                            print("ID do Aluno:    " + str( idAluno))
                                    
                        else:
                            listaP.fetchone()
                            qtdIten = listaP.rowcount.numerator
                                    
                        if qtdIten == 0:
                                os.system('cls')
                                print("==========================================")
                                print("      Aluno Não possui notas !!! ")
                                print("==========================================")
                                opcao = input("Deseja Tentar Novamente [S/N]? ").upper()
                        else:
                            try:
                                self.__usuDAO.use.idNota = int(input('Qual o ID da nota que deseja Excluir: '))
                            except ValueError:
                                print('Erro: você precisa digitar um valor numerico para o ID Nota') 
                                self.__usuDAO.use.idNota =None   
                                        
                            if self.__usuDAO.use.idNota ==None :
                                while self.__usuDAO.use.idNota ==None:
                                 try:
                                    self.__usuDAO.use.idNota = int(input('Qual o ID da nota que deseja Excluir: '))
                                 except ValueError:
                                    print('Erro: você precisa digitar um valor numerico para o ID Nota') 
                                    self.__usuDAO.use.idNota =None 
                                
                        self.__usuDAO.usu = self.__usu
                        verificar =self.__usuDAO.verificar(self.__usuDAO.use.idNota) 
                        if verificar == True:    
                            self.__usuDAO.excluirNota() 
                            print("==========================================")
                            print("      Nota Excluida Com Sucesso !!! ")
                            print("==========================================") 
                            opcao = input("Deseja excluir outra Nota [S/N]? ").upper()
                            os.system('cls')
                        else:   
                            print('O ID da Nota Não Pertence ao ID Do Aluno Informado:')
                            opcao = input("Deseja Tentar Novamente [S/N]? ").upper() 
                        os.system('cls')       
                       
                
        self.__usuDAO.fecharConexao()