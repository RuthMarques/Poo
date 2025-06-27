from classes import Pessoa
import os

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    usuario = Pessoa(nome="", profissao="", idade="")

while True:
    print("1 - iserir dados e exibir")
    print("2 - Sair do Programa")
    opcao = input("Informe a opção desejada: ").strip()
    limpar()
    match opcao:
        case "1":
            try:
                usuario.nome = input("Informe seu nome: ").title().strip()
                usuario.idade = int(input("Informe a idade: "))
                usuario.profissao = input("Informe a profissão: ").strip()

                limpar()
                print(usuario)
                print(f"Idade de {usuario.nome}: {len(usuario)} anos.")
                continue
            except Exception as e:
                print(f"Não foi possivel executar o programa. {e}")
                break
        case "2":
            break
        case _:
            print("opção Invalda.")
            continue