"""Urls for app a01."""
from django.conf.urls import url

from a01.views import GraphView
from a01.views import OrderView
from a01.views import HomeView
from a01.views import MovieDetailView
from a01.views import HallDetailView
from a01.views import ScreeningDetailView
from a01.views import CustomerDetailView
from a01.views import PaymentDetailView

from a01.views import MovieListView
from a01.views import HallListView
from a01.views import ScreeningListView
from a01.views import CustomerListView
from a01.views import PaymentListView



urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^graph/$', GraphView.as_view(), name='graph'),
    url(r'^order/$', OrderView.as_view(), name='order'),
    url(r'^movie/(?P<id>[0-9]+)/$', MovieDetailView.as_view(), name='moviedetail'),
    url(r'^hall/(?P<id>[0-9]+)/$', HallDetailView.as_view(), name='halldetail'),
    url(r'^screening/(?P<id>[0-9]+)/$', ScreeningDetailView.as_view(), name='screeningdetail'),
    url(r'^customer/(?P<id>[0-9]+)/$', CustomerDetailView.as_view(), name='customerdetail'),
    url(r'^payment/(?P<id>[0-9]+)/$', PaymentDetailView.as_view(), name='paymentdetail'),

    url(r'^movie/list/$', MovieListView.as_view(), name='movie'),
    url(r'^hall/list/$', HallListView.as_view(), name='hall'),
    url(r'^screening/list/$', ScreeningListView.as_view(), name='screening'),
    url(r'^customer/list/$', CustomerListView.as_view(), name='customer'),
    url(r'^payment/list/$', PaymentListView.as_view(), name='payment'),
]
