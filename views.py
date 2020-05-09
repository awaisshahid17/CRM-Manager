from django.core.urlresolvers import reverse_lazy, reverse
from django.shortcuts import get_object_or_404, render, redirect
from django.template.loader import render_to_string
from crm_manager.forms import PromocodeForm
from crm_manager.models import Promocode
from django.views.generic import View
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required



# Create your views here.

class PromoView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(PromoView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        obj = Promocode.objects.all().order_by("-id")
        return render(request, 'promo.html', {"obj": obj})

    def post(self, request):
        obj = Promocode.objects.all().order_by("-id")
        print "promo list"
        return render(request, 'partial/promo_list.html', {"obj": obj})

class AddPromo(View):
    def post(self, request):
        print "Add promocode"
        form = PromocodeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('promo')
        return render(request, 'add_promo.html', {'form': form})

    def get(self, request):
        form = PromocodeForm()
        return render(request, 'add_promo.html', {'form': form})

class Landing(View):
    def get(self, request):
        return render(request, "landing.html", {})

