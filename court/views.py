# coding: utf-8
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import inlineformset_factory
from .models import Court, InfoCourt
from .forms import CourtInfoForm, CourtForm, CourtInfoAddForm
from accident.models import Accident


def court_list(request):
    """Список клиентов общий"""
    accident =Accident.objects.all()

    court_info = InfoCourt.objects.all()
    # for item in accident:
    #     if item.court_info:
    #         print('Инфокоурт', item.court_info.pk)
    #         print('ДТП', item.pk)
    #     else:
    #         print('Нет ИнфоКоурт')

    # for i in court_info:
    #     if i.court_info.all():
    #         print('ДТП строка', i.court_info.all())
    #     else:
    #
    #         print('Пусто', i.pk, i.case_number, i.data_reg)
    # print([items for items in court_info if court_info not in accident])
    return render(request,
                  'dist/court/list.html',
                  {'court_info': court_info,
                  }
                  )


def court_new(request):
    """Создание-добавление  новой судопроизводства"""
    error = ''
    if request.method == 'POST':
        court_info = CourtInfoForm(request.POST, request.FILES)
        if court_info.is_valid():
            court_info.save()
            return redirect('/court/')
    else:
        error = ' Форма не верно заполнена'
    court_info = CourtInfoForm()
    template_name = 'dist/court/new.html'
    data = {'court_info': court_info,
            'error': error,

            }

    return render(request, template_name, data)




def court_event_add(request, pk):
    """Создание-добавление  нового судебного события"""

    accident = Accident.objects.get(id=pk)
    accident_pk = accident.pk
    court_info = accident.court_info
    if court_info is not None:
        print(court_info, 'инфо о деле')
        court_list: list = court_info.info_courts.all()
        # court_info = CourtInfoForm(prefix='court-info', instance=court_info)
        print('Случай информации о деле существует', )
    else:
        court_list: list = []
        Court_ifno = CourtInfoForm(prefix='court-info', instance=court_info)
        # court_info = CourtInfoForm(prefix='court-info', instance=court_info)
        # court_info = CourtInfoForm(prefix='court-info', instance=court_info)
        # court = CourtForm(instance=Court, prefix='court')
        error = 'Операции по  судопроизводсту нет'
        print('Случай есть информация о деле, список операций  по делу пустой', )

    if request.method == 'POST':
        form = CourtForm(request.POST, request.FILES)
        if form.is_valid():
            print('До', form.cleaned_data)
            court = form.save(commit=False)
            court.info_court = court_info
            court.save()
            return redirect('/court/court-event-add/%d/' % pk)
        else:
            return print('Ваша форма заполнена не првильно')
    CourtForms = CourtForm()
    court_info = CourtInfoAddForm(instance=court_info)
    template_name = 'dist/court/event/read_court_add_event.html'
    data = {'court_info': court_info,
            'court': CourtForms,
            'court_list': court_list,
            'accident_pk': accident_pk
            }

    return render(request, template_name, data)


def court_info_edit(request, pk):
    """Редактирование информации о судебном процессе"""
    accident = Accident.objects.get(id=pk)
    accident_pk = accident.pk
    court_info = InfoCourt.objects.get(id =accident.court_info.pk)


    if request.method == 'POST':
        form = CourtInfoForm(request.POST, request.FILES, instance=court_info)
        if form.is_valid():
            form.save()
            return redirect('/court/court-event-add/%d/' % pk)

    form =CourtInfoForm(instance=court_info)
    data = {
        'accident_pk': accident_pk,
        'court_info': form,
            }
    template_name = 'dist/court/info/edit_form.html'
    return render(request, template_name, data)


# def court_new_pk(request, pk):
#     """Создание добавление нового судопрозводства к ДТП"""
#
#     accident = Accident.objects.get(id=pk)
#     accident_pk = accident.pk
#     court_info = accident.court_info
#     # court_info_id = accident.court_info.pk
#     # print(court_info_id)
#
#     # court_info1 = get_object_or_404(Court, id=accident.court_info.pk)
#     # print(court_info1)
#     court_list: list = []
#     # court:list = []
#     if court_info is not None:
#         print(court_info, 'инфо о деле')
#         court_list: list = court_info.info_courts.all()
#         # court_info = CourtInfoForm(prefix='court-info', instance=court_info)
#         print('Случай информации о деле существует', )
#     else:
#         court_list: list = []
#         # court_info = CourtInfoForm(prefix='court-info', instance=court_info)
#         # court_info = CourtInfoForm(prefix='court-info', instance=court_info)
#         # court = CourtForm(instance=Court, prefix='court')
#         error = 'Операции по  судопроизводсту нет'
#         print('Случай есть информация о деле, список операций  по делу пустой', )
#     if request.method == 'POST':
#         courtinfoForm = CourtInfoForm(request.POST, request.FILES, prefix='court-info', instance=court_info)
#         if courtinfoForm.is_valid():
#             inst = courtinfoForm.save(commit=False)
#             inst.save()
#             accident.courtinfoForm = inst
#             accident.save()
#             print(' Форма заполнена успешно и сохранена с привязкой к ДТП', accident.pk)
#             return redirect('/court/court-event-add/%d/' % accident_pk)
#         else:
#             error = 'Форма не верно заполнена'
#
#     courtinfoForm = CourtInfoForm(prefix='court-info', instance=court_info)
#     template_name = 'dist/court/new_pk.html'
#     # template_name = 'dist/court/event/modal_event.html'
#     data = {
#         # 'error': error,
#         'accident_pk': accident_pk,
#         'court_info': courtinfoForm,
#         'court_list': court_list,
#
#     }
#     return render(request, template_name, data)


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
        courtinfo = CourtInfoForm(request.POST, request.FILES, prefix='court-info')
        if courtinfo.is_valid():
            inst = courtinfo.save(commit=False)
            inst.save()
            accident.court_info = inst
            accident.save()
            print(' Форма заполнена успешно и сохранена с привязкой к ДТП', inst.pk)
            return redirect('/court/court-event-add/%d/' % pk)
        else:
            error = 'Форма не верно заполнена'

    # court_info = CourtInfoForm(prefix='court-info', instance=court_info)
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
