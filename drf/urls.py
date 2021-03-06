"""drf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
from rest_framework import routers
from quickstart.views import LoginView, LogoutView, Photo_GroupListView, PhotoListView, PhotosByGroupIdListView

#api route
router = routers.DefaultRouter()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/login/', LoginView.as_view()),
    url(r'^api/v1/logout/', LogoutView.as_view()),
    url(r'^api/v1/groups/$', Photo_GroupListView.as_view()),
    url(r'^api/v1/group/(?P<pk>[0-9a-zA-Z@]+)/$', Photo_GroupListView.as_view()),
    url(r'^api/v1/photos/(?P<pk>[0-9]+)/$', PhotoListView.as_view()),
    #Query params
    url(r'^api/v1/photos/\?group=(?P<group>[0-9a-zA-Z@]+)/$', PhotosByGroupIdListView.as_view()),
]
