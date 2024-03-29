from django.shortcuts import render, redirect, get_object_or_404

from client.models import Partner
from .models import *
from accident.models import Accident
from .forms import ExpertForm, ExpertNewForm, ExpertFiles,  FileExpertFormset
from client.forms import PartnerForm


def expert_list(request):
    expert_list = Expert.objects.all()
    return render(request, 'dist/expert/list.html', {'results': expert_list})


def expert_modal_new(request):
    """Создание-добавление  новой экспертизы в модальном окне Образец"""
    error = ''
    if request.method == 'POST':
        form = ExpertForm(request.POST, request.FILES or None, )
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
    template_name = 'dist/expert/modal_event.html'
    return render(request, template_name, data)


def expert_new(request):
    """Создание-добавление  новой экспертизы без привязки к ДТП"""

    if request.method == 'POST':
        expertform = ExpertNewForm(request.POST, prefix=Expert)
        formset = FileExpertFormset(request.POST, request.FILES,)
        if expertform.is_valid() and formset.is_valid():
            expert = expertform.save()
            for form in formset:
                file = form.save(commit=False)
                if file.scan_doc:
                    file.files = expert
                    file.save()
            return redirect('/expert/edit/%s'%expert.pk)
    else:
        expertform = ExpertNewForm(prefix=Expert)
        formset = FileExpertFormset(queryset=ExpertFiles.objects.none(),)
        template_name = 'dist/expert/new.html'
        data = {'expert': expertform,
                'formset': formset,
           }
        return render(request, template_name, data)


def expert_new_pk(request, pk):
    """Создание-добавление  новой экспертизы к ДТП"""
    accident = get_object_or_404(Accident, id=pk)
    accident_pk = accident.id
    expert_list = accident.expert_accident.all()
    court = accident.court_info
    formset = FileExpertFormset(queryset=ExpertFiles.objects.none(), )
    print(formset)
    partner = Partner.objects.filter(accident_id=pk, type='True').first()
    if request.method == 'POST':
        expertform = ExpertForm(request.POST, request.FILES, prefix=Expert)
        formset = FileExpertFormset(request.POST, request.FILES,)
        if expertform.is_valid() and formset.is_valid():
            inst = expertform.save(commit=False)
            inst.accident_id = pk
            inst.client_id = partner.client_id
            inst.car_id = partner.car_id
            inst.save()
            for form in formset:
                file = form.save(commit=False)
                if file.scan_doc:
                    file.files = inst
                    file.save()
            return redirect('/expert/expert-new-pk/%d/' % accident_pk)
    else:
        error = ' Форма не верно заполнена'
        expert = ExpertForm(prefix=Expert)
        template_name = 'dist/expert/new_pk.html'

        data = {
            'expert': expert,
            'error': error,
            'accident': accident,
            'accident_pk': accident_pk,
            'expert_list': expert_list,
            'client': partner,
            'court': court,
            'formset': formset,
        }
        return render(request, template_name, data)


class MyException(Exception):
   pass


def expert_edit(request, pk):
    """Редактирования  данных экспертизы"""

    expert = get_object_or_404(Expert, pk=pk)
    formset = FileExpertFormset(queryset=ExpertFiles.objects.none(), )
    if request.method == "POST":
        expert_form = ExpertNewForm(request.POST,  instance=expert, prefix=Expert)
        formset = FileExpertFormset(request.POST, request.FILES, prefix=None)
        if expert_form.is_valid() and formset.is_valid():
            expert = expert_form.save()
            for form in formset:
                inst = form.save(commit=False)
                if inst.scan_doc:
                    inst.files = expert
                    print(inst)
                    inst.save()
        return redirect('/expert/edit/%s'%expert.pk)
    else:
        error = ' Форма не верно заполнена'
        expert_form = ExpertNewForm(instance=expert, prefix=Expert)
        list_files = expert.files_expert.all()
        template_name = 'dist/expert/edit.html'
        data = {'expert_edit': expert_form,
                    'list_files': list_files,
                    'pk': pk,
                    'formset': formset,
                    'error': error
                }
        return render(request, template_name, data)


