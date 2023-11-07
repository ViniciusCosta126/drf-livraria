from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from livraria.views import CategoriaViewSet, AutorViewSet, LivroViewSet

router = routers.DefaultRouter()
router.register('categorias', CategoriaViewSet)
router.register('autores', AutorViewSet)
router.register('livros', LivroViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls))
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
