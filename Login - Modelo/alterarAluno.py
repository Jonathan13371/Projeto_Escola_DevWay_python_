

from alunoDAO import AlunoDAO
from aluno import Aluno
import os 







class AlterarAluno():
    def __init__(self):
        self.__usu = Aluno()
        self.__usuDAO =AlunoDAO()

        opcao = 'S'
        while opcao != 'N':
                print(50 * '=')
                print('Escola DevWay'.center(50))
                print('Área Do Professor - Alterar Alunos'.center(50))
                print(50 * '=')
                print('')
                print('')
                self.__usu.nomeAluno = input('Digite o nome do aluno que deseja alterar: ')
                self.__usuDAO.usu = self.__usu
                
                listaP = self.__usuDAO.pesquisarAluno()
                for(idAluno,nomeAluno,loginAluno,senhaAluno) in listaP:
                    print("==========================================")
                    print("ID do Aluno:    " + str( idAluno))
                    print("Nome  do Aluno: " + nomeAluno)
                    print("Login do Aluno: " + loginAluno)
                    print("Senha do Aluno: " + senhaAluno)

                    print("==========================================")
                else:
                    listaP.fetchone()
                    qtdItens = listaP.rowcount.numerator
                if qtdItens == 0:
                        print("==========================================")
                        print("      Aluno Não encontrado !!! ")
                        print("==========================================")
                        opcao= input('Deseja tentar novamente [S/N]: ').upper()
                        os.system('cls')
                
                else:
                       
                    try:
                        self.__usu.idAluno = int(input('Digite o ID do Aluno que deseja alterar  '))
                    except ValueError:
                        print('Erro: insira um valor numerico para o ID aluno')
                        self.__usu.idAluno =None

                       
                    if self.__usu.idAluno ==None:
                        while self.__usu.idAluno ==None:
                            try:
                             self.__usu.idAluno = int(input('Digite o ID do Aluno que deseja alterar  '))
                            except ValueError:
                             print('Erro: insira um valor numerico para o ID aluno')
                             self.__usu.idAluno =None

                    self.__usuDAO.usu = self.__usu
                    os.system('cls')
                        
                    verificar = self.__usuDAO.verificarID(self.__usuDAO.usu.idAluno)  
                    if verificar ==True:
                        self.__usuDAO.pesquisarID()  
                        
                        print('\nATENÇÃO: caso não deseja alterar determinado campo precione ENTER')                
                        novoNome = (input('Digite o novo  nome:'))
                        if novoNome =='':
                            self.__usu.nomeAluno =  self.__usuDAO.usu.nomeAluno 
                            
                        else:
                            self.__usu.nomeAluno = str (novoNome)
                            

                        novoLogin = (input('Digite o novo Login:'))
                        if novoLogin == '':
                            self.__usu.loginAluno=self.__usuDAO.usu.loginAluno 

                        else:
                            self.__usu.loginAluno = str (novoLogin)  
                                

                        novaSenha =  (input('Digite a nova senha:'))
                        if novaSenha =='':
                            self.__usu.senhaAluno =  self.__usuDAO.usu.senhaAluno 

                        else:
                            self.__usu.senhaAluno = str (novaSenha)

                                
                        self.__usuDAO.usu = self.__usu
                                               
                        self.__usuDAO.AlterarAluno()
                        opcao = input("Deseja Alterar outro Aluno [S/N]? ").upper()
                        os.system('cls')
                   
                    else:
                        print('Erro: esse id não pertence a esse aluno')
                        opcao = input("Deseja tentar novamente [S/N]? ").upper()    
       
        self.__usuDAO.fecharConexao()
             
