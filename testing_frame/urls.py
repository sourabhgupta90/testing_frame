from django.conf.urls import patterns, include, url

from testing_frame.test_app import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testing_frame.views.home', name='home'),
    # url(r'^testing_frame/', include('testing_frame.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^fire_ajax/2/$', views.fire_ajax, name='fire_ajax'),
    url(r'^$', views.index, name='index'),
    
    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
)
