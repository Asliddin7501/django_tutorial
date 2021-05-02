from django.contrib import admin
from .models import Telefon

class TelefonAdmin(admin.ModelAdmin):
    class Meta:
        model = Telefon

admin.site.register(Telefon, TelefonAdmin)