from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('dailyclass/', include('dailyclass.urls')),
    path('community/', include('community.urls')),

]
