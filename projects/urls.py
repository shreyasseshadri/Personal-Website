from django.conf.urls import url
from projects import views

urlpatterns = [
    url(r'^$', views.index, name='project_index'),
]
