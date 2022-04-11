# coding: utf-8

from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import AccidentForm, AccidentAddPartnerForm
from client.models import Client, Partner
from client.forms import PartnerForm, ClientForm



def accident_list(request):
    # Список ДТП общий

    accident = Accident.objects.all()
    print(accident)
    return render(request,
                  'dist/accident/list.html',
                  {'accident': accident,
                   }
                  )





def accident_new(request):
    # Создание-добавление  нового ДТП

    error = ''
    if request.method == 'POST':
        form = AccidentForm(request.POST, request.FILES)
        if form.is_valid():
            inst = form.save(commit=False)
            # поле которое необходимо заполнить датой 'data'
            inst.save()
            return redirect('/accident/edit/%d/' %(inst.pk))
    else:
        error = ' Форма не верно заполнена'
    form = AccidentForm()
    data = {
                'form': form,
                'error': error
                }
    template_name = 'dist/accident/new.html'
    return render(request,
                  template_name,
                  data
                  )

def accident_add_partner(request, pk):
    # Добавление участников  в дело о  ДТП

    accident = get_object_or_404(Accident, pk=pk)
    list_partner = accident.partner_accident.all()
    if request.method == "POST":
        #form = AccidentAddPartnerForm(request.POST,request.FILES or None, prefix='accident',instance=accident)
        form = PartnerForm(request.POST, request.FILES or None, prefix='partners')
        if form.is_valid():
            # _date = form.cleaned_data['data']
            # print(_date)
            form = form.save(commit=False)
            # Сохранение связей ДТП
            form.accident = accident
            #pforms =pform.save(commit=False)
            form.save()
            #pform.save()
            print(pk)
            print(form, 'f')
            print(type(form))
            # return redirect('/accident/edit/%d/accident-add-partner/' % (pk)+ str(form.id)+ '/')
            return redirect('/accident/edit/%d/' % (pk), '/')

    else:
        form = AccidentAddPartnerForm(prefix='accident', instance=accident)
        add_partner = PartnerForm(prefix='partners')
        list_partner = accident.partner_accident.all()
    template_name = 'dist/accident/add_partner.html'

    return render(request, template_name, {'form': form,
                                        'add_partner': add_partner,
                                        'list_partner': list_partner,
                                        'accident_pk': pk,
                                       }
              )


def accident_edit(request, pk):
    # Редактирования  данных ДТП

    accident = get_object_or_404(Accident, pk=pk)
    list_partner = accident.partner_accident.all()
    if request.method == "POST":
        form = AccidentAddPartnerForm(request.POST, request.FILES, prefix='accident', instance=accident)
        client = ClientForm(request.POST, request.FILES, prefix='client')
        add_partner = PartnerForm(request.POST, request.FILES, prefix='partners')
        if form.is_valid() and add_partner.is_valid() and client.is_valid():
            print(form)
            _date = form.cleaned_data['data']
            print(_date)
            _date = '10.01.2022'
            print('Дата форматирования', _date)

            accident = form.save(commit=False)
            list_partner = add_partner.save(commit=False)
            print('Список экспертиз ДТП', accident.expert_set)

            client = client.save()
            accident.save()
            list_partner.save()
            return redirect('/accident/edit/%d/' % (accident.id))
    else:
        form = AccidentAddPartnerForm(prefix='accident', instance=accident)
        add_partner = PartnerForm(prefix='partners')
        list_partner = accident.partner_accident.all()
        client = ClientForm(request.POST, request.FILES, prefix='client')
        template_name = 'dist/accident/edit.html'

    return render(request, template_name, {'form': form,
                                           'Accident': Accident,
                                           'add_partner': add_partner,
                                           'list_partner': list_partner,
                                           'accident_pk': pk,
                                           'client': client
                                           }
                  )


def accident_main1(request):
    # ТЕСТОВЫЙ ВАРИАНТ С ШАБЛОНОМ Главная страница по ДТП добавление данных изменение данных

    error = ''
    if request.method == 'POST':
        form = AccidentForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            form = form.save(commit=False)
            form.save()
            return redirect('/Accident/')
        else:
            error = ' Форма не верно заполнена'

    form = AccidentForm()
    data = {
        'form': form,
        'error': error
    }
    template_name = 'dist/accident-main1.html'
    return render(request,
                  template_name,
                  data
                  )


def accident_list_doc(request):
    # ТЕСТОВЫЙ ВАРИАНТ С ШАБЛОНОМ  Документы

    error = ''
    if request.method == 'POST':
        form = AccidentForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            form = form.save(commit=False)

            form.save()
            return redirect('/Accident/')
        else:
            error = ' Форма не верно заполнена'

    form = AccidentForm()
    data = {
        'form': form,
        'error': error
    }
    template_name = 'dist/accident/accident-list-doc.html'
    return render(request,
                  template_name,
                  data
                  )




def accident_edit1(request, pk):
    # Редактирования  данных ДТП

    accident = get_object_or_404(Accident, pk=pk)
    accident.get_accident()
    partner = get_object_or_404(Partner)
    if request.method == "POST":
        form = AccidentAddPartnerForm(request.POST, instance=accident)

        if form.is_valid():
            # _date = form.cleaned_data['date_birth']
            # print(_date)
            client = form.save(commit=False)
            client.save()
            return redirect('/accident/')

    else:
        form = AccidentAddPartnerForm(instance=accident)
        template_name = 'dist/accident/edit.html'
    return render(request, template_name, {'form': form,
                                           'Accident': pk
                                           }
                  )




def test(request):
    acc = Partner.objects.filter(accident_id=1).first()
    acc1 = Partner.objects.filter(accident_id=1)
    print(acc1[0].car.number)
    print(acc.car.model)
    #self.partner_accident.filter(type='True').first()
    return HttpResponse(f'{acc.car.model}')

