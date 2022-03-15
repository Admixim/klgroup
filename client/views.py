# coding: utf-8
from django.shortcuts import render, redirect, get_object_or_404
from . import models
from client.forms import ClientForm, CompanyForm
from datetime import datetime


def client_list(request):
    """Список клиентов общий"""

    clients = models.Client.objects.all()
    return render(request, 'dist/handbk/person/client-list.html', {'results': clients})


def client_new(request):
    """Создание-добавление  нового клиента"""

    error = ''
    if request.method == 'POST':
        form = ClientForm(request.POST, prefix='client')
        print('test до валидации', form)
        if form.is_valid():
            print('test после валидации успешно пройден', form.cleaned_data)
            form = form.save(commit=False)
            form.save()
            return redirect('/client/')
        else:
            error = ' Форма не верно заполнена'

    form = ClientForm(prefix='client')
    data = {'form': form,
            'error': error
            }
    template_name = 'dist/handbk/person/client-new.html'
    return render(request, template_name, data)


def client_edit(request, pk):
    """"Редактирования  данных клиента"""

    client = get_object_or_404(models.Client, pk=pk)
    if request.method == "POST":
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            # date_birth = (datetime.strptime(str(form.cleaned_data['date_birth']), '%Y-%m-%d')).strftime("%d-%m-%Y" )
            client = form.save(commit=False)
            # print('row ', form.cleaned_data['data_create'])
            # print('strptime', datetime.strptime(str(form.cleaned_data['data_create']), '%Y-%m-%d'))
            # _data_create = form.cleaned_data['data_create'] #(datetime.strptime(str(form.cleaned_data['data_create']), '%Y-%m-%d')).strftime("%d-%m-%Y")
            # print('_date_create ', _data_create)
            # client.data_create = _data_create
            client.save()
            return redirect('/client/')

    else:
        form = ClientForm(instance=client)
        template_name = 'dist/handbk/person/client-edit.html'
        return render(request, template_name, {'form': form,
                                               'client': pk
                                               }
                      )


def company_list(request):
    """Список контрагентов общий"""

    company = models.Company.objects.all()
    return render(request, 'dist/handbk/contractor/company-list.html', {'results': company}
                  )


def company_new(request):
    """Создание-добавление  нового контрагента"""

    error = ''
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/client/company/')
        else:
            error = ' Форма не верно заполнена'

    form = CompanyForm()
    data = {'form': form,
            'error': error
            }
    template_name = 'dist/handbk/contractor/company-new.html'
    return render(request, template_name, data)


def company_edit(request, pk):
    """Редактирование данных контрагента"""

    company = get_object_or_404(models.Company, pk=pk)
    if request.method == "POST":
        form = CompanyForm(request.POST, instance=company, prefix='blabla')
        if form.is_valid():
            company = form.save(commit=False)
            company.save()
            return redirect('/client/company/')
    else:
        form = CompanyForm(instance=company, prefix='company')
        template_name = 'dist/handbk/contractor/company-edit.html'
    return render(request, template_name, {'form': form
                                           }
                  )
