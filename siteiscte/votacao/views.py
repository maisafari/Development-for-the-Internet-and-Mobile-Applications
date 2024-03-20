import loader
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .models import Questao, Opcao
from django.template import loader
from django.shortcuts import render
from .models import Questao
from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
def index(request):
    latest_question_list = Questao.objects.order_by('-pub_data')[:5]
    context = {'latest_question_list':latest_question_list}
    return render(request, 'votacao/index.html',context)
def detalhe(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    return render(request, 'votacao/detalhe.html',{'questao': questao})
def resultados(request, questao_id):
 questao = get_object_or_404(Questao, pk=questao_id)
 return render(request,'votacao/resultados.html',{'questao': questao})
def voto(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    try:
        opcao_seleccionada =questao.opcao_set.get(pk=request.POST['opcao'])

    except (KeyError, Opcao.DoesNotExist):
# Apresenta de novo o form para votar
        return render(request, 'votacao/detalhe.html', {'questao': questao,'error_message': "Não escolheu uma opção",})
    else:
        opcao_seleccionada.votos += 1
        opcao_seleccionada.save()
        return HttpResponseRedirect(reverse('votacao:resultados',args=(questao.id,)))


def criar_opcao(request, questao_id):
    if request.method == 'POST':
        questao = Questao.objects.get(pk=questao_id)
        opcao_texto = request.POST.get('opcao_texto')
        opcao = Opcao.objects.create(questao=questao, opcao_texto=opcao_texto)
        return redirect('votacao:detalhe', questao_id=questao_id)
    else:
        return render(request, 'votacao/criar_opcao.html', {'questao_id': questao_id})