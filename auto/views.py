from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from auto.forms import *
from auto.models import *


def auto_list(request):
    # Список ТС общий

    auto = Car.objects.all()
    # q = request.GET.get('find')
    # if q:
    #     auto = models.Car.objects.filter(number=q)
    return render(request, 'dist/handbk/auto/auto-list.html', {'results': auto})

def auto_model(request):

    get_brend = get_object_or_404(Brend, pk=2)

    print('Нужные модель', get_brend.id, get_brend)
    get_model = get_brend.brand_model.all()
    for q in get_brend.brand_model.all():
        print(q)
    print(get_model)
    context_data = {'get_model': get_model}
    print(context_data)
    return  JsonResponse(context_data)


def auto_new(request):
    """Создание-добавление  нового  ТС """

    if request.method == 'POST':
        autoform = AutoForm(request.POST, prefix=Car)
        formset = FileAutoFormset(request.POST, request.FILES, prefix=AutoFiles)
        insurance = InsuranceAutoFormset(request.POST, request.FILES, prefix=Insurance)
        if autoform.is_valid() and formset.is_valid() and insurance.is_valid():
            auto = autoform.save()
            for form in formset:
                file = form.save(commit=False)
                if file.scan_doc:
                    file.files = auto
                    file.save()
            for doc in insurance:
                item = doc.save(commit=False)
                item.car = auto
                item.save()
                return redirect('/auto/')

    template_name = 'dist/handbk/auto/auto-new.html'
    autoform = AutoForm(prefix=Car)
    formset = FileAutoFormset(queryset=AutoFiles.objects.none(), prefix=AutoFiles)
    insurance = InsuranceAutoFormset(queryset=Insurance.objects.none(), prefix=Insurance)
    return render(request, template_name, {
            'autoform': autoform,
            'formset': formset,
            'insurance': insurance,
        })




def auto_edit(request, pk):
    """Редактирования  данных ТС"""

    auto = get_object_or_404(Car, pk=pk)
    formset = FileAutoFormset(queryset=AutoFiles.objects.none())
    if request.method == "POST":
        autoform = AutoForm(request.POST, instance=auto, )
        formset = FileAutoFormset(request.POST, request.FILES, )
        print(formset)
        if autoform.is_valid() and formset.is_valid():
            auto = autoform.save()
            for form in formset:
                instance = form.save(commit=False)
                if instance.scan_doc:
                    instance.files = auto
                    print('Instance', instance)
                    print('auto', auto)
                    instance.save()
        return redirect('auto-list')
    else:
        autoform = AutoForm(instance=auto)
        list_files = auto.files_auto.all()
        template_name = 'dist/handbk/auto/auto-edit.html'
        data = {
                'autoform': autoform,
                'formset': formset,
                'list_files': list_files,
                'auto': pk,
            }
        return render(request, template_name, data)



def edit_auto_new(request, pk):
    template_name = 'dist/handbk/auto/auto-files.html'
    auto = Car.objects.get(id=pk)
    formset = FileAutoFormset(queryset=AutoFiles.objects.none())
    if request.method == 'GET':
        autoform = AutoForm(instance=auto)
        print('Yo', auto)
        formset = FileAutoFormset(queryset=AutoFiles.objects.none())
    elif request.method == 'POST':
        autoform = AutoForm(request.POST, instance=auto)
        formset = FileAutoFormset(request.POST, request.FILES)

        if autoform.is_valid() and formset.is_valid():
            auto = autoform.save()
            for form in formset.is_bound:
                file = form.save(commit=False)
                if file.scan_doc:
                    file.files = auto
                    file.save()
            return redirect('/auto/')

    else:
        print('Упала из за ошибки')
        autoform = AutoForm(instance=auto)
        list_files = auto.files_auto.all()
        data = {
            'autoform': autoform,
            'formset': formset,
            'list_files': list_files,
            'auto': pk,
        }
        return render(request, template_name, data)




