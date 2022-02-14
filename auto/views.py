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
    return render(request, 'dist/auto-list.html', {'results': auto})




def auto_new(request):
    template_name = 'dist/auto-files.html'
    if request.method == 'GET':
        autoform = AutoForm(request.GET or None)
        formset = FileFormset(queryset=File.objects.none())
    elif request.method == 'POST':
        autoform = AutoForm(request.POST)
        formset = FileFormset(request.POST, request.FILES)

        if autoform.is_valid() and formset.is_valid():
            auto = autoform.save()
            for form in formset:
                file = form.save(commit=False)
                file.files = auto
                file.save()
            return redirect('/auto/')
        else:
            print('You have error')
    return render(request, template_name, {
        'autoform': autoform,
        'formset': formset,
    })


def edit_auto_new(request, pk):
    template_name = 'dist/auto-files.html'
    auto = Car.objects.get(id=pk)
    if request.method == 'GET':

        autoform = AutoForm(instance=auto)
        print('Yo', auto)
        # formset = FileFormset(queryset=File.objects.none())
    elif request.method == 'POST':
        autoform = AutoForm(request.POST, instance=auto)
        formset = FileFormset(request.POST, request.FILES)

        if autoform.is_valid() and formset.is_valid():
            auto = autoform.save()
            for form in formset:
                file = form.save(commit=False)
                file.files = auto
                file.save()
                return redirect('/auto/')
        else:
            print('You have error')
    return render(request, template_name, {
        'autoform': autoform,
        'formset': formset,
    })


def auto_edit(request, pk):
    """Редактирования  данных ТС"""

    auto = get_object_or_404(Car, pk=pk)
    if request.method == "POST":
        form = AutoForm(request.POST, instance=auto)
        if form.is_valid():
            auto = form.save(commit=False)
            auto.save()
            p = form.cleaned_data
            print(p)
            return redirect('/auto/')
    else:
        form = AutoForm(instance=auto)
        template_name = 'dist/auto-edit.html'
        data = {
            'form': form,
        }
    return render(request, template_name, data)
