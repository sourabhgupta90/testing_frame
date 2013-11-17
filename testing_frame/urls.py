from django.conf.urls import patterns, include, url

from testing_frame.test_app import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', 'testing_frame.views.home', name='home'),
    # url(r'^testing_frame/', include('testing_frame.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
    
    url(r'^fire_ajax/2/$', views.fire_ajax, name='fire_ajax'),
    url(r'^main_page$', views.render_main_page, name='main_page'),
    url(r'^webworker$', views.webworker, name='webworker'),
    url(r'^colander$', views.colander_test),
    url(r'^css-test$', views.css_test),
    url(r'^dashboard$', views.yui_test, name='dashboard'),
    url(r'^handle_bar$', views.handle_bar_test),
    url(r'^page/(\w+_*\w+)/$', views.sidebar_page),
    url(r'^test_chosen/2/$', views.test_chosen),
    url(r'^$', views.index, name='index'),
    url(r'^time/$', views.current_datetime),
    url(r'^datasource/$', views.datasource_template),
    url(r'^datasource_data/$', views.datasource_data),
    url(r'^time/plus/(\d{1,2})/$', views.hours_ahead),
)
