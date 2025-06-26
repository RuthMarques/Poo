# classe
class Pessoa:
    # atributos
    nome = "Ruth"
    idade = 18
    email = "ruthmarquessantos19@gmail.com"
    profissão = "progamador"

    # algoritimo principal
if __name__ == "__main__":
    # istanciar a classe Pessoa ( cria objeto da classe)
    usuario = Pessoa()

    # exibir na tela os dados do usuario
    print(f"Nome: {usuario.nome}.")
    print(f"Idade: {usuario.idade}.")
    print(f"Email: {usuario.email}.")
    print(f"Profissão: {usuario.profissão}.")