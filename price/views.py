# coding: utf-8
from django.shortcuts import render,redirect, get_object_or_404
from price.models import *
from price.forms import *
# from .forms import PriceForm, Assignment_pay


# Список услуг прайса  общий
def price_list(request):
    price = models.Price.objects.all()
    return render(request, 'dist/price/price-list.html', {'results': price})



def price_court_cash(request):
    error = ''
    template_name = 'dist/price/price-court-cash-accident.html'
    return render(request, template_name)

# Создание-добавление  новой услуги в прайс
def price_new(request):
    error = ''
    if request.method == 'POST':
        form =PriceForm(request.POST, prefix='test')

        if form.is_valid():
            print(form.cleaned_data)
            form = form.save(commit=False)
            form.save()
            return  redirect('/price/')
        else:
            error = ' Форма не верно заполнена'

    form = PriceForm(prefix='test')
    data = {'form':form,
            'error':error
            }
    template_name = 'dist/price-new.html'
    return render(request, template_name,data)

# Редактирования  данных услуги прайса
def price_edit(request, pk):
    client = get_object_or_404(models.Price, pk=pk)
    if request.method == "POST":
        form = PriceForm(request.POST, instance=price)
        if form.is_valid():
            # _date = form.cleaned_data['date_birth']
            # print(_date)
            client =form.save(commit=False)
            client.save()
            return redirect('/price/')

    else:
        form = PriceForm(instance=price)
        template_name = 'dist/contacts-edit.html'
    return render(request, template_name, {'form': form, 'price': pk})

# Список платежей по цессиям  общий
def assignment_pay_list(request):
    clients = models.Bank_pay.objects.all()
    return render(request, 'dist/assignment_pay.html', {'results': assignment_pay})


# Создание-добавление  входящего платежного документа цессии
def assignment_pay(request):
    error = ''
    if request.method == 'POST':
        form =Assignment_payForm(request.POST, prefix='test')

        if form.is_valid():
            print(form.cleaned_data)
            form = form.save(commit=False)
            form.save()
            return  redirect('/assignment_pay/')
        else:
            error = ' Форма не верно заполнена'

    form = PriceForm(prefix='test')
    data = {'form':form,
            'error':error
            }
    template_name = 'dist/assignment_pay.html'
    return render(request, template_name,data)

# Редактирования  данных входящего платежного документа цессии
def assignment_pay_edit(request, pk):
    client = get_object_or_404(models.Price, pk=pk)
    if request.method == "POST":
        form = Assignment_payForm(request.POST, instance=assignment_pay)
        if form.is_valid():
            # _date = form.cleaned_data['date_birth']
            # print(_date)
            client =form.save(commit=False)
            client.save()
            return redirect('/assignment_pay/')

    else:
        form = Assignment_payForm(instance=assignment_pay)
        template_name = 'dist/assignment_pay-edit.html'
    return render(request, template_name, {'form': form, 'assignment_pay': pk})

