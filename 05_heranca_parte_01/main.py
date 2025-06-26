# biblotecas
import os
import classes

# algoritimo principal
if __name__ == "__main__":
    # intancia de objetos
    usuario = classes.PessoaFísica("","","","","","","")
    empresa = classes.PessoaJurídica("","","","","","",)

    os.system("cls" if os.name == "nt" else "clear")

    # atribuir valores ao objeto do tipo Pessoa Física
    print(f"{'-'*20} DADOS DO USUARIO {'-'*20}\n")

    usuario.nome = input("informe seu nome: ").title().strip()
    usuario.cpf = input("informe seu CPF: ").strip()
    usuario.profissao = input("informe sua profissão: ").strip()
    usuario.genero = input("informe seu genero: ").strip()
    usuario.email = input("informe seu email: ").strip().lower
    usuario.endereço = input("informe seu endereço: ").title().strip()
    usuario.telefone = input("informe seu telefone: ").strip()

    #limpar a tela 
    os.system("cls" if os.name == "nt" else "clear")

    # atribuir valores ao objeto do tipo Pessoa Jurídica
    empresa.razao_social = input("informe a razão social  da empresa: ").title().strip()
    empresa.nome_fantasia = input("informe o nome fantasia: ").title().strip()
    empresa.cnpj = input("informe o CNPJ: ").strip()
    empresa.email = input("informe o email: ").title().lower()
    empresa.endereço = input("informe o endereço da empresa: ").title().strip()
    empresa.telefone = input("informe o telefone da empresa: ").strip()

    #limpar a tela
    os.system("cls" if os.name == "nt" else "clear")

    # exibir os dados do usuario
    print("Dados do usuario:\n")
    usuario.exibir_dados()
    print("-"*60)
    print("Dados da empresa:\n")
    empresa.exibir_dados()
    
