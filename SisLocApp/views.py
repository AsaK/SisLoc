from django.shortcuts import render
from models import Users
import datetime
import hashlib

# Create your views here.
def index(request):
    return render(request, 'SisLocApp/index.html')

def users(request):
    action = request.GET.get('action')
    if action == 'criar':
        inputNome = request.GET.get('inputNome')
        if inputNome is not None:
            inputUsuario = request.GET.get('inputUsuario')
            inputEmail = request.GET.get('inputEmail')
            inputTipo = request.GET.get('inputTipo')
            inputSenha = request.GET.get('inputSenha')
            newUser = Users()
            newUser.name = inputNome
            newUser.username = inputUsuario
            newUser.email = inputEmail
            newUser.type = inputTipo
            newUser.password = hashlib.md5(inputSenha).hexdigest()
            newUser.creation_date = datetime.datetime.now()
            newUser.save()
            UsersResult = Users.objects.all()
            return render(request, 'SisLocApp/users.html', {'UsersResult': UsersResult,
                                                            'action': 'listar',
                                                            'status': 'created'})
        return render(request, 'SisLocApp/users.html', {'action': 'criar'})
    elif action == 'excluir':
        UsersResult = Users.objects.all()
        inputExcluir = request.GET.get('inputExcluir')
        if inputExcluir is None:
            return render(request, 'SisLocApp/users.html', {'UsersResult': UsersResult,
                                                            'action': 'listar',
                                                            'status': 'warning'})
        userDeleted = Users.objects.filter(id=inputExcluir)
        userDeleted.delete()
        return render(request, 'SisLocApp/users.html', {'UsersResult': UsersResult,
                                                        'action': 'listar',
                                                        'status': 'deleted'})
    elif action == 'alterar':
        inputAlterar = request.GET.get('inputAlterar')
        UsersResult = Users.objects.get(id=inputAlterar)
        inputNome = request.GET.get('inputNome')
        if inputNome is None:
            return render(request, 'SisLocApp/users.html', {'UsersResult': UsersResult,
                                                            'action': 'alterar'})
        inputEmail = request.GET.get('inputEmail')
        inputTipo = request.GET.get('inputTipo')
        inputAlterarSenha = request.GET.get('inputAlterarSenha')
        UsersResult.name = inputNome
        UsersResult.email = inputEmail
        UsersResult.type = inputTipo
        if inputAlterarSenha == 'on':
            UsersResult.password = request.GET.get('inputSenha')
        UsersResult.save()
        UsersResult = Users.objects.all()
        return render(request, 'SisLocApp/users.html', {'UsersResult': UsersResult,
                                                'action': 'listar',
                                                'status': 'updated'})

    else:
        UsersResult = Users.objects.all()
        return render(request, 'SisLocApp/users.html', {'UsersResult': UsersResult,
                                                        'action': 'listar'})
