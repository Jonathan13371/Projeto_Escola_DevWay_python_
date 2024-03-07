
from aluno import Aluno
from alunoDAO import AlunoDAO
import os


class CadastrarAluno():

    def __init__(self):
        self.__usu = Aluno()
        self.__usuDAO = AlunoDAO()

        opcao = 'S'
        while opcao != 'N':
                print(50 * '=')
                print('Escola DevWay'.center(50))
                print('Área Do Professor - Cadastramento Alunos'.center(50))
                print(50 * '=')
                print('')
                print('')
                
                
                
                self.__usu.nomeAluno = ''
                 
                while not self.__usu.nomeAluno.isalpha():
                        self.__usu.nomeAluno = input('Digite o nome do aluno: ') 
                        if not self.__usu.nomeAluno.isalpha():
                            print('Voce está tentando digitar numeros para o nome do aluno ou voce não estar digitando nada!')
                            print('Por favor Digite apenas letras!')          
                
                
                self.__usu.loginAluno= input('Digite o login do aluno: ')
                if self.__usu.loginAluno =='':
                    while self.__usu.loginAluno =='':
                        print('Voce precisa cadastrar um login!')
                        self.__usu.loginAluno= input('Digite o login do aluno: ')
                
            
                
                print('ATENÇÃO: A senha so pode ter no maximo 30 caracteres')
                self.__usu.senhaAluno = input('Digite a senha do aluno: ')
                if self.__usu.senhaAluno =='':
                    print('ATENÇÃO: A senha so pode ter no maximo 30 caracteres')
                    while self.__usu.senhaAluno =='':
                        print('Voce precisa cadastrar uma senha:')
                        self.__usu.senhaAluno = input('Digite a senha do aluno: ')

                if len(self.__usu.senhaAluno)>30:
                    while len(self.__usu.senhaAluno)>30:
                     print('Voce excedeu o limite de caractere tente novamente')        
                     self.__usu.senhaAluno = input('Digite a senha do aluno: ')

                self.__usuDAO.usu = self.__usu   

                self.__usuDAO.cadastrarAluno()
                os.system('cls')
                print(50 * '=')
                print('Aluno Cadastrado com Sucesso!'.center(50))
                print(50 * '=')
                
                
                opcao = input('Deseja continuar cadastrando [S/N]:').upper()
                os.system('cls')
        self.__usuDAO.fecharConexao()


            