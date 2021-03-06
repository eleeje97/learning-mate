from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('dailyclass/', include('dailyclass.urls')),
    path('community/', include('community.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    re_path(r'^fp/', include('django_drf_filepond.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
