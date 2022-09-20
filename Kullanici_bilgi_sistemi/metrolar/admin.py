from django.contrib import admin
from metrolar.models import Metro
# Register your models here.

@admin.register(Metro) #Makale
class MetroAdmin(admin.ModelAdmin):
    list_display = ('id','Description','LineName','BabyRoom','WC','Masjid',)
    list_filter = ('WC','BabyRoom','Masjid', 'LineName')
    search_fields = ('Description','LineName' )
    search_help_text=('Search by; Description and or LineName')


