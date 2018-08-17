"""sjourney URL Configuration

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
from django.conf.urls import url, patterns, include
from django.contrib import admin
from sjourney.app.views import HomeView, AppView, logout
from sjourney.app.api import UserListAPIView, SocialAuthUserListAPIView
from sjourney.app.api import SocialAuthUserDetailAPIView
from sjourney.app.api import CategoryListAPIView, CategoryDetailAPIView
from sjourney.app.api import PictureListAPIView, PictureDetailAPIView
from sjourney import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^$', HomeView.as_view()),
    url(r'^app/$', AppView.as_view(), name='app'),
    url(r'^logout/$', logout),

    url(r'^api/v1/users/$', UserListAPIView.as_view(), name='user'),
    url(r'^api/v1/susers/$',
        SocialAuthUserListAPIView.as_view(), name='suser'),
    url(r'^api/v1/susers/(?P<pk>[0-9]+)',
        SocialAuthUserDetailAPIView.as_view()),

    url(r'^api/v1/categories/$',
        CategoryListAPIView.as_view(), name='category'),
    url(r'^api/v1/categories/(?P<pk>[0-9]+)',
        CategoryDetailAPIView.as_view(), name='one_category'),

    url(r'^api/v1/pics/$', PictureListAPIView.as_view(), name='picture'),
    url(r'^api/v1/pics/(?P<pk>[0-9]+)', PictureDetailAPIView.as_view()),

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT,
    }),
    url(r'^docs/', include('rest_framework_docs.urls')),
]
