def pedir_nome():
    print("----------------------------")
    nome = input("Digite o nome do aluno: ")
    print("----------------------------")
    return nome

def pedir_notas(nome_nota):
    nota = float(input(f"Digite a nota da {nome_nota}:").replace(",", "."))
    return nota

def calcular_media(n1 , n2):
    media = (n1 * 0.4) + (n2 * 0.6)
    return media

def resultado(media):
    if media >= 6:
        return "Aprovado!"
    else:
        return "Reprovado."