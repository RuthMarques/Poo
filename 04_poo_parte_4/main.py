#biblioteca
import random

#classe 
class Pessoa:
    # contrutor
    def __init__(self, nome, email, profissão, humor):
        self.nome = nome
        self.email = email
        self.profissão = profissão
        self.humor = humor

    # métodos
    def dar_boas_vindas(self):
        return "Boa tarde!"
    
    def cumprimentar(self):
        return f"Olá, eu me chamo {self.nome}. É um Prazer!"
    
    def perguntar(self):
        return f"Qual o seu nome?"
    def cartao_de_visitas(self):
        print(f"Nome: {self.nome}")
        print(f"Email: {self.email}")
        print(f"Profissão: {self.profissão}")

    def ofender(self):
        return f"Quem liga? Me erra! Vai ver se eu tÔ na esquina!"
        
#algoritimo principal
if __name__ == "__main__":
    # instancia de dois objetos
    usuario_masculino = Pessoa("","","", bool(random.getrandbits(1)))
    usuaria_feminina = Pessoa("","","", bool(random.getrandbits(1)))

    # seta os valores dos atributos do objeto masculino
    usuario_masculino.nome = input("Informe seu nome: ").title().strip()
    usuario_masculino.email = input("Informe seu email: ").lower().strip()
    usuario_masculino.profissão = input("Informe sua profissão: ").strip()

    # seta os valores dos atributos do objeto feminino
    usuaria_feminina.nome = input("Informe seu nome: ").title().strip()
    usuaria_feminina.email = input("Informe seu email: ").lower().strip()
    usuaria_feminina.profissão = input("Informe sua profissão: ").strip()

    # conversa
    print(f"Homem: -{usuario_masculino.dar_boas_vindas()}")
    print(f"Mulher: -{usuaria_feminina.dar_boas_vindas()}")
    print(f"Homem: -{usuario_masculino.perguntar()}")
    if usuaria_feminina.humor is True:
        print(f"Mulher: -{usuaria_feminina.cumprimentar()}")
        print(f"Mulher: -{usuaria_feminina.perguntar()}")
        usuario_masculino.humor = usuaria_feminina.humor
        print(f"Mulher: -{usuario_masculino.cumprimentar()}")
        print(f"Homem: Bom Humor = {usuario_masculino.humor}")
        print(usuario_masculino.cartao_de_visitas())

    else:
        print(f"Mulher: -{usuaria_feminina.ofender()}")
        usuario_masculino.humor = usuaria_feminina.humor
        print(f"Homem: Bom Humor = {usuario_masculino.humor}")