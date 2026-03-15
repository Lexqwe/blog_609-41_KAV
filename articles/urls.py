from django.urls import  path

from articles import views

app_name = 'articles'

urlpatterns = [
    path('', views.article_list, name='list'),
    path('form', views.article_form, name='form'),
    path('<slug:slug>', views.article_item, name='article_detail'),
    path('update/<slug:slug>', views.article_update, name='update'),
    path('delete/<slug:slug>', views.article_delete, name='delete'),
]