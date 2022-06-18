from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('accounts.urls')),
    # path('dailyclass/', include('dailyclass.urls')),
    path('community/', include('community.urls')),

]
