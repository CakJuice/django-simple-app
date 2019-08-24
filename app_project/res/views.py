from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView

from .models import Country


@method_decorator(login_required, 'dispatch')
class CountryCreateView(CreateView):
    model = Country
    fields = ['name', 'code', 'image']
    template_name = 'res/country/create.html'
    success_url = reverse_lazy('res_country_create')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.updated_by = self.request.user
        return super().form_valid(form)
