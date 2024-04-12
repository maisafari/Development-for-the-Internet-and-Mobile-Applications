from datetime import datetime

from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, get_object_or_404, redirect

from .forms import AlunoForm, UserRegistoForm
from .models import Questao, Opcao, Aluno
from django.template import loader
from django.http import Http404, HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout


def index(request):
    if request.user.is_authenticated:

        latest_question_list = Questao.objects.order_by('-pub_data')[:5]

        try:
            aluno = Aluno.objects.get(user=request.user)
        except Aluno.DoesNotExist:
            aluno = None

        context = {}
        if aluno:
            context['is_aluno'] = True
            context['latest_question_list'] = latest_question_list

        else:
            context['is_aluno'] = False
            context['latest_question_list'] = latest_question_list

        # Renderizar o template index.html com o contexto adequado
        return render(request, 'votacao/index.html', context)
    else:
        return redirect('votacao:login')


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

def registo_user(request):
    if request.method == 'POST':
        form_user = UserRegistoForm(request.POST)
        form_aluno = AlunoForm(request.POST)
        if form_user.is_valid() and form_aluno.is_valid():
            user = form_user.save()
            aluno = form_aluno.save(commit=False)
            aluno.user = user
            aluno.save()
            raw_password = form_user.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('votacao:index')  # Altere 'pagina_principal' para a página desejada após o registro
    else:
        form_user = UserRegistoForm()
        form_aluno = AlunoForm()
    return render(request, 'votacao/registo_user.html', {'form_user': form_user, 'form_aluno': form_aluno})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            request.session['username'] = user.username  # Armazena o username na sessão
            return redirect('votacao:index')
    else:
        form = AuthenticationForm()
    return render(request, 'votacao/login.html', {'form': form})

def logoutview(request):
    logout(request)
    return redirect(reverse('votacao:login'))

