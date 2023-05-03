
from django.urls import path
from  .import views
app_name='docapp'
urlpatterns = [
    path('',views.index,name='index'),
    path('document/<int:document_id>/',views.detail,name='detail'),
    path('add/',views.add_document,name='add_document'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')


]