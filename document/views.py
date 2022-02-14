# coding: utf-8
import shutil
import os
import time
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from io import BytesIO

from xhtml2pdf import pisa

from client.models import *
from .models import Document, Body_doc
# from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse, FileResponse
import uuid
from client.forms import ClientForm


def context(client_id, document_id):
    """Функция для добавления в шаблон данных из модели клиента,документа, тело документа"""

    document = Document.objects.get(id=document_id)
    client = Client.objects.get(id=client_id)
    body_doc = Body_doc.objects.filter(document=document).order_by('id')

    data = {'document': document,
            'client': client,
            'body_doc': {k: block for k, block in enumerate(body_doc)}}

    return data


def pdf_contract(request, client_id):
    """Создание  pdf договора  с клиентом и записи его в папку"""

    client = Client.objects.get(id=client_id)
    form = ClientForm(request.POST, instance=client)
    print(request.method)
    template_path = 'doc_pdf/contract.html'
    document = Document.objects.get(id=1)
    print(form)
    if form.is_valid():
        print(form.cleaned_data)
        client = form.save(commit=False)
        client.save()
    else:
        print("У меня куча ошибок, наверное)))")

    context = {
        'client': Client.objects.get(id=client_id),
        'document': document
    }
    template = get_template(template_path)
    html = template.render(context)

    # создание имени  для pdf файла
    time_string = time.strftime("%m-%d-%Y_")
    type_doc = 'contract_'
    name = uuid.uuid4()
    # создание pdf файла
    _file = open(f'{settings.MEDIA_ROOT}/pdf_doc/{type_doc}{time_string}{name}.pdf', 'wb')
    pisa_status = pisa.CreatePDF(html.encode('UTF-8'), encoding='UTF-8', dest=_file)
    _file.close()
    return FileResponse(open(f'{settings.MEDIA_ROOT}/pdf_doc/{type_doc}{time_string}{name}.pdf', 'rb'),
                        as_attachment=True)


def pdf_contract_one(request, client_id):
    """функция создание pdf файла и записи его в бд Договор юридических услуг первичный"""

    client = Client.objects.get(id=client_id)
    form = ClientForm(request.POST, instance=client)
    if form.is_valid():
        client = form.save(commit=False)
        client.save()

    document = Document.objects.get(id=1)
    template_path = 'doc_pdf/contract_one.html'

    context = {
        'client': client,
        'document': document
    }
    template = get_template(template_path)
    html = template.render(context)
    time_string = time.strftime("%m-%d-%Y_")
    name = uuid.uuid4()
    type_doc = 'contract_one_'
    _file = open(f"{settings.MEDIA_ROOT}/pdf_doc/{type_doc}{time_string}{name}.pdf", 'wb')
    pisa_status = pisa.CreatePDF(html.encode('UTF-8'), encoding='UTF-8', dest=_file)
    _file.close()
    return FileResponse(open(f'{settings.MEDIA_ROOT}/pdf_doc/{type_doc}{time_string}{name}.pdf', 'rb'),
                        as_attachment=True)


def pdf_contract_one_add(request, client_id):
    """Функция создание pdf файла и записи его в бд Дополнительное соглашение к договору"""

    client = Client.objects.get(id=client_id)
    form = ClientForm(request.POST, instance=client)
    if form.is_valid():
        client = form.save(commit=False)
        client.save()
    document = Document.objects.get(id=1)
    template_path = 'doc_pdf/contract_one_add.html'

    context = {
        'client': client,
        'document': document
    }
    template = get_template(template_path)
    html = template.render(context)
    time_string = time.strftime("%m-%d-%Y_")
    type_doc = 'contract_one_add_'
    name = uuid.uuid4()
    _file = open(f"{settings.MEDIA_ROOT}/pdf_doc/{type_doc}{time_string}{name}.pdf", 'wb')
    pisa_status = pisa.CreatePDF(html.encode('UTF-8'), encoding='UTF-8', dest=_file)
    _file.close()
    return FileResponse(open(f'{settings.MEDIA_ROOT}/pdf_doc/{type_doc}{time_string}{name}.pdf', 'rb'),
                        as_attachment=True)


def pdf_assignment(request, client_id):
    """Созадние договора Цессии с клиентом"""

    client = Client.objects.get(id=client_id)
    form = ClientForm(request.POST, instance=client)
    if form.is_valid():
        client = form.save(commit=False)
        client.save()
    document = Document.objects.get(id=1)
    template_path = 'doc_pdf/assignment.html'
    context = {
        'client': client,
        'document': document
    }
    template = get_template(template_path)
    html = template.render(context)
    time_string = time.strftime("%m-%d-%Y_")
    type_doc = 'assignment_'
    name = uuid.uuid4()
    # создание pdf файла
    _file = open(f"{settings.MEDIA_ROOT}/pdf_doc/{type_doc}{time_string}{name}.pdf", 'wb')
    pisa_status = pisa.CreatePDF(html.encode('UTF-8'), encoding='UTF-8', dest=_file)
    _file.close()
    return FileResponse(open(f'{settings.MEDIA_ROOT}/pdf_doc/{type_doc}{time_string}{name}.pdf',
                             'rb'),
                        as_attachment=True)


def pdf_assignment_add(request, client_id):
    """Функция создание pdf файла и записи его в бд  Дополнительное соглашение к договору цесссии"""

    client = Client.objects.get(id=client_id)
    form = ClientForm(request.POST, instance=client)
    if form.is_valid():
        client = form.save(commit=False)
        client.save()
    document = Document.objects.get(id=2)
    template_path = 'doc_pdf/assignment _add.html'
    context = {
        'client': client,
        'document': document
    }
    template = get_template(template_path)
    html = template.render(context)
    result = BytesIO()
    time_string = time.strftime("%m-%d-%Y_")
    type_doc = 'assignment_add'
    name = uuid.uuid4()
    _file = open(f"{settings.MEDIA_ROOT}/pdf_doc/{type_doc}{time_string}{name}.pdf", 'wb')
    pisa_status = pisa.CreatePDF(html.encode('UTF-8'), encoding='UTF-8', dest=_file)
    _file.close()
    return FileResponse(open(f'{settings.MEDIA_ROOT}/pdf_doc/{type_doc}{time_string}{name}.pdf', 'rb'),
                        as_attachment=True)


def pdf_contract_expert(request, client_id):
    """Функция создание pdf файла и записи его в бд  Договор экспертизы точная оценка"""

    form = ClientForm(request.POST)
    if form.is_valid():
        client = form.save(commit=False)
        client.save()
    document = Document.objects.get(id=2)
    template_path = 'doc_pdf/contract_expert.html'

    context = {
        'client': client,
        'document': document
    }

    template = get_template(template_path)
    html = template.render(context)
    # создание имени  для pdf файла
    time_string = time.strftime("%m-%d-%Y_")
    type_doc = 'contract_expert'
    name = uuid.uuid4()
    # создание pdf файла
    _file = open(f"{settings.MEDIA_ROOT}/pdf_doc/{type_doc}{time_string}{name}.pdf", 'wb')
    pisa_status = pisa.CreatePDF(html.encode('UTF-8'), encoding='UTF-8', dest=_file)
    _file.close()
    return FileResponse(open(f'{settings.MEDIA_ROOT}/pdf_doc/{type_doc}{time_string}{name}.pdf', 'rb'),
                        as_attachment=True)


def pdf_contract_arbit(request, client_id):
    """Функция создание pdf файла и записи его в бд   Договор арбитражный суд"""

    form = ClientForm(request.POST, )
    if form.is_valid():
        client = form.save(commit=False)
        client.save()

    document = Document.objects.get(id=2)
    template_path = 'doc_pdf/contract_one_arbit.html'

    context = {
        'client': client,
        'document': document
    }

    template = get_template(template_path)
    html = template.render(context)
    time_string = time.strftime("%m-%d-%Y_")
    type_doc = 'contract_arbit'
    name = uuid.uuid4()
    _file = open(f"{settings.MEDIA_ROOT}/pdf_doc/{type_doc}{time_string}{name}.pdf", 'wb')
    pisa_status = pisa.CreatePDF(html.encode('UTF-8'), encoding='UTF-8', dest=_file)
    _file.close()
    return FileResponse(open(f'{settings.MEDIA_ROOT}/pdf_doc/{type_doc}{time_string}{name}.pdf', 'rb'),
                        as_attachment=True)
