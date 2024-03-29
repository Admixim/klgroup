# coding: utf-8
# тесст модули
from auto.forms import AutoForm, FileAutoFormset, InsuranceAutoFormset
from auto.models import *

print('Hello')
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import AccidentForm, AccidentAddPartnerForm
from client.models import Client, Partner
from client.forms import PartnerForm, ClientForm







def techerjs(request):
    # Учебная страница по JS
    Carmodels = Car.objects.all()
    print(Carmodels)
    for item in Carmodels:
        print(item)
        print(item)
    brand = Brend.objects.all()
    print(brand)
    modelall = Model.objects.all()
    for item in modelall:
        print('id Модели:', item.pk, ';', 'Имя модели ТС: ', item.name, ';', 'id Марки ТС', item.brand_auto.pk,  ';', 'Имя ТС:', item.brand_auto.name)
    if request.method == 'POST':
        autoform = AutoForm(request.POST, prefix=Car)
        if autoform.is_valid():
            auto = autoform.save()
        return redirect('/auto/')

    template_name = 'dist/techerjs.html'
    autoform = AutoForm(prefix=Car)

    return render(request, template_name, {
            'autoform': autoform,
        })


def accident_list(request):
    # Список ДТП общий

    accident = Accident.objects.all()

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
            inst.save()
            return redirect('/accident/accident-add-partner/%d/' % (inst.pk))
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
    expert_list = accident.expert_accident.all()
    court = accident.court_info
    if request.method == "POST":
        # form = AccidentAddPartnerForm(request.POST,request.FILES or None, prefix='accident',instance=accident)
        add_partner = PartnerForm(request.POST, request.FILES or None, prefix='partners')
        if add_partner.is_valid():
            form = add_partner.save(commit=False)
            # Сохранение связей ДТП
            form.accident = accident
            # pforms =pform.save(commit=False)
            form.save()
            # pform.save()
            # return redirect('/accident/edit/%d/accident-add-partner/' % (pk)+ str(form.id)+ '/')
            return redirect('/accident/accident-add-partner/%d/' % pk, '/')
    else:
        list_partner = accident.partner_accident.all()
    add_partner = PartnerForm(prefix='partners')
    form = AccidentAddPartnerForm(prefix='accident', instance=accident)
    template_name = 'dist/accident/add_partner.html'
    return render(request, template_name, {'form': form,
                                           'add_partner': add_partner,
                                           'list_partner': list_partner,
                                           'accident_pk': pk,
                                           'expert_list': expert_list,
                                           'court': court,
                                           }
                  )


def accident_edit(request, pk):
    """Редактирования  данных ДТП"""

    accident = get_object_or_404(Accident, pk=pk)
    list_partner = accident.partner_accident.all()
    if request.method == "POST":
        form = AccidentAddPartnerForm(request.POST, request.FILES, prefix='accident', instance=accident)
        client = ClientForm(request.POST, request.FILES, prefix='client')
        add_partner = PartnerForm(request.POST, request.FILES, prefix='partners')
        if form.is_valid() and add_partner.is_valid() and client.is_valid():
            _date = form.cleaned_data['data']
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
    """ТЕСТОВЫЙ ВАРИАНТ С ШАБЛОНОМ Главная страница по ДТП добавление данных изменение данных"""

    error = 'Ошибка'
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


def accident_list_doc(request, pk):
    """ТЕСТОВЫЙ ВАРИАНТ С ШАБЛОНОМ  Документы"""

    accident = get_object_or_404(Accident, pk=pk)
    court = accident.court_info
    if request.method == 'POST':
        form = AccidentForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form = form.save(commit=False)
            form.save()
            return redirect('/Accident/')
        else:
            error = ' Форма не верно заполнена'
    try:
        list_client = accident.partner_accident.all()
    except AttributeError:
        list_client = None
    try:
        list_car = accident.partner_accident.all()
        print('list_car', list_car)
    except AttributeError:
        list_car = None
    try:
        list_expert = accident.expert_accident.all()
    except AttributeError:
        list_expert = None
    try:
        list_court = accident.court_info.info_courts.all()
    except AttributeError:
        list_court = None
    form = AccidentForm()
    data = {
        'list_court': list_court,
        'list_client': list_client,
        'list_car': list_car,
        'list_expert': list_expert,
        'accident_pk': pk,
        'form': form,
        'court': court,
        'expert_list': list_expert,
    }
    template_name = 'dist/accident/accident-list-doc.html'
    return render(request,
                  template_name,
                  data
                  )


def accident_edit1(request, pk):
    """Редактирования  данных ДТП"""

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
    # self.partner_accident.filter(type='True').first()
    return HttpResponse(f'{acc.car.model}')
