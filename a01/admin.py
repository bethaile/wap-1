from django.contrib import admin
from .models import Customer
from .models import Hall
from .models import Payment
from .models import Screening
from .models import Movie


admin.site.register(Customer)
admin.site.register(Hall)
admin.site.register(Payment)
admin.site.register(Screening)
admin.site.register(Movie)
# Register your models here.
