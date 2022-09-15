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
        formset = FileExpertFormset(request.POST, request.FILES, prefix=ExpertFiles)
        if expertform.is_valid() and formset.is_valid():
            expert = expertform.save()
            print('Expert', expert)
            for form in formset:
                file = form.save(commit=False)
                print('files-1',file.files)
                if file.scan_doc:
                    print('scandoc1', file.scan_doc)
                    print('files2', file)
                    file.files = expert
                    file.save()
        return redirect('/expert/')
    else:
        expertform = ExpertNewForm(prefix=Expert)
        formset = FileExpertFormset(queryset=ExpertFiles.objects.none(), prefix=ExpertFiles)
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
    error = ''
    partner = Partner.objects.filter(accident_id=pk, type='True').first()
    if request.method == 'POST':
        form = ExpertForm(request.POST, request.FILES)
        if form.is_valid():
            inst = form.save(commit=False)
            inst.accident_id = pk
            inst.client_id = partner.client_id
            inst.car_id = partner.car_id
            inst.save()
            return redirect('/expert/expert-new-pk/%d/' % pk)
        else:
            error = ' Форма не верно заполнена'
    expert = ExpertForm()

    template_name = 'dist/expert/new_pk.html'
    data = {
            'expert': expert,
            'error': error,
            'accident': accident,
            'accident_pk': accident_pk,
            'expert_list': expert_list,
            'client': partner,
            'court': court,
            }
    return render(request, template_name, data)


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
                                           'pk': pk
                                           }
                  )


