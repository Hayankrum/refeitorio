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

    path('new/',views.new, name='new'),
    path('lista/', views.lista, name='lista'),
    path('editar/<str:id>', views.editar, name='editar'),
    path('excluir/<str:id>', views.excluir, name='excluir'),

    re_path(r'^img/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
