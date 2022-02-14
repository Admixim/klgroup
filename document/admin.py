from django.contrib import admin
from document.models import Document, Body_doc,Document_tags,Table


@admin.register(Body_doc)
class Body_docAdmin(admin.ModelAdmin):
    """Таблица обектов документа """

    list_display = [
        "id",
        "name",
        "text",
        "document",
        "is_active",
        "updated",
        "created"]
    list_display_links = ("name",)
    search_fields = ("name",)


class InBody(admin.StackedInline):
    model = Body_doc


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    """Таблица Документов """

    list_display = [
        "id",
        "name",
        "executor",
        "comment",
        "location",
        "author",
        "customer",
        "is_active",
        "updated",
        "created"]
    list_display_links = ("id", "name")
    save_on_top = True
    extra = 0
    search_fields = ("id", "name",)
    inlines = [
        InBody
    ]
@admin.register(Document_tags)
class Document_tagsAdmin(admin.ModelAdmin):
    """Таблица обектов документа """

    list_display = [
        "id",
        ('table'),
        "name",
        "tags",
        "model",
        "comment",
        "is_active",
        "updated",
        "created"
    ]
    list_display_links = ("name",)
    search_fields = ("name",)


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    """Таблица имени модели """

    list_display = [
        "id",
        "name",
        "comment",
        "is_active",
        "updated",
        "created"]
    list_display_links = ("name",)
    search_fields = ("name",)
