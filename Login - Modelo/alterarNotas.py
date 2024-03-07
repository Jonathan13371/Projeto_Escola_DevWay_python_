

from alunoDAO import AlunoDAO
from aluno import Aluno
import os 









from alunoDAO import AlunoDAO
from aluno import Aluno

import os 







class AlterarNotas():
    def __init__(self):
        self.__usu = Aluno()
        self.__usuDAO =AlunoDAO()
       

        opcao = 'S'
        while opcao != 'N':
                print(50 * '=')
                print('Escola DevWay'.center(50))
                print('Área Do Professor - Alterar Notas'.center(50))
                print(50 * '=')
                print('')
                print('')
                self.__usu.nomeAluno = input('Digite o nome do aluno que deseja alterar: ')
                self.__usuDAO.usu = self.__usu
                
                listaP = self.__usuDAO.pesquisarAluno()
                for(idAluno,nomeAluno,loginAluno,senhaAluno) in listaP:
                    print("==========================================")
                    print("ID do Aluno:    " + str( idAluno))
                    print("Nome do Aluno:   " + str( nomeAluno))
                    print("==========================================")
                else:
                    listaP.fetchone()
                    qtdItens = listaP.rowcount.numerator
                    if qtdItens == 0:
                        print("==========================================")
                        print("      Aluno Não encontrado !!! ")
                        print("==========================================")
                    else:
                        try:
                          self.__usuDAO.use.idAluno = int(input('Digite o ID do Aluno que deseja alterar  '))
                        except ValueError :
                            print('insira um valor numerico para o ID Aluno:')
                            self.__usuDAO.use.idAluno = None

                        if self.__usuDAO.use.idAluno ==None:
                            while self.__usuDAO.use.idAluno ==None:
                                try:
                                    self.__usuDAO.use.idAluno =int(input('Digite o ID do Aluno que deseja alterar  '))
                                except ValueError:
                                    print('insira um valor numerico para o ID Aluno:')
                                    self.__usuDAO.use.idAluno = None   
                        
                        self.__usuDAO.usu = self.__usu
                        
                          

                        listaP = self.__usuDAO.pesquisarAlunoNotasID()
                        for(idNota,disciplina,media,faltas,idAluno) in listaP:
                         print("==========================================")
                         print("ID da Nota:    " + str( idNota))
                         print("ID do Aluno:    " + str( idAluno))


                        try:
                            self.__usuDAO.use.idNota = int(input('Qual o ID da nota que deseja Alterar: '))
                            
                        except ValueError:
                            print('insira um valor numerico para o ID Nota:')
                            self.__usuDAO.use.idNota = None

                        if self.__usuDAO.use.idNota == None:
                            while self.__usuDAO.use.idNota == None:
                             try:
                                self.__usuDAO.use.idNota = int(input('Qual o ID da nota que deseja Alterar: '))
                             except ValueError:
                                print('insira um valor numerico para o ID Nota:')
                                self.__usuDAO.use.idNota = None


                        
                        
                        
                        
                        
                        self.__usuDAO.usu = self.__usu
                        os.system('cls')
                        self.__usuDAO.pesquisarNotasID()
                        print('Atenção: caso nao queria alterar o campo precione <ENTRE> ')
                        

                        novoNome = input('Digite o Novo novo nome da disciplina:')
                        if novoNome =='':
                            self.__usuDAO.use.disciplina = self.__usuDAO.use.disciplina
                        
                        else:
                            self.__usuDAO.use.disciplina = str (novoNome)
                        

                        novaMEDIA = input('Digite o Nova media: ')
                        if novaMEDIA == '':
                            self.__usuDAO.use.media = self.__usuDAO.use.media

                        else:
                            self.__usuDAO.use.media = float(novaMEDIA )  
                            

                        novaqtdFaltas =  input('Digite a quantidade de faltas:')
                        if novaqtdFaltas =='':
                            self.__usuDAO.use.faltas =  self.__usuDAO.use.faltas

                        else:
                            self.__usuDAO.use.faltas = int (novaqtdFaltas)

                            
                        
                    
                    
                    
                    
                        self.__usuDAO.usu = self.__usu
                        self.__usuDAO.AlterarNotas()
                        
                    
                        
                
                        opcao = input("Deseja Alterar outro Aluno [S/N]? ").upper()
                        os.system('cls')
       
        self.__usuDAO.fecharConexao()
             
