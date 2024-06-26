import glob
import os
from datetime import datetime

from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, get_object_or_404, redirect
from .forms import AlunoForm, UserRegistoForm
from .models import Questao, Opcao, Aluno, Administrador
from django.template import loader
from django.http import Http404, HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.files.storage import FileSystemStorage

def is_administrador(user):
    return user.is_authenticated and user.is_superuser  # Assuming superuser is equivalent to administrator

administrador_required = user_passes_test(is_administrador, login_url='/login/')
@login_required
def index(request):
    latest_question_list = Questao.objects.order_by('-pub_data')[:5]
    aluno = None
    file_url = render_file(request)
    if not request.user.is_superuser:
        aluno, created = Aluno.objects.get_or_create(user=request.user, defaults={'curso': 'Default Curso', 'votos': 0})
    context = {'is_aluno': bool(aluno), 'latest_question_list': latest_question_list, 'file_url': file_url}

    return render(request, 'votacao/index.html', context)

@login_required
def detalhe(request, questao_id):
    file_url = render_file(request)
    questao = get_object_or_404(Questao, pk=questao_id)
    return render(request, 'votacao/detalhe.html',{'questao': questao, 'file_url': file_url})
@login_required
def resultados(request, questao_id):
    file_url = render_file(request)
    questao = get_object_or_404(Questao, pk=questao_id)
    return render(request,
'votacao/resultados.html',{'questao': questao,'file_url': file_url})

@login_required
def voto(request, questao_id):

    if request.method == 'POST':

        if 'Votar' in request.POST['action']:
            print("a")
            questao = get_object_or_404(Questao, pk=questao_id)
            opcao_id = request.POST.get('opcao_id')
            try:
                opcao_selecionada = questao.opcao_set.get(pk=opcao_id)
            except (KeyError, Opcao.DoesNotExist):
                return render(request, 'votacao/detalhe.html', {'questao': questao, 'error_message': 'Não escolheu uma opção'})
            else:
                opcao_selecionada.votos += 1
                opcao_selecionada.save()

                # Verificar se o usuário é um aluno ou administrador
                if hasattr(request.user, 'aluno'):
                    aluno = request.user.aluno
                    if aluno.votos == aluno.limite:
                        return render(request, 'votacao/detalhe.html', {'questao': questao,'error_message': 'Limite de votos atingido'})
                    else:
                        aluno.votos += 1
                    aluno.save()
                elif hasattr(request.user, 'administrador'):
                    administrador = request.user.administrador
                    if administrador.votos == administrador.limite:
                        return render(request, 'votacao/detalhe.html', {'questao': questao,'error_message': 'Limite de votos atingido'})
                    else:
                        administrador.votos += 1
                    administrador.save()

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
                    return redirect('votacao:detalhe', questao_id=questao_id)

    return redirect('votacao:index')

@administrador_required
def criar_questao(request):
    file_url = render_file(request)
    if request.method == 'POST':
        texto_questao = request.POST.get('questao_texto')
        if texto_questao:
            nova_questao = Questao(questao_texto=texto_questao, pub_data=datetime.now())
            nova_questao.save()
            return redirect('votacao:index')
        else:
            return render(request, 'votacao/criar_questao.html', {'erro': 'Texto da questão é obrigatório', 'file_url': file_url})
    else:
        return render(request, 'votacao/criar_questao.html', {'file_url': file_url})

@administrador_required
def criar_opcao(request, questao_id):
    file_url = render_file(request)
    questao = get_object_or_404(Questao, pk=questao_id)

    if request.method == 'POST':
        opcao_texto = request.POST.get('opcao_texto')
        if opcao_texto:
            nova_opcao = Opcao(questao=questao, opcao_texto=opcao_texto)
            nova_opcao.save()
            return redirect('votacao:detalhe', questao_id=questao_id)
        else:
            return render(request, 'votacao/criar_opcao.html', {'questao': questao, 'erro': 'Texto da opção é obrigatório', 'file_url': file_url})
    else:
        return render(request, 'votacao/criar_opcao.html', {'questao': questao, 'file_url': file_url})

@administrador_required
def remover_questao(request, questao_id):
    file_url = render_file(request)
    if request.method == 'POST':
        questao_id = request.POST.get('questao_id')
        questao = get_object_or_404(Questao, pk=questao_id)
        questao.delete()
        return redirect('votacao:index')
    else:
        return redirect('votacao:index')


def registo_user(request):
    file_url = render_file(request)
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
    file_url = render_file(request)
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            request.session['username'] = user.username  # Armazena o username na sessão
            limite(request)
            file_url = render_file(request)

            return render(request, 'votacao/index.html', {'file_url': file_url})

    else:
        form = AuthenticationForm()
    return render(request, 'votacao/login.html', {'form': form})

@login_required
def logoutview(request):
    logout(request)
    return redirect(reverse('votacao:login'))

@login_required
def infopessoal(request):
    file_url = render_file(request)
    return (
        render(request, 'votacao/infopessoal.html', {'request': request, 'file_url': file_url}))

@login_required
def votosCount(request):
     count = 0

@login_required
def limite(request):
    if hasattr(request.user, 'aluno'):
        aluno = request.user.aluno
        grupo = aluno.grupo
        ultimo_digito = int(aluno.grupo[-1])  # Último dígito do grupo
        print(ultimo_digito)
        aluno.limite = ultimo_digito + 5
        aluno.save()

@login_required
def base_view(request):
    return

@login_required()
def fazer_upload(request):
    if request.method == 'POST' and request.FILES.get('myfile') is not None :
        user = request.user
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = user.username + "_" + myfile.name
        filename = fs.save(filename, myfile)
        uploaded_file_url = fs.url(filename)
        file_url = render_file(request)
        return render(request, 'votacao/fazer_upload.html', {'uploaded_file_url': uploaded_file_url, 'file_url': file_url})
    file_url = render_file(request)
    return render(request,'votacao/fazer_upload.html', {'file_url': file_url})


@login_required
def render_file(request):
    file_pattern = os.path.join(settings.MEDIA_ROOT, f"{request.user.username}_*.*")
    matching_files = glob.glob(file_pattern)

    if matching_files:
        file_path = matching_files[0]
        file_name = os.path.basename(file_path)
        file_url = os.path.join(settings.MEDIA_URL, file_name)
    else:
        file_url = None

    return file_url