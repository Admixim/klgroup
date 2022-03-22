# coding: utf-8
from django.shortcuts import render, redirect, get_object_or_404
from client.forms import *
from datetime import datetime


def client_list(request):
    """Список клиентов общий"""

    clients = Client.objects.all()
    return render(request, 'dist/handbk/person/client-list.html', {'results': clients})


def client_new(request):
    """Создание-добавление  нового клиента"""

    template_name = 'dist/handbk/person/client-new.html'
    if request.method == 'GET':
        personform = ClientForm(request.GET or None)
        formset = FilePersonFormset(queryset=FilePerson.objects.none())
    elif request.method == 'POST':
        personform = ClientForm(request.POST, )
        formset = FilePersonFormset(request.POST, request.FILES, )
        if personform.is_valid() and formset.is_valid():
            person = personform.save()
            for form in formset:
                instance = form.save(commit=False)
                instance.files_person = person
                instance.save()
            return redirect('/client/')
        else:
            print('Форма не верно заполнена')
    return render(request, template_name, {
        'form': personform,
        'formset': formset,
    })


def client_edit(request, pk):
    """Редактирования  данных  Физ лица"""

    person = get_object_or_404(Client, pk=pk)
    formset = FilePersonFormset(queryset=FilePerson.objects.none())
    if request.method == "POST":
        clientform = ClientForm(request.POST, instance=person, )
        formset = FilePersonFormset(request.POST, request.FILES, prefix=None)
        if clientform.is_valid() and formset.is_valid():
            print(formset)
            person = clientform.save()
            for form in formset:
                instance = form.save(commit=False)
                instance.files_person = person
                print(instance)
                instance.save()
            return redirect('/client/')
    else:
        form = ClientForm(instance=person)
        list_files = person.files_persons.all()
        template_name = 'dist/handbk/person/client-edit.html'
        data = {
            'form': form,
            'client': pk,
            'list_files': list_files,
            'formset': formset,
        }
        return render(request, template_name, data)


def company_list(request):
    """Список контрагентов общий"""

    company = Company.objects.all()
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
