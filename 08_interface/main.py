# importações 
import classes
import os

if  __name__ == "__main__":
    # instacia objeto
    usuario = classes.PessoaFisica("", "", "", "", "", "")
    empresa = classes.PessoaJuridica("", "", "", "", "", "")

while True:
    print("-"*60)
    print("1 - Inserir dados do usuario")
    print("2 - inserir dados da empresa")
    print("3 - exibir dados")
    print("4 - Sair do Programa")
    opcao = input("informe a opção desejada: ").strip()
    os.system("cls" if os.name == "nt" else "clear")
    match opcao:
        case "1":
            try:
                usuario.nome = input("Informe o nome do usuario: ").title().strip()
                usuario.cpf = input("Informe o CPF:").strip()
                usuario.profissao = input("Informe a profissão:").strip()
                usuario.email = input("Informe o email:").strip().lower()
                usuario.endereco = input("Informe o endereço:").strip().title()
                usuario.telefone = input("Informe o telefone:").strip()

                os.system("cls" if os.name == "nt" else "clear")

            except Exception as e:
                print(f"Não foi possivel inserir dados dos usuario. {e}.")
            finally:
                continue
        case "2":
            try:
                empresa.razao_social = input("Informe a razão social da empresa:").strip().title()
                empresa.nome_fantasia = input("Informe o nome da empresa:").strip().title()
                empresa.cnpj = input("Informe o cnpj:").strip()
                empresa.email = input("Informe o email da empresa:").strip().lower()
                empresa.endereco = input("Informe o endereço da empresa:").strip().title()
                empresa.telefone = input("Informe o telefone da empresa:").strip().title()

                os.system("cls" if os.name == "nt" else "clear")

                print(f" Dados da empresa {empresa.nome_fantasia} inseridos com sucesso!")
            except Exception as e:
                print(f"Não foi possivel inserir dados da empresa. {e}.")
            finally:
                 continue
        case "3":
                try:
                    print("\n Dados do usuario \n")
                    usuario.exibir_dados()
                    print("-"*60)
                    print("\n Dados da empresa \n")
                    empresa.exibir_dados()
                except Exception as e:
                    print(f"Não foi possivel exibir os dados")
                finally:
                    continue
        case "4":
            print("Programa encerrado.")
            break
        case _:
            print("opção invalida")