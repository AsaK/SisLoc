from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from models import Users, Customers, Product, Features, Booking
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
            page = request.GET.get('pagina')
            paginator = Paginator(UsersResult, 20) #Show 20 per page
            try:
                UsersResult  = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                UsersResult  = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                UsersResult  = paginator.page(paginator.num_pages)
            return render(request, 'SisLocApp/users.html', {'UsersResult': UsersResult,
                                                            'action': 'listar',
                                                            'status': 'created'})
        return render(request, 'SisLocApp/users.html', {'action': 'criar'})
    elif action == 'excluir':
        inputExcluir = request.GET.get('inputExcluir')
        userDeleted = Users.objects.filter(id=inputExcluir)
        userDeleted.delete()
        UsersResult = Users.objects.all()
        page = request.GET.get('pagina')
        paginator = Paginator(UsersResult, 20) #Show 20 per page
        try:
            UsersResult  = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            UsersResult  = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            UsersResult  = paginator.page(paginator.num_pages)
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
        page = request.GET.get('pagina')
        paginator = Paginator(UsersResult, 20) #Show 20 per page
        try:
            UsersResult  = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            UsersResult  = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            UsersResult  = paginator.page(paginator.num_pages)
        return render(request, 'SisLocApp/users.html', {'UsersResult': UsersResult,
                                                        'action': 'listar',
                                                        'status': 'updated'})
    else:
        UsersResult = Users.objects.all()
        page = request.GET.get('pagina')
        paginator = Paginator(UsersResult, 20) #Show 20 per page
        try:
            UsersResult  = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            UsersResult  = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            UsersResult  = paginator.page(paginator.num_pages)
        return render(request, 'SisLocApp/users.html', {'UsersResult': UsersResult,
                                                        'action': 'listar'})


def customers(request):
    action = request.GET.get('action')
    if action == 'criar':
        inputNome = request.GET.get('inputNome')
        if inputNome is not None:
            inputEmail = request.GET.get('inputEmail')
            inputTipo = request.GET.get('inputTipo')
            inputAtivo = request.GET.get('inputAtivo')
            newCustomer = Customers()
            newCustomer.name = inputNome
            newCustomer.email = inputEmail
            newCustomer.type = inputTipo
            if inputAtivo is not None:
                newCustomer.enabled = 'S'
            else:
                newCustomer.enabled = 'N'
            newCustomer.creation_date = datetime.datetime.now()
            newCustomer.save()
            CustomersResult = Customers.objects.all()
            page = request.GET.get('pagina')
            paginator = Paginator(CustomersResult, 20) #Show 20 per page
            try:
                CustomersResult  = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                CustomersResult  = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                CustomersResult  = paginator.page(paginator.num_pages)
            return render(request, 'SisLocApp/customers.html', {'CustomersResult': CustomersResult,
                                                                'action': 'listar',
                                                                'status': 'created'})

        return render(request, 'SisLocApp/customers.html', {'action': 'criar'})
    elif action == 'excluir':
        inputExcluir = request.GET.get('inputExcluir')
        CustomerDeleted = Customers.objects.filter(id=inputExcluir)
        CustomerDeleted.delete()

        CustomersResult = Customers.objects.all()
        page = request.GET.get('pagina')
        paginator = Paginator(CustomersResult, 20) #Show 20 per page
        try:
            CustomersResult  = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            CustomersResult  = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            CustomersResult  = paginator.page(paginator.num_pages)
        return render(request, 'SisLocApp/customers.html', {'CustomersResult': CustomersResult,
                                                            'action': 'listar',
                                                            'status': 'deleted'})
    elif action == 'alterar':
        inputAlterar = request.GET.get('inputAlterar')
        CustomersResult = Customers.objects.get(id=inputAlterar)
        inputNome = request.GET.get('inputNome')
        if inputNome is None:
            return render(request, 'SisLocApp/customers.html', {'CustomersResult': CustomersResult,
                                                                'action': 'alterar'})
        inputEmail = request.GET.get('inputEmail')
        inputTipo = request.GET.get('inputTipo')
        inputAtivo = request.GET.get('inputAtivo')
        CustomersResult.name = inputNome
        CustomersResult.email = inputEmail
        CustomersResult.type = inputTipo
        if inputAtivo == 'on':
            CustomersResult.enabled = 'S'
        else:
            CustomersResult.enabled = 'N'
        CustomersResult.save()

        CustomersResult = Customers.objects.all()
        page = request.GET.get('pagina')
        paginator = Paginator(CustomersResult, 20) #Show 20 per page
        try:
            CustomersResult  = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            CustomersResult  = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            CustomersResult  = paginator.page(paginator.num_pages)
        return render(request, 'SisLocApp/customers.html', {'CustomersResult': CustomersResult,
                                                            'action': 'listar',
                                                            'status': 'updated'})
    else:
        CustomersResult = Customers.objects.all()
        page = request.GET.get('pagina')
        paginator = Paginator(CustomersResult, 20) #Show 20 per page
        try:
            CustomersResult  = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            CustomersResult  = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            CustomersResult  = paginator.page(paginator.num_pages)
        return render(request, 'SisLocApp/customers.html', {'CustomersResult': CustomersResult,
                                                            'action': 'listar'})

def products(request):
    action = request.GET.get('action')
    if action == 'criar':
        inputNome = request.GET.get('inputNome')
        if inputNome is not None:
            inputCapacidade = request.GET.get('inputCapacidade')
            inputTipo = request.GET.get('inputTipo')
            newProduct = Product()
            newProduct.name = inputNome
            newProduct.capacity = inputCapacidade
            newProduct.type = inputTipo[0]
            newProduct.creation_date = datetime.datetime.now()
            newProduct.save()
            ProductsResult = Product.objects.all()
            page = request.GET.get('pagina')
            paginator = Paginator(ProductsResult, 20) #Show 20 per page
            try:
                ProductsResult = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                ProductsResult = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                ProductsResult = paginator.page(paginator.num_pages)
            # FeaturesResult = Features.objects.all()
            return render(request, 'SisLocApp/products.html', {'ProductsResult': ProductsResult,
                                                               'action': 'listar',
                                                               'status': 'created'})
        return render(request, 'SisLocApp/products.html', {'action': 'criar'})
    elif action == 'excluir':
        inputExcluir = request.GET.get('inputExcluir')
        ProductDeleted = Product.objects.filter(id=inputExcluir)
        ProductDeleted.delete()

        ProductsResult = Product.objects.all()
        page = request.GET.get('pagina')
        paginator = Paginator(ProductsResult, 20) #Show 20 per page
        try:
            ProductsResult = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            ProductsResult = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            ProductsResult = paginator.page(paginator.num_pages)
        # FeaturesResult = Features.objects.all()
        return render(request, 'SisLocApp/products.html', {'ProductsResult': ProductsResult,
                                                           'action': 'listar',
                                                           'status': 'deleted'})
    elif action == 'alterar':
        inputAlterar = request.GET.get('inputAlterar')
        ProductsResult = Product.objects.get(id=inputAlterar)
        inputNome = request.GET.get('inputNome')
        if inputNome is None:
            return render(request, 'SisLocApp/products.html', {'ProductsResult': ProductsResult,
                                                               'action': 'alterar'})
        inputCapacidade = request.GET.get('inputCapacidade')
        inputTipo = request.GET.get('inputTipo')

        ProductsResult.name = inputNome
        ProductsResult.capacity = inputCapacidade
        ProductsResult.type = inputTipo[0]
        ProductsResult.save()

        ProductsResult = Product.objects.all()
        page = request.GET.get('pagina')
        paginator = Paginator(ProductsResult, 20) #Show 20 per page
        try:
            ProductsResult = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            ProductsResult = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            ProductsResult = paginator.page(paginator.num_pages)
        # FeaturesResult = Features.objects.all()
        return render(request, 'SisLocApp/products.html', {'ProductsResult': ProductsResult,
                                                           'action': 'listar',
                                                           'status': 'updated'})
    else:
        ProductsResult = Product.objects.all()
        page = request.GET.get('pagina')
        paginator = Paginator(ProductsResult, 20) #Show 20 per page
        try:
            ProductsResult = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            ProductsResult = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            ProductsResult = paginator.page(paginator.num_pages)
        # FeaturesResult = Features.objects.all()
        return render(request, 'SisLocApp/products.html', {'ProductsResult': ProductsResult,
                                                           'action': 'listar'})


