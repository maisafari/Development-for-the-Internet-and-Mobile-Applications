from datetime import datetime

from django.shortcuts import render, get_object_or_404, redirect

from .models import Questao, Opcao
from django.template import loader
from django.http import Http404, HttpResponse,HttpResponseRedirect
from django.urls import reverse
def index(request):
    latest_question_list =Questao.objects.order_by('-pub_data')[:5]
    context = {'latest_question_list':latest_question_list}
    return render(request, 'votacao/index.html',context)
def detalhe(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    return render(request, 'votacao/detalhe.html',{'questao': questao})
def resultados(request, questao_id):
 questao = get_object_or_404(Questao, pk=questao_id)
 return render(request,
'votacao/resultados.html',{'questao': questao})
def voto(request, questao_id):
    if request.method == 'POST':
        if 'Votar' in request.POST['action']:
            questao = get_object_or_404(Questao, pk=questao_id)
            opcao_id = request.POST.get('opcao_id')
            try:
                opcao_selecionada = questao.opcao_set.get(pk=opcao_id)
            except (KeyError, Opcao.DoesNotExist):
                return render(request, 'votacao/detalhe.html', {'questao': questao, 'error_message': "Não escolheu uma opção"})
            else:
                opcao_selecionada.votos += 1
                opcao_selecionada.save()
                return HttpResponseRedirect(reverse('votacao:resultados', args=(questao.id,)))

        elif 'Remover' in request.POST['action']:
            opcao_id = request.POST.get('opcao_id')
            if opcao_id:
                q = get_object_or_404(Questao, pk=questao_id)
                try:
                    opcao_selecionada = q.opcao_set.get(pk=opcao_id)
                    opcao_selecionada.delete()
                    return redirect('votacao:detalhe', questao_id=questao_id)
                except (KeyError, Opcao.DoesNotExist):
                    return redirect('votacao:voto')

    return redirect('votacao:index')


def criar_questao(request):
    if request.method == 'POST':
        texto_questao = request.POST.get('questao_texto')
        if texto_questao:
            nova_questao = Questao(questao_texto=texto_questao, pub_data=datetime.now())
            nova_questao.save()
            return redirect('votacao:index')
        else:
            return render(request, 'votacao/criar_questao.html', {'erro': 'Texto da questão é obrigatório'})
    else:
        return render(request, 'votacao/criar_questao.html')

def criar_opcao(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)

    if request.method == 'POST':
        opcao_texto = request.POST.get('opcao_texto')
        if opcao_texto:
            nova_opcao = Opcao(questao=questao, opcao_texto=opcao_texto)
            nova_opcao.save()
            return redirect('votacao:detalhe', questao_id=questao_id)
        else:
            return render(request, 'votacao/criar_opcao.html', {'questao': questao, 'erro': 'Texto da opção é obrigatório'})
    else:
        return render(request, 'votacao/criar_opcao.html', {'questao': questao})

def remover_questao(request, questao_id):
    if request.method == 'POST':
        questao_id = request.POST.get('questao_id')
        questao = get_object_or_404(Questao, pk=questao_id)
        questao.delete()
        return redirect('votacao:index')
    else:
        return redirect('votacao:index')



