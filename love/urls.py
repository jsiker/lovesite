from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'love.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', 'squish.views.home', name='home'),

    #login/logout/register
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^register/$', 'squish.views.register', name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),  #user enters email for account they want to reset
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'), #user redirected to email sent page
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',#user gets links to click
    'django.contrib.auth.views.password_reset_confirm',
    name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'), #your password has been reset page
    url(r'^pay/$', 'squish.views.pay', name='pay'),

    #stripe
    url(r'^payments/', include("payments.urls")),

    #profile
    url(r'^profile/', 'squish.views.profile', name='profile'),


)
