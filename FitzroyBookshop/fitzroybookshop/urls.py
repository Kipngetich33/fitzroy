from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

# The following importations allows the app to make use of the static path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('^$',views.home,name = 'Home'),
    url('^search/',views.search,name = 'Search'),
    url('^maintenance/',views.maintenance,name = 'Maintenance'),
    url('^site/map',views.map,name = 'Site_Map'),
]
if settings.DEBUG:
   	urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)