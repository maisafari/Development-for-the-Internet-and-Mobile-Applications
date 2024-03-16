from datetime import datetime, timedelta

from votacao.models import Questao, Opcao

def mostrar_todas_questoes():
    questoes = Questao.objects.all()

    if questoes.exists():
        print('Lista de todas as questões:')
        for questao in questoes:
            print(f'- {questao.questao_texto}')
    else:
        print('Nenhuma questão encontrada.')

def mostrar_opcoes_gostas_de():
    questao = Questao.objects.filter(questao_texto__startswith='Gostas de').first()
    if questao:
        opcoes = Opcao.objects.filter(questao=questao)
        for opcao in opcoes:
            print(f'Opção: {opcao.opcao_texto}')
    else:
        print('Nenhuma questão encontrada com texto "Gostas de..."')


def mostrar_op_superior_a_2votos():
    questao = Questao.objects.filter(questao_texto__startswith='Gostas de').first()
    if questao:
        opcoes = Opcao.objects.filter(questao=questao, votos__gt=2)
        if opcoes.exists():
            print(f'Opções da questão com texto "Gostas de..." e votos > 2:')
            for opcao in opcoes:
                print(f'- Opção: {opcao.opcao_texto}, Votos: {opcao.votos}')
        else:
            print('Nenhuma opção encontrada com texto "Gostas de..." e votos > 2')
    else:
        print('Nenhuma questão encontrada com texto "Gostas de..."')


def mostrar_questoes_publicadas_ultimos_3_anos():
    data_limite = datetime.now() - timedelta(days=3 * 365)
    questoes = Questao.objects.filter(pub_data__gte=data_limite)
    if questoes.exists():
        print('Questões publicadas nos últimos 3 anos:')
        for questao in questoes:
            print(f'- {questao.questao_texto}')
    else:
        print('Nenhuma questão encontrada publicada nos últimos 3 anos.')


def mostrar_opcao_mais_votada():
    questoes = Questao.objects.all()

    for questao in questoes:
        print(f'Questão: {questao.questao_texto}')

        opcao_mais_votada = questao.opcao_set.order_by('-votos').first()

        if opcao_mais_votada:
            print(f'Opção mais votada: {opcao_mais_votada.opcao_texto} - Votos: {opcao_mais_votada.votos}')
        else:
            print('Nenhuma opção encontrada para esta questão.')