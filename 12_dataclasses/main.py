from classes import Pessoa

if __name__ == "__main__":
    usuario = Pessoa(
        nome="",
        idade=0,
        email="",
        telefone="",
        profissao="",
        peso=0.0,
        altura=0.0
    )

    usuario.nome = "Ruth"
    usuario.idade = 18
    usuario.email = "ruth@gamil.com"
    usuario.telefone = "(61) 9 83734972"
    usuario.profissao = "Programadora"
    usuario.peso = 50
    usuario.altura = 1.64

    print(f"{usuario}, tenho {len(usuario)} anos. Segue meus dados:")
    print(f"Nome: {usuario.nome}")
    print(f"Email: {usuario.email}")
    print(f"Idade: {usuario.idade}")
    print(f"Telefone: {usuario.telefone}")
    print(f"Profissao: {usuario.profissao}")
    print(f"Peso: {usuario.peso}")
    print(f"Altura: {usuario.altura}")

    del(usuario)