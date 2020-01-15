from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.home,name = 'home'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^webiste/(\d+)',views.website,name ='website'),
    url(r'^new/website$', views.new_website, name='new-website'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)