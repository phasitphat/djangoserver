"""myproject URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from myapp import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^myapp/', include('myapp.urls', namespace='myapp')),
    
    url(r'^$', views.Home, name='Home'),
    url(r'^(?P<id>[0-9]+)/$', views.Detail, name='Detail'),

    url(r'^waitingpayment/', views.WaitingPayment, name='WaitingPayment'),
    url(r'^waitingpayment/(?P<id>[0-9]+)/$', views.Detail, name='Detail'),
    url(r'^paid/', views.Paid, name='Paid'),
    url(r'^paid/(?P<id>[0-9]+)/$', views.Detail, name='Detail'),
    url(r'^reportpayment/', views.ReportPayment, name='ReportPayment'),
    url(r'^reportpayment/(?P<id>[0-9]+)/$', views.Detail, name='Detail'),
    url(r'^close/', views.Close, name='Close'),
    url(r'^close/(?P<id>[0-9]+)/$', views.Detail, name='Detail'),
    url(r'^contactus/', views.Contact, name='Contact'),
    url(r'^contactus/(?P<id>[0-9]+)/$', views.ContactusDetail, name='ContactusDetail'),
]

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
