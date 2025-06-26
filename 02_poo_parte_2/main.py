# classe 
class Pessoa:
    # atributos
    nome = "Ruth Marques"
    idade = 18
    email = "ruthmarquessantos19@gmail.com"
    profissão = "progamador"

    # métodos
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}, tenho {self.idade} anos, trabalho como {self.profissão} e meu email é {self.email}.")

# algoritimo principal
if __name__ == "__main__":
    # instanciar a classe
    usuario = Pessoa()

    # executar o método
    usuario.apresentar()