# '''
# Tarefa 02 - Dicionário.
#
#
# Competências relacionadas:
# - Saber manipular a estrutura de dicionário
# - Desenvolver uma solução viável para o problema
#
#
# Crie uma Classe Aluno com os seguintes atributos: nome, curso.
#
# class Aluno:
#     def __init__(self,nome,curso):
#         self.nome = nome
#         self.curso = curso
#
#
# Utilize para a tarefa as seguintes listas:
# lista_estados = ['RS','SC','SP','RJ','MG']
# lista_cursos = ['ADS','RDS','PMM','SPI']
#
# Dicionário para armazernar os dados:
# dic_estudantes = {}
#
#
# Considere o menu a baixo.
#
# MENU
# 1- Catalogar Aluno
# 2- Imprimir Alunos por Estado
# 3- Imprimir Alunos por Curso
# 4- Localizar um aluno por nome.
# Escolha:
#
# Na opção 1:
#     Você deverá escolher um dos estados conforme a lista_estados,
#     instanciar um aluno com nome e curso e armazenar essa informação em dic_estudantes
#     da seguinte forma:
#             - a key será um dos estados da lista_estados, e o
#             - value será uma lista com todas intâncias de alunos matriculados.
#         Exemplo: dic_estudantes = {
#                                 'RS' : [obj1, obj2, obj3] ,
#                                 'SC' : [obj4, obj5, obj6] ,
#                                 'SP' : [obj7, ...]
#                                 ...
#                                 }
#     obs: Não precisa consistência para verificar se o aluno está e mais de um curso, ou estado.
#
# Na opção 2:
#     Você deverá ler o estado, e do dicionário dic_estudantes, imprima os dados de todos alunos
#         do estado escolhido.
#
# Na opção 3:
#     Você deverá ler o nome de um curso, e mostrar o nome de todos alunos deste curso.
#     (busca em dic_estudantes)
#
# Na opção 4:
#     Você deverá ler o nome de um aluno e mostrar seu curso e estado onde este aluno está relacionado.
#
#
# '''
class Aluno:
    def __init__(self,nome,curso):
        self.nome = nome
        self.curso = curso
    def __str__(self):
        return f'{self.nome}, {self.curso} '

# listas:
lista_estados = ['RS','SC','SP','RJ','MG']
lista_cursos = ['ADS','RDS','PMM','SPI']
lista_alunos = []

# Dicionário perai, vou tentar lembrar
dic_estudantes = {}

# Catalogar
def Catalogar():
    nome = input('Aluno:')
    curso = input('Qual o curso que ele faz: ')
    lista_alunos.append(nome)
    print(f'O nome do aluno é: {nome}.')

    lista_estados = ['RS', 'SC', 'SP', 'RJ', 'MG']

    estado = input('Sigla do estado: ').upper()
    print(f'O curso que ele faz: {curso}.')
    while True:
        if estado in lista_estados:
            break
        else:
            print('Estado inválido')
            estado = input('Sigla do estado: ').upper()
    print(f'A sigla do estado que ele mora é: {estado}.')

    if not dic_estudantes.get(estado):
        dic_estudantes[estado] = [nome]
    elif dic_estudantes.get(estado):
        dic_estudantes[estado].append(nome)
    print(dic_estudantes)
def Mostrar():
    dict_from_list = dict(zip(dic_estudantes, [lista_cursos]))
    print(dict_from_list)
    print(dic_estudantes)


def menu():
    menu = """\033[1;93m
    MENU:

       1- Catalogar Aluno
       2- Imprimir Alunos por Estado
       3- Imprimir Alunos por Curso
       4- Localizar um aluno por nome

    ESCOLHA: \033[m
    """
    while True:
            escolha = input(menu)
            if escolha == '0':
                print('\033[1;31mVocê decidiu sair...\033[m'.upper())
                break
            elif escolha == '1':
                Catalogar()
            elif escolha == '2':
                Mostrar()
            elif escolha == '3':
                pass
            elif escolha == '4':
                pass
            else:
                print('\n\033[1;31mDigite um número válido...\033[m'.upper())
menu()


