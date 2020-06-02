from django.conf.urls import url

from .views import hi, vid

urlpatterns = [
    url(r'^style/$', hi),
    url(r'^vidplayer/$', vid, name="vid_player"),

 ]