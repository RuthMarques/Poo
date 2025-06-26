# bibloteca
import classes
# algoritimo principal
if __name__ =="__main__":
    # instancia o classe filho
    Filho = classes.Filho("","","","",0.0,0.0)

    try:
        Filho.nome = input("Informe o nome:").strip().title()
        Filho.email = input("Informe o e-mail:").strip().lower()
        Filho.telefone = input("Informe o telefone:").strip()
        Filho.genero = input("Informe o genero:").strip().title()
        Filho.peso = float(input("Informe o nome:").replace(",","."))
        Filho.altura = float(input("Informe a altura em metros:").replace(",","."))

        #atributo
        Filho.exibir_info()
    except Exception as e:
        print(f"Não foi possivel executar. {e}.")