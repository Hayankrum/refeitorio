from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve

from siteapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('userapp.urls')),
    path('',include('userapp.urls')),

    path('',views.new, name='new'),
    path('lista/', views.lista, name='lista'),
    path('editar/<str:id>', views.editar, name='editar'),
    path('excluir/<str:id>', views.excluir, name='excluir'),


    path('ev_new/',views.ev_new, name='ev_new'),
    path('ev_lista/', views.ev_lista, name='ev_lista'),
    path('ev_editar/<int:id_evento>/', views.ev_editar, name='ev_editar'),  # URL para editar evento
    path('ev_excluir/<int:id_evento>/', views.ev_excluir, name='ev_excluir'),  # URL para excluir evento

    re_path(r'^img/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
