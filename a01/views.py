
import json
import datetime

from django.db import models

from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.core import serializers
from django.core.serializers import serialize
# Create your views here.


from django.views import View
from django.views.generic import TemplateView

from django.http import JsonResponse
from django.http import HttpResponse

from a01.models import Customer
from a01.models import Hall
from a01.models import Movie
from a01.models import Payment
from a01.models import Screening


class HomeView(TemplateView):

    template_name = 'a01/home.html'

    def get_context_data(self, **kwargs):
        """Context data."""
        context = super(HomeView, self).get_context_data(**kwargs)
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
        datas = []
        for i in obj_list:
            data = {}
            for k in i._meta.get_fields():
                try:
                    val = getattr(i, k.name)
                    if isinstance(val, datetime.date) or isinstance(val, datetime.datetime) or isinstance(val, datetime.time):
                        val = val.isoformat()
                    elif isinstance(val, models.Model):
                        val = val.__str__()
                except:
                    continue
                data[k.name] = val
            datas.append(data)
        return HttpResponse(json.dumps(datas), content_type='json')


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


class TicketOrder(View):

    def post(self):





        pass
