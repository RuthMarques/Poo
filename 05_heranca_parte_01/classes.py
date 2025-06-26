# classe-pai ou superclasse
class Pessoa:
    # atributos
    def __init__(self, email, endereço, telefone):
        self.email = email
        self.endereço = endereço
        self.telefone = telefone

    # método 
    def exibir_dados(self):
        print(f"Email: {self.email}")
        print(f"Endereço: {self.endereço}")
        print(f"telefone: {self.telefone}")


# classes-filha ou subclasses
class PessoaFísica(Pessoa):
    # atributos
    def __init__(self, nome, cpf, profissao, genero, email, endereço, telefone):
        self.nome = nome
        self.cpf = cpf
        self.profissao = profissao
        self.genero = genero
        super().__init__(email=email, endereço=endereço, telefone=telefone)

    # método polimorfismo
    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Profissao: {self.profissao}")
        print(f"Genero: {self.genero}")
        super().exibir_dados()

class PessoaJurídica(Pessoa):
    def __init__(self, razao_social, nome_fantasia, cnpj, email, endereço, telefone):
        self.razao_social = razao_social
        self.nome_fantasia = nome_fantasia
        self.cnpj = cnpj
        super().__init__(email=email, endereço=endereço, telefone=telefone)

    def exibir_dados(self):
        print(f"Razão Social: {self.razao_social}")
        print(f"Nome Fantasia: {self.nome_fantasia}")
        print(f"CNPJ: {self.cnpj}")
        super().exibir_dados()