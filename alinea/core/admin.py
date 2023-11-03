from django.contrib import admin
from .models import CaruselLanding, Contact

# Register your models here.
class LandingAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    readonly_fields = ('width', 'height', 'order', 'created', 'updated')

admin.site.register(CaruselLanding, LandingAdmin)

class ContactAdmin(admin.ModelAdmin):
    readonly_fields = ('name', 'mail', 'phone', 'message', 'created')
    list_filter = ('created', 'status')
    list_display = ('name', 'status')

admin.site.register(Contact, ContactAdmin)