from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from src.settings.base import MEDIA_ROOT, MEDIA_URL
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.api.urls'))
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
urlpatterns += [re_path(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT,}),]