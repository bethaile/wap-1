from django.shortcuts import render
from django.core import serializers
# Create your views here.


from django.views.generic import TemplateView
from django.views import View

from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from a01.models import Customer
from a01.models import Hall
from a01.models import Movie
from a01.models import Payment
from a01.models import Screening
from django.core.serializers import serialize


class HomeView(TemplateView):

    template_name = 'a01/home.html'

    def get_context_data(self, **kwargs):
        """Context data."""
        context = super(HomeView, self).get_context_data(**kwargs)
        context['movies'] = Movie.objects.all()
        return context


class OrderView(TemplateView):

    def get_context_data(self, **kwargs):
        """Context data."""
        context = super(OrderView, self).get_context_data(**kwargs)
        return context


class GraphView(TemplateView):
    template_name = 'a01/graph.html'

    def get_context_data(self, **kwargs):
        context = super(GraphView, self).get_context_data(**kwargs)
        return context


################################################################################
# DETAIL VIEWS


class DetailView(View):
    get_class = None

    def get(self, req, id):
        obj = get_object_or_404(self.get_class, pk=id)

        json_data = serializers.serialize('json', [obj, ])

        return HttpResponse(json_data, content_type='json')


class MovieDetailView(DetailView):
    get_class = Movie


class HallDetailView(DetailView):
    get_class = Hall


class ScreeningDetailView(DetailView):
    get_class = Screening


class CustomerDetailView(DetailView):
    get_class = Customer


class PaymentDetailView(DetailView):
    get_class = Payment

################################################################################
# DETAIL VIEWS


class ListView(View):
    get_class = None

    def get(self, *args):
        obj_list = self.get_class.objects.all()
        json_data = serializers.serialize('json', obj_list)

        return HttpResponse(json_data, content_type='json')


class MovieListView(ListView):
    get_class = Movie


class HallListView(ListView):
    get_class = Hall


class ScreeningListView(ListView):
    get_class = Screening


class CustomerListView(ListView):
    get_class = Customer


class PaymentListView(ListView):
    get_class = Payment
