from django.contrib import admin
from .models import CsvFile, Image, Client

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name',)

class CsvFileAdmin(admin.ModelAdmin):
    list_display = ('url', 'client', 'uploaded', 'activate')

class ImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'title', 'description', 'client', 'created')

admin.site.register(CsvFile, CsvFileAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Client, ClientAdmin)
