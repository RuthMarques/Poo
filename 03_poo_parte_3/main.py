# classe
class Pessoa:
    # método contrutor
    def __init__(self, nome, idade, email, profissão):
        # atributos
        self.nome = nome
        self.idade = idade
        self.email = email
        self.profissão = profissão

    # método de ação
    def apresentar(self):
        print(f"Olá, eu me chamo {self.nome}, tenho {self.idade} anos, trabalho como {self.profissão} e meu email é {self.email}. ")

# algoritimo principal
if __name__ == "__main__":
    # instanciar a classe
    usuario = Pessoa("", 0, "", "")


    # tratamento de exceção
    try:
        # seta valores aos atributos do objeto
        usuario.nome = input("Informe o nome do usuario: ").title().strip()
        usuario.idade = int(input("Informe a idade: "))
        usuario.email = input("Informe o email: ").lower().strip()
        usuario.profissão = input("Informe sua profissão: ").strip()

        # executa o método 
        usuario.apresentar()
    except Exception as e:
        print(f"Não foi possivel executar o programa. {e}.")