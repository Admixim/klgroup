from django.shortcuts import render,redirect, get_object_or_404

from client.models import Partner
from .models import *
from accident.models import Accident
from .forms import ExpertForm, ExpertNewForm
from client.forms import PartnerForm


def expert_list(request):
    expert_list = Expert.objects.all()
    return render(request, 'dist/expert/list.html', {'results': expert_list})

def expert_modal_new(request):
    """Создание-добавление  новой экспертизы в модальном окне"""
    error = ''
    if request.method == 'POST':
        form = ExpertForm(request.POST,request.FILES or None,)
        if form.is_valid():
            print(form.cleaned_data)
            form = form.save(commit=False)
            form.save()
            return redirect('/expert/')
        else:
            error = ' Форма не верно заполнена'

    form = ExpertForm()
    data = {'form': form,
            'error': error
            }
    template_name = 'dist/expert/modal_new.html'
    return render(request, template_name,data)

def expert_new(request):
    """Создание-добавление  новой экспертизы без привязки к ДТП"""

    template_name = 'dist/expert/new.html'
    error = ''
    if request.method == 'POST':
        expert = ExpertNewForm(request.POST, request.FILES or None, )
        if expert.is_valid():
            expert.save()

            return  redirect('/expert/')
    else:
        error = ' Форма не верно заполнена'
        expert = ExpertNewForm()
        data = {'expert':expert,
            'error':error
            }

    return render(request, template_name,data)


def expert_new_pk(request, pk):
    """Создание-добавление  новой экспертизы к ДТП"""

    error = ''
    if request.method == 'POST':
        form =ExpertForm(request.POST, request.FILES)

        if form.is_valid():
            print(form.cleaned_data)
            inst = form.save(commit=False)

            inst.accident_id = pk
            inst.save()
            return  redirect('/expert/expert-new-pk/%d/' % pk)
        else:
            error = ' Форма не верно заполнена'
    expert_list = Expert.objects.filter(accident_id=pk)
    client = Partner.objects.filter(accident_id=pk, type='True').first()

    accident_pk =Accident.objects.get(pk=pk)
    expert = ExpertForm()
    template_name = 'dist/expert/new_pk.html'
    data = {'expert':expert,
            'error':error,
            'accident_pk':accident_pk,
            'expert_list':expert_list,
            'client':client,
            'pk':pk
            }


    return render(request, template_name,data)



def expert_edit(request, pk):
    """Редактирования  данных экспертизы"""

    expert = get_object_or_404(Expert, pk=pk)
    if request.method == "POST":
        expert_edit_form = ExpertNewForm(request.POST, request.FILES, instance=expert)
        if expert_edit_form.is_valid():
            inst = expert_edit_form.save(commit=False)
            inst.id = pk
            inst.save()
            print(pk)
            return redirect('/expert/edit/%d/' % (inst.id) )

        else:
            error = ' Форма не верно заполнена'
    expert_edit_form = ExpertNewForm(instance=expert)
    template_name = 'dist/expert/edit.html'
    return render(request, template_name, {'expert_edit': expert_edit_form,
                                           'pk':pk
                                           }
                  )


