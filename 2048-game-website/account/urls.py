from django.conf.urls import url
from . import views
urlpatterns=[url(r'login/',views.login,name='login'),
url(r'home/(?P<id>[0-9]+)/',views.home,name='home'),
url(r'logout/',views.logout,name='logout'),
url(r'forgetpassword/',views.forgetpassword,name='forget'),
url(r'reset/(?P<id>[0-9]+)/(?P<otp>[0-9]+)/',views.reset,name='reset'),
url(r'signup/',views.signup,name='signup'),
url(r'activate/(?P<id>[0-9]+)/(?P<otp>[0-9]+)/',views.activate,name='activate'),
url(r'change/',views.change,name='change'),
]