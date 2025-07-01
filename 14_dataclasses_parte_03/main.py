from classes import PessoaFisica, PessoaJuridica
import os

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    usuario = PessoaFisica(nome="", profissao="", genero="",
                           email="", telefone="", endereco="")
    empresa = PessoaJuridica(nome_fantasia="", cnpj="", website="",
                           email="", telefone="", endereco="")
    
    limpar()
    print(f"{'-'*20} DADOS DO USUARIO {'-'*20}")
    usuario.nome = input("Informe o nome do usuario: ").strip().title()
    usuario.profissão = input("Informe a profissão do usuario: ").strip()
    usuario.genero = input("Informe o genero do usuario: ").strip()
    usuario.email = input("Informe o email do usuario: ").strip().lower()
    usuario.telefone= input("Informe o telefone do usuario: ").strip()
    usuario.endereco = input("Informe o endereço  do usuario: ").strip().title()

    print(f"{'-'*20} DADOS DA EMPRESA {'-'*20}")
    empresa.nome_fantasia = input("Informe o nome fantasia da empresa: ").strip().title()
    empresa.cnpj = input("Informe o CNPJ da empresa: ").strip()
    empresa.website = input("Informe o website da empresa: ").strip().lower()
    empresa.email = input("Informe o email da empresa: ").strip().lower()
    empresa.telefone= input("Informe o telefone da empresa: ").strip()
    empresa.endereco = input("Informe o endereço  da empresa: ").strip().title()

    limpar()

    # saida de dados 
    print(f"{usuario}. Segue meus dados: ")
    usuario.exibir_dados()
    print(f"{empresa}. Segue os dados da empresa: ")
    empresa.exibir_dados()

    # destroi os objetos 
    del(usuario)
    del(empresa)
