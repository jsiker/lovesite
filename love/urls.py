from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'love.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home', 'squish.views.home', name='home'),

    #login/logout/register
    url(r'^logout/$', 'squish.views.user_logout', name='logout'),
    url(r'^register/$', 'squish.views.register', name='register'),
    # url(r'^login/$', 'squish.views.user_login', name='login'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),  #user enters email for account they want to reset
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'), #user redirected to email sent page
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',#user gets links to click
    'django.contrib.auth.views.password_reset_confirm',
    name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'), #your password has been reset page
    url(r'^pay/$', 'squish.views.pay', name='pay'),

    #messaging
    url(r'^messages/', include('postman.urls')),

    #stripe
    url(r'^payments/', include("payments.urls")),

    #profile
    url(r'^profile/', 'squish.views.profile', name='profile'),
    # url(r'^upload_pic', 'squish.views.upload_pic', name='upload_pic'),

    #file upload
    # url(r'^upload/$', 'squish.views.upload', name='upload'),

    #messaging
    url(r'^message/', include('django_messages.urls'))


)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)