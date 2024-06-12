""""
Crie um programa que cadastre o nome de 30 alunos em uma lista, e receba de cada aluno 5 notas de 0 a 10. 
O programa deverá retornar a média do aluno e indicar se o aluno está aprovado ou reprovado (média para aprovação = 7). 
Ao final, o programa deverá mostrar uma lista com o nome dos aprovados. Crie um repositório, suba no GitHub e poste o link.
"""

#Calcular a média

def calcular_media(notas):
    return sum(notas) / len(notas)

#Define a aprovação

def verifica_aprovacao(media):
    return media >= 7

def aluno ():
    alunos = []

    for i in range(30):
        nome = input(f' Informe o nome a ser cadastrado {i + 1}: ')
        notas = []

        while True:
            try:
                notas = list(map(float, input(f'Digite as 5 notas de {nome} separadas por espaço: ').split()))
                if len(notas) == 5:
                    break
                else:
                    print('Verifique se as 5 notas foram informadas corretamente.')
            except:
                print('Verifique os valores informados.')

        media = calcular_media(notas)
        aprovacao = verifica_aprovacao(media)
        alunos.append(nome, media, aprovacao)

    aprovados = [aluno[0] for aluno in alunos if aluno [2]]

    print('\n LISTA DE APROVADOS')
    for aprovado in aprovados:
        print(aprovado)