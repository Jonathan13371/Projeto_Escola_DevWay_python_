import os
from alunoDAO import AlunoDAO
from aluno import Aluno

class PesquisarNotas():
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
                self.__usu.nomeAluno = input('Digite o nome do aluno: ')
                self.__usuDAO.usu = self.__usu

                listaPes = self.__usuDAO.pesquisarAluno()
                for(idAluno,nomeAluno,loginAluno,senhaAluno) in listaPes:
                    print("==========================================")
                    print('ID do Aluno:' + str(idAluno))
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
               
               
                if qtdItens >= 1:
                    try:
                          self.__usu.idAluno = int(input('Digite o ID do Aluno que deseja pesquisar  a nota'))
                    except ValueError :
                            print('insira um valor numerico para o ID Aluno:')
                            self.__usu.idAluno  = None

                    if self.__usu.idAluno  ==None:
                        while self.__usu.idAluno  ==None:
                         try:
                            self.__usu.idAluno =int(input('Digite o ID do Aluno que deseja pesquisar a nota'))
                         except ValueError:
                            print('insira um valor numerico para o ID Aluno:')
                    
                    self.__usuDAO.usu = self.__usu
                    os.system('cls')
                    
                    verificar = self.__usuDAO.verificarID(self.__usuDAO.usu.idAluno) 
                    if verificar ==True:       
                        exibir = self.__usuDAO.alunoPrincipal()
                    
                        print('   Disciplina       Média       Faltas ')
                        for(nomeAluno,disciplina,media,faltas) in exibir:  
                
                            print(f'    {disciplina}           {media}              {faltas}')   
                
                        else:     
                            
                            exibir.fetchone()
                            qtdItens = exibir.rowcount.numerator
                            if qtdItens == 0:       
                                os.system('cls')       
                                print(50*"=")
                                print(f"      O Aluno AINDA NAO POSSUI NOTAS DISPONIVEIS!!! ".center(50))
                                print(50*"=")
                                            
                            
                            
                        opcao = input('Deseja pesquisar outra nota [S/N]: ').upper()  
                        os.system('cls')      
                    else:
                        print('Erro: esse id não coresponte a esse aluno')
                        opcao = input("Deseja tentar novamente [S/N]? ").upper()
                        os.system('cls')
                    
        self.__usuDAO.fecharConexao()