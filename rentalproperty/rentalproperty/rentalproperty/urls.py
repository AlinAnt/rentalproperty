
from django.urls import include
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
]

urlpatterns += [
    path('catalog/', include('catalog.urls')),
]

urlpatterns += [
    path('', RedirectView.as_view(url='/catalog/', permanent=True)),
]
# используем static() чтобы добавить соотношения для статических файлов
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
