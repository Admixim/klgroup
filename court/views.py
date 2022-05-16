# coding: utf-8
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import inlineformset_factory
from .models import Court, InfoCourt
from .forms import CourtInfoForm, CourtForm
from accident.models import Accident


def court_list(request):
    """Список клиентов общий"""
    court_info = InfoCourt.objects.all()
    return render(request, 'dist/court/list.html', {'court_info': court_info
                                                    }
                  )


def court_new(request):
    """Создание-добавление  новой судопроизводства"""
    error = ''
    if request.method == 'POST':
        infoform = CourtInfoForm(request.POST, request.FILES, prefix=InfoCourt)
        courtform = CourtForm(request.POST, request.FILES, prefix=Court)
        if infoform.is_valid() and courtform.is_valid():
            infoform.save()
            courtform.save()
            return redirect('/court/')
    else:
        error = ' Форма не верно заполнена'
    court_info = CourtInfoForm(prefix=InfoCourt)
    courtform = CourtForm(prefix=Court)
    template_name = 'dist/court/new.html'
    data = {'court_info': court_info,
            'courtform': courtform,
            'error': error,

            }

    return render(request, template_name, data)




def court_event_add(request, pk):
    """Создание-добавление  нового судебного события"""

    accident = Accident.objects.get(id=pk)
    accident_pk = accident.pk
    court_info = accident.court_info
    court_list =Court.objects.all(court_info=pk)

    if request.method == 'POST':
        form = CourtForm(request.POST, request.FILES)
        print('CourtForm', form)
        if form.is_valid():
            print('До', form.cleaned_data)
            court = form.save(commit=False)
            court.info_court = court_info
            court.save()


            return redirect('/')
    CourtForms = CourtForm()
    template_name = 'dist/court/event/read_court_add_event.html'
    data = {'court_info': court_info,
            'court': CourtForms,
            'court_list': court_list,
            'accident_pk': accident_pk
            }

    return render(request, template_name, data)


def court_new_pk(request, pk):
    """Создание добавление нового судопрозводства к ДТП"""

    accident = Accident.objects.get(id=pk)
    accident_pk = accident.pk
    court_info = accident.court_info
    # court_info_id = accident.court_info.pk
    # print(court_info_id)

    # court_info1 = get_object_or_404(Court, id=accident.court_info.pk)
    # print(court_info1)
    court_list: list = []
    # court:list = []
    if court_info is not None:
        print(court_info, 'инфо о деле')
        court_list: list = court_info.info_courts.all()
        # court_info = CourtInfoForm(prefix='court-info', instance=court_info)
        print('Случай информации о деле существует', )
    else:
        court_list: list = []
        # court_info = CourtInfoForm(prefix='court-info', instance=court_info)
        # court_info = CourtInfoForm(prefix='court-info', instance=court_info)
        # court = CourtForm(instance=Court, prefix='court')
        error = 'Операции по  судопроизводсту нет'
        print('Случай есть информация о деле, список операций  по делу пустой', )
    if request.method == 'POST':
        courtinfoForm = CourtInfoForm(request.POST, request.FILES, prefix='court-info', instance=court_info)
        if courtinfoForm.is_valid():
            inst = courtinfoForm.save(commit=False)
            inst.save()
            accident.courtinfoForm = inst
            accident.save()
            print(' Форма заполнена успешно и сохранена с привязкой к ДТП', accident.pk)
            return redirect('/court/court-event-add/%d/' % accident_pk)
        else:
            error = 'Форма не верно заполнена'

    courtinfoForm = CourtInfoForm(prefix='court-info', instance=court_info)
    template_name = 'dist/court/new_pk.html'
    # template_name = 'dist/court/event/modal_event.html'
    data = {
        # 'error': error,
        'accident_pk': accident_pk,
        'court_info': courtinfoForm,
        'court_list': court_list,

    }
    return render(request, template_name, data)


def court_new_pk(request, pk):
    """Создание добавление нового судопрозводства к ДТП"""

    accident = Accident.objects.get(id=pk)
    accident_pk = accident.pk
    court_info = accident.court_info
    # court_info1 = get_object_or_404(Court, id=accident.court_info.pk)
    # print(court_info1)
    court_list:list = []
    # court:list = []
    if court_info is not None:
        court_list: list = court_info.info_courts.all()
        # court_info = CourtInfoForm(prefix='court-info', instance=court_info)
        # court = CourtForm(instance=Court, prefix='court')
        print('Случай нет информации о деле', )
    else:
        court_list:list = []
        court_info = CourtInfoForm(prefix='court-info', instance=court_info)
        # court_info = CourtInfoForm(prefix='court-info', instance=court_info)
        # court = CourtForm(instance=Court, prefix='court')
        error = 'Операции по  судопроизводсту нет'
        print('Случай есть информация о деле, список операций  по делу пустой', )
    if request.method == 'POST':
        courtinfo = CourtInfoForm(request.POST, request.FILES or None, prefix='court-info', instance=court_info)
        court = CourtForm(request.POST, request.FILES or None, prefix='court', instance=Court)
        if courtinfo.is_valid():
            inst = courtinfo.save(commit=False)
            inst.save()
            accident.court_info = inst
            accident.save()
            print(' Форма заполнена успешно и сохранена с привязкой к ДТП', inst.pk)
            return redirect('/court/court-new-pk/%d/' % pk)
        else:
            error = 'Форма не верно заполнена'

    court_info = CourtInfoForm(prefix='court-info', instance=court_info)
    court = CourtForm(prefix='court',)
    template_name = 'dist/court/new_pk.html'
    data = {
            # 'error': error,
            'accident_pk': accident_pk,
            'court_info': court_info,
            'court_list': court_list,
            'court': court,
            }
    return render(request, template_name, data)


def court_list_doc(request):
    template_name = 'dist/court/court-list-doc.html'
    return render(request, template_name)


def price_court_cash_new(request):
    error = ''
    template_name = 'dist/price/price-court-cash-new.html'
    return render(request, template_name)
