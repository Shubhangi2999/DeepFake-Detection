from django.utils.translation import ugettext_lazy
from django.contrib.admin import AdminSite
from django.contrib import admin
from  .models import Video

# Register your models here.

@admin.register(Video)
class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'videofile')

AdminSite.site_header = ugettext_lazy('My Administration')

AdminSite.site_title = ugettext_lazy('My Admin')

AdminSite.index_title = ugettext_lazy('VIDEO PLAYER')
