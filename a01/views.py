from django.shortcuts import render

# Create your views here.


from django.views.generic import TemplateView
from django.views import View

from django.http import JsonResponse
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


class DetailView(View):
    get_class = None

    def get(self, req, id):
        obj = get_object_or_404(self.get_class, pk=id)
        return JsonResponse(serialize('json', obj))


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
