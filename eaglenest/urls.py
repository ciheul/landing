from django.conf.urls import include, url

from . import views


urlpatterns = [
    url(r'^dashboard/$', views.DashboardView.as_view(), name='dashboard'),
    url(r'^component/tci/$', views.ComponentTciListView.as_view(), name='component-tci-list'),
    url(r'^component/tci/1/$', views.ComponentTciView.as_view(), name='component-tci'),
    url(r'^component/oc/$', views.ComponentOcView.as_view(), name='component-oc'),
    url(r'^$', views.DashboardView.as_view()),
]