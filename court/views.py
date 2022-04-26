# coding: utf-8
from django.shortcuts import render,redirect, get_object_or_404
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
            'courtform':courtform,
            'error': error,


            }

    return render(request, template_name, data)


def court_edit(request, pk):
    """Создание-добавление  нового клиента"""

    # В шаблоне столит id 28 для ДТП и Экспертизы вывести в форму id  для корреткного перехода )

    # court_pk = get_object_or_404(InfoCourt, pk=1)
    # print(pk)
    accident = Accident.objects.all()
    error = ''
    if request.method == 'POST':
        infoform =CourtInfoForm(request.POST, prefix=InfoCourt)
        courtform = CourtForm(request.POST,  prefix=Court)
        print(infoform, '1d')
        if infoform.is_valid() and courtform.is_valid():
            infoform.save()
            courtform.save()

            return redirect('/court/court-edit/%d/' % (pk))
    else:
        error = ' Форма не верно заполнена'
    court_info = CourtInfoForm(prefix=InfoCourt)
    courtform = CourtForm(prefix=Court)
    template_name = 'dist/court/new_pk.html'
    data = {'court_info': court_info,
            'courtform': courtform,
            'error': error,
            'pk': pk,
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
        court_list:list = court_info.info_courts.all()
        # court_info = CourtInfoForm(prefix='court-info', instance=court_info)
        # court = CourtForm(instance=Court, prefix='court')
        print('Случай court_info is not None', )
    else:
        court_list:list = []
        # court_info = CourtInfoForm(prefix='court-info', instance=court_info)
        # court = CourtForm(instance=Court, prefix='court')
        error = 'Операции по  судопроизводсту нет'
        print('Случай court_list:list = ', )
    if request.method == 'POST':
        courtinfo = CourtInfoForm(request.POST, request.FILES or None, prefix='court-info', instance=court_info)
        court = CourtForm(request.POST, request.FILES or None, prefix='court', instance=Court)
        if courtinfo.is_valid():
            inst = courtinfo.save(commit=False)
            # inst = accident.court_info
            print('Форма инст.id', inst.pk)
            print('Форма инст', courtinfo)
            inst.save()
            print(inst.pk)
            accident.court_info_id = inst.pk
            # print(accident.court_info)
            print('Случай if courtinfo.is_valid() and court.is_valid():', )
            return redirect('/court/court-new-pk/%d/' % pk)
        else:
            error = 'Форма не верно заполнена'
            print('Случай error = Форма не верно заполнен', )

    court_info = CourtInfoForm(prefix='court-info', )
    court = CourtForm(prefix='court')
    template_name = 'dist/court/new_pk.html'
    data = {
            'error': error,
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

