class Aluno:
    def __init__(self, nome, matricula, cpf):
        self.__nome = nome 
        self.__matricula = matricula
        self.__cpf = cpf
        self.cursos_iscritos = []

    #metodos de acesso
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome


    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula


    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    # metodo de ação
    def inscrever_curso(self, curso):
        if curso not in self.cursos_iscritos:
            self.cursos_iscritos.append(curso)
            curso.adicionar_aluno(self) #associa o aluno ao curso 

    def listar_cursos(self):
        lista = []
        for curso in self.cursos_incritos:
            lista.append(curso.nome_curso)
        return lista
        
    # metodo especial
    def __del__(self):
        print(f"Objeto {self.nome} destruído com sucesso!")

class Curso:
    def __init__(self, nome_curso):
        self.__nome_curso = nome_curso
        self.alunos_incritos = []
        
    # metodo de acesso
    @property
    def nome_curso(self):
        return self.__nome_curso


    @nome_curso.setter
    def nome_curso(self, nome_curso):
        self.__nome_curso = nome_curso

    # metodos de ação
    def adicionar_aluno(self, aluno):
        if aluno not in self.alunos_incritos:
            self.alunos_incritos.append(aluno)
            aluno.inscrever_curso(self)  # associa o curso ao aluno

    def listar_alunos(self):
        lista = []
        for aluno in self.alunos_incritos:
            lista.append(aluno.nome)
        return lista

    # metodo especial
    def __del__(self):
        print(f"Objeto {self.nome_curso} destruído com sucesso!")
