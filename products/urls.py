from django.conf.urls import include, url
from . import views

urlpatterns = [
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^cat$', views.categories),
    url(r'^prod$', views.items),
]