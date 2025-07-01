from classes import PessoaFísica, PessoaJuridica
import os 

def limpar():
    os.system("cls" if os.name == "nt" else "claer")

if __name__ == "__main__":
    usuario = PessoaFísica(
        nome="",
        cpf="",
        profissao="",
        email="",
        telefone="",
        endereço=""
        )
    
    empresa = PessoaJuridica(
        razao_social="",
        nome_fantasia="",
        cnpj="",
        email="",
        telefone="",
        endereço=""
        )
    
    
    print("Informe os dados do usuario:\n")

    usuario.nome = input("Informe o nome do usuario: ").strip().title()
    usuario.cpf = input("Informe o CPF do usuario:").strip()
    usuario.profissao = input("Informe a profissão do usuario: ").strip()
    usuario.email = input("Informe o email do usuario: ").strip().lower()
    usuario.telefone = input("Informe o telefone do usuario: ").strip()
    usuario.endereço = input("Informe o endereço do usuario: ").strip().title()

    print(f"{'-'*40}")
    print("Informe os dados da empresa:\n")

    empresa.razao_social = input("Informe a razão social: ").strip().title()
    empresa.nome_fantasia = input("Informe o nome da empresa:").strip()
    empresa.cnpj = input("Informe o CNPJ da empresa: ").strip()
    empresa.email = input("Informe o email do empresa: ").strip().lower()
    empresa.telefone = input("Informe o telefone do empresa: ").strip()
    empresa.endereço = input("Informe o endereço da empresa: ").strip().title()

    # limpar a tela
    limpar()

    # saida de dados 
    print(usuario)
    print(empresa)

    # exibir os dados
    print(f"{'-'*20} Dados do usuario {'-'*20}")
    print(f"Nome: {usuario.nome}")
    print(f"CPF: {usuario.cpf}")
    print(f"Profissão: {usuario.profissao}")
    print(f"Email: {usuario.email}")
    print(f"Telefone: {usuario.telefone}")
    print(f"Endereço: {usuario.endereço}")

    print(f"{'-'*20} Dados da empresa {'-'*20}")
    print(f"Razão Social: {empresa.razao_social}")
    print(f"Nome Fantasia: {empresa.nome_fantasia}")
    print(f"CNPJ: {empresa.cnpj}")
    print(f"Email: {empresa.email}")
    print(f"Telefone: {empresa.telefone}")
    print(f"Endereço: {empresa.endereço}")
