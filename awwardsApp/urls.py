from django.conf.urls import url,include
from django.conf import settings
from . import views
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^accounts/profile/', views.my_profile, name='my_profile'),
    url(r'register/',views.register, name='register'),
    url(r'project/(\d+)',views.rate_project,name='rate-project'),
    url(r'profile/(\d+)',views.profile,name='profile'),
    url(r'my_profile',views.my_profile,name='my_profile'), 
    url(r'^new/project$', views.new_project, name='new_project'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^ratings/', include('star_ratings.urls', namespace='ratings')),
    url(r'^accounts/', include('registration.backends.simple.urls')),


]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
