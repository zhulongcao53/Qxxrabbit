"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import patterns, include, url    
from django.contrib import admin  
from blog import views
from blog.views import *  
from DjangoUeditor import urls as DjangoUeditor_urls
from django.conf import settings

admin.autodiscover()  
  
urlpatterns = patterns('',  
    # Examples:  
    # url(r'^$', 'mysite.views.home', name='home'),  
    # url(r'^blog/', include('blog.urls')),  
  
    url(r'^grappelli/',include('grappelli.urls')), 
    url(r'^admin/', include(admin.site.urls)),  
    url(r'^$', archive),
    url(r'^ueditor/', include(DjangoUeditor_urls)),
    url(r'^tag(?P<tag>\w+)/$', 'blog.views.search_tag', name = 'search_tag'),
    url(r'^search/$','blog.views.blog_search', name = 'search'),
) 

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#if settings.DEBUG:
    #urlpatterns += patterns('',
        #url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
    #)
