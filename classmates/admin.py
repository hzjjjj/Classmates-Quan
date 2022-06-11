from django.contrib import admin
from classmates.models import Quan

# Register your models here.
class QuanAdmin(admin.ModelAdmin):
    exclude = ('quan_star','quan_read','quan_creator',)
    list_display = ('quan_title','quan_creator','quan_type','quan_tag','quan_star','quan_read','quan_created_date',)

    def save_model(self, request, obj, form, change):
        obj.quan_creator = request.user
        super().save_model(request,obj,form,change)

admin.site.register(Quan, QuanAdmin)
