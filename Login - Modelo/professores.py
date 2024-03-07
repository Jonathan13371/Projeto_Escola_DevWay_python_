class Professores():

    __idProf = int 
    __nomeProf = str
    __loginProf = str
    __senhaProf = str 

    @property

    def idProf(self):
        return self.__idProf

    @idProf.setter
    def idProf(self, idProf):
        self.__idProf = idProf    

    @property

    def nomeProf(self):
        return self.__nomeProf

    @nomeProf.setter
    def nomeProf(self, nomeProf):
        self.__nomeProf = nomeProf    

    @property

    def loginProf(self):
        return self.__loginProf

    @loginProf.setter
    def loginProf(self, loginProf):
        self.__loginProf = loginProf   

    @property

    def senhaProf(self):
        return self.__senhaProf

    @senhaProf.setter
    def senhaProf(self, senhaProf):
        self.__senhaProf = senhaProf                 