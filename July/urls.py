"""July URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from users.views import RegisterView, LoginView, LogoutView, PasswordView, RestPasswordView,MideaAuthenticateView
from blog.views import *

from blog.feeds import RssSiteNewsFeed, AtomSiteNewsFeed
from django.contrib.sitemaps.views import sitemap
from blog.sitemap import BlogSitemap
from werobot.contrib.django import make_view
from .robot import robot
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static
sitemaps = {
    'static': BlogSitemap,
}

urlpatterns = [
    # ========== Blog Home =========
    url(r'^$', ArticleListView.as_view(), name='index'),
    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'^article/(?P<article_url>.*)$', ArticleDetailView.as_view(), name='article'),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    # ========== User =========
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^password/$', PasswordView.as_view(), name='password'),
    url(r'^rest_password/$', RestPasswordView.as_view(), name='restpassword'),
    url(r'^midea_authenticate/$', MideaAuthenticateView.as_view(), name='mideaauthenticate'),
    # ========== Admin =========
    url(r'^admin/', include('admin.urls', namespace='admin')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    url(r'^rss\.xml$', RssSiteNewsFeed()),
    url(r'^atom\.xml$', AtomSiteNewsFeed()),
    # ========== WechatRobot =========
    url(r'^robot/',make_view(robot)),

    url(r'^favicon.ico$',RedirectView.as_view(url=r'static/favicon.ico')),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_URL)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
