from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'coding.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'news.views.home', name='home'),
    url(r'^contact/', 'news.views.contact', name='contact'),
    url(r'^admin/', include(admin.site.urls)),
]
