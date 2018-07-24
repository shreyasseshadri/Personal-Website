from django.conf.urls import url
from about import views


urlpatterns = [
    url(r'^$',views.index,name="index"),
    url(r'$', views.pdf_view, name='project_index'),
]