def features(request):
    action = request.GET.get('action')
    if action == 'criar':
        inputNome = request.GET.get('inputNome')
        if inputNome is not None:
            newFeature = Features()
            newFeature.name = inputNome
            newFeature.creation_date = datetime.datetime.now()
            newFeature.save()
            FeaturesResult = Features.objects.all()
            page = request.GET.get('pagina')
            paginator = Paginator(FeaturesResult, 20) #Show 20 per page
            try:
                FeaturesResult = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                FeaturesResult = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                FeaturesResult = paginator.page(paginator.num_pages)
            # FeaturesResult = Features.objects.all()
            return render(request, 'SisLocApp/features.html', {'FeaturesResult': FeaturesResult,
                                                               'action': 'listar',
                                                               'status': 'created'})
        return render(request, 'SisLocApp/features.html', {'action': 'criar'})
    elif action == 'excluir':
        inputExcluir = request.GET.get('inputExcluir')
        FeatureDeleted = Features.objects.filter(id=inputExcluir)
        FeatureDeleted.delete()
        FeaturesResult = Features.objects.all()
        page = request.GET.get('pagina')
        paginator = Paginator(FeaturesResult, 20) #Show 20 per page
        try:
            FeaturesResult = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            FeaturesResult = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            FeaturesResult = paginator.page(paginator.num_pages)
        # FeaturesResult = Features.objects.all()
        return render(request, 'SisLocApp/features.html', {'FeaturesResult': FeaturesResult,
                                                           'action': 'listar',
                                                           'status': 'deleted'})
    elif action == 'alterar':
        inputAlterar = request.GET.get('inputAlterar')
        FeaturesResult = Features.objects.get(id=inputAlterar)
        inputNome = request.GET.get('inputNome')
        if inputNome is None:
            return render(request, 'SisLocApp/features.html', {'FeaturesResult': FeaturesResult,
                                                               'action': 'alterar'})
        FeaturesResult.name = inputNome
        FeaturesResult.save()

        FeaturesResult = Features.objects.all()
        page = request.GET.get('pagina')
        paginator = Paginator(FeaturesResult, 20) #Show 20 per page
        try:
            FeaturesResult = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            FeaturesResult = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            FeaturesResult = paginator.page(paginator.num_pages)
        # FeaturesResult = Features.objects.all()
        return render(request, 'SisLocApp/features.html', {'FeaturesResult': FeaturesResult,
                                                           'action': 'listar',
                                                           'status': 'updated'})
    else:
        FeaturesResult = Features.objects.all()
        page = request.GET.get('pagina')
        paginator = Paginator(FeaturesResult, 20) #Show 20 per page
        try:
            FeaturesResult = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            FeaturesResult = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            FeaturesResult = paginator.page(paginator.num_pages)
        # FeaturesResult = Features.objects.all()
        return render(request, 'SisLocApp/features.html', {'FeaturesResult': FeaturesResult,
                                                           'action': 'listar'})


def booking(request):
    action = request.GET.get('action')
    if action == 'criar':
        inputNome = request.GET.get('inputNome')
        if inputNome is not None:
            newFeature = Features()
            newFeature.name = inputNome
            newFeature.creation_date = datetime.datetime.now()
            newFeature.save()
            FeaturesResult = Features.objects.all()
            return render(request, 'SisLocApp/features.html', {'FeaturesResult': FeaturesResult,
                                                               'action': 'listar',
                                                               'status': 'created'})
        ProductsResult = Product.objects.all()
        return render(request, 'SisLocApp/booking.html', {'ProductsResult': ProductsResult,
                                                          'action': 'criar'})
    elif action == 'excluir':
        inputExcluir = request.GET.get('inputExcluir')
        FeatureDeleted = Features.objects.filter(id=inputExcluir)
        FeatureDeleted.delete()
        FeaturesResult = Features.objects.all()
        return render(request, 'SisLocApp/features.html', {'FeaturesResult': FeaturesResult,
                                                           'action': 'listar',
                                                           'status': 'deleted'})
    elif action == 'alterar':
        inputAlterar = request.GET.get('inputAlterar')
        FeaturesResult = Features.objects.get(id=inputAlterar)
        inputNome = request.GET.get('inputNome')
        if inputNome is None:
            return render(request, 'SisLocApp/features.html', {'FeaturesResult': FeaturesResult,
                                                               'action': 'alterar'})
        FeaturesResult.name = inputNome
        FeaturesResult.save()

        FeaturesResult = Features.objects.all()

        return render(request, 'SisLocApp/features.html', {'FeaturesResult': FeaturesResult,
                                                           'action': 'listar',
                                                           'status': 'updated'})
    else:
        BookingsResult = Booking.objects.all()
        page = request.GET.get('pagina')
        paginator = Paginator(BookingsResult, 20) #Show 20 per page
        try:
            BookingsResult = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            BookingsResult = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            BookingsResult = paginator.page(paginator.num_pages)
        return render(request, 'SisLocApp/booking.html', {'BookingsResult': BookingsResult,
                                                          'action': 'listar'})
