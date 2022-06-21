from django.contrib import admin
from . import models
from .services import set_property
# Register your models here.

class BooksAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'listed_by',
        'status',
    )

    def save_model(self, request, obj, form, change):
        obj = set_property(request, obj)
        return super().save_model(request, obj, form, change)

admin.site.register(models.Books, BooksAdmin)