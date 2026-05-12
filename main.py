from clientes import pedir_nome, pedir_notas, calcular_media, resultado
from database import cadastrar_aluno

print("CADASTRO DE NOTAS FATEC")

nome = pedir_nome()

n1 = pedir_notas("N1")
n2 = pedir_notas("N2")
media = calcular_media(n1, n2)
situacao = resultado(media)

print(f"A média do aluno {nome} é {media:.1f}!")
print(situacao)

cadastrar_aluno(nome, n1, n2, media, situacao)