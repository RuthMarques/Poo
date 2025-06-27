import classes as c
import os

# algoritimo principal
if __name__ == "__main__":
    usuario = c.Pessoa("","","")

    usuario.nome = input("informe o nome: ").strip().title()
    usuario.email = input("informe o email: ").strip().lower
    usuario.profissao = input("informe a profissão: ").strip()

os.sytem("cls" if os.name == "nt" else "clear")

# exibir os atributos
print(f"Nome: {usuario.nome}")
print(f"Email: {usuario.email}")
print(f"Profissão: {usuario.profissao}")