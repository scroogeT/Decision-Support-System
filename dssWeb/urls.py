from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^routes/$', views.dailyRoutes, name='dailyRoutes'),
    url(r'^fees/$', views.feesTable, name='feesTable'),
    url(r'^routeAllocation$', views.routeAllocations, name='routeAllocation'),
    url(r'^vrpSolve$', views.vrpSolve, name='vrpSolve'),
    url(r'^profitability$', views.profitability, name='profitabilityAnalysis'),
]