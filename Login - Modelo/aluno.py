class Aluno():
    __idAluno = int 
    __nomeAluno = str
    __loginAluno = str
    __senhaAluno = str 


    @property

    def idAluno(self):
        return self.__idAluno

    @idAluno.setter
    def idAluno(self, idAluno):
        self.__idAluno = idAluno    


    @property

    def nomeAluno(self):
        return self.__nomeAluno

    @nomeAluno.setter
    def nomeAluno(self, nomeAluno):
        self.__nomeAluno = nomeAluno   

    @property

    def loginAluno(self):
        return self.__loginAluno

    @loginAluno.setter
    def loginAluno(self, loginAluno):
        self.__loginAluno = loginAluno      

    @property

    def senhaAluno(self):
        return self.__senhaAluno

    @senhaAluno.setter
    def senhaAluno(self, senhaAluno):
        self.__senhaAluno = senhaAluno        
      
         
