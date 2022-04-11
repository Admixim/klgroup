from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *

from django.forms.forms import *
from django.forms import modelformset_factory


def auto_list(request):
    # Список ТС общий

    auto = Car.objects.all()
    # q = request.GET.get('find')
    # if q:
    #     auto = models.Car.objects.filter(number=q)
    return render(request, 'dist/handbk/auto/auto-list.html', {'results': auto})




def auto_new(request):
    """Создание-добавление  нового  ТС """

    if request.method == 'POST':
        autoform = AutoForm(request.POST, prefix=Car)
        formset = FileAutoFormset(request.POST, request.FILES, prefix=AutoFiles)
        if autoform.is_valid() and formset.is_valid():
            auto = autoform.save()
            for form in formset:
                file = form.save(commit=False)
                file.files = auto
                file.save()
            return redirect('/auto/')
    else:
        template_name = 'dist/handbk/auto/auto-new.html'
        autoform = AutoForm(prefix=Car)
        formset = FileAutoFormset(queryset=AutoFiles.objects.none(), prefix=AutoFiles)
        return render(request, template_name, {
            'autoform': autoform,
            'formset': formset,
        })


def auto_edit(request, pk):
    """Редактирования  данных ТС"""

    auto = get_object_or_404(Car, pk=pk)
    formset = FileAutoFormset(queryset=AutoFiles.objects.none())
    if request.method == "POST":
        autoform = AutoForm(request.POST, instance=auto)
        formset = FileAutoFormset(request.POST, request.FILES, prefix=None)
        if autoform.is_valid() and formset.is_valid():
            auto = autoform.save()
            for form in formset:
                instance = form.save(commit=False)
                instance.files = auto
                instance.save()
            return redirect('/auto/')
    else:
        autoform = AutoForm(instance=auto)
        list_files = auto.files_auto.all()
        print(list_files)
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
    if request.method == 'GET':
        autoform = AutoForm(instance=auto)
        print('Yo', auto)
        # formset = FileFormset(queryset=File.objects.none())
    elif request.method == 'POST':
        autoform = AutoForm(request.POST, instance=auto)
        formset = FileAutoFormset(request.POST, request.FILES)

        if autoform.is_valid() and formset.is_valid():
            auto = autoform.save()
            for form in formset.is_bound:
                file = form.save(commit=False)
                file.files = auto
                file.save()
                return redirect('/auto/')

        else:
            print('Упала из за ошибки')
    return render(request, template_name, {
        'autoform': autoform,
        'formset': formset,
    })



