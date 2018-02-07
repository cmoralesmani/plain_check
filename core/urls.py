from django.conf.urls import url, include

from . import views as core_views

app_name = 'core'

urlpatterns = [
    url(
        r'^$',
        core_views.index,
        name='index'
    )
]
