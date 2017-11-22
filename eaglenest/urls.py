from django.conf.urls import include, url

from . import views


urlpatterns = [
    url(r'^dashboard/$', views.DashboardView.as_view(), name='dashboard'),
    url(r'^$', views.DashboardView.as_view()),
]