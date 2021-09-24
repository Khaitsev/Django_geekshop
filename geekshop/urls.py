from django.contrib import admin
from django.urls import path, include
from mainapp import views as mainapp
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('mainapp.urls', namespace='products')),
    path('contact/', mainapp.contact, name='contact'),
    path('', mainapp.main, name='main'),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('baskets/', include('basketapp.urls', namespace='baskets')),
    path('admin-staff/', include('adminapp.urls', namespace='admin_staff')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)