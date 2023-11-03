from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from .forms import ContactoForm
from .models import CaruselLanding

class HomePageView(TemplateView):
    template_name = "core/base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carusel_landings'] = CaruselLanding.objects.all()
        context['form'] = ContactoForm()
        return context

    def post(self, request):
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core/base.html')  # Redirige a la URL de agradecimiento
        context = {'form': form, 'carusel_landings': CaruselLanding.objects.all()}
        return render(request, self.template_name, context)
