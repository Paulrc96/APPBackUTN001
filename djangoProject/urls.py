from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter, url
from product.views import ProductViewSet, ProductViewSetMarca, ProductViewSetNacionalidad

router = DefaultRouter()
router.register(r'productos', ProductViewSet)


urlpatterns = router.urls

urlpatterns += [
    path('admin/', admin.site.urls),
    url(r'^productos/marca/(?P<marca>\w+)$', ProductViewSetMarca.as_view(), name='producto'),
    url(r'^productos/nacionalidad/(?P<nacionalidad>\w+)$', ProductViewSetNacionalidad.as_view(), name='nacionalidad')
]
