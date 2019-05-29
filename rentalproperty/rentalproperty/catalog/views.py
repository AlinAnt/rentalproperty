from django.shortcuts import render, render_to_response
from .models import Area, TypeArea
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime
from .forms import RenewAreaForm
from django.views.generic.edit import FormView
from django.contrib.auth import login

def index(request):
    num_areas = Area.objects.all().count()
    num_types = TypeArea.objects.all().count()

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    return render(
        request,
        'index.html',
        context={'num_areas': num_areas, 'num_types': num_types, 'num_visits': num_visits},
    )


class RegisterList(FormView):
    form_class = UserCreationForm
    success_url = "/"
    template_name = "registration/register.html"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super(RegisterList, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegisterList, self).form_invalid(form)


class AreaListView(generic.ListView):
    model = Area
    paginate_by = 10
    context_object_name = 'area_list'


class TypeAreaListView(generic.ListView):
    model = TypeArea
    context_object_name = 'type_area_list'


class AreaDetailView(generic.DetailView):
    model = Area


class TypeAreaDetailView(generic.DetailView):
    model = TypeArea
    context_object_name = 'type_area_detail.html'
    list_filter = ('type_area',)


class RentalAreasByUserListView(LoginRequiredMixin, generic.ListView):
    model = Area
    template_name = 'catalog/area_list_rent_user.html'
    paginate_by = 10

    def get_queryset(self):
        return Area.objects.filter(rent=self.request.user).filter(status='Busy').order_by('endOfRental')


class RentalBooksAllListView(PermissionRequiredMixin, generic.ListView):
    model = Area
    permission_required = ''
    template_name = 'catalog/area_list_rent_all.html'
    paginate_by = 10

    def get_queryset(self):
        return Area.objects.filter(status="Busy").order_by('endOfRental')


class RentThisArea(generic.ListView):
    model = TypeArea
    template_name = 'catalog/rent_this_area.html'


def renew_area_seller(request, pk):
    area = get_object_or_404(Area, pk=pk)

    if request.method == 'POST':

        form = RenewAreaForm(request.POST)

        if form.is_valid():
            area.endOfRental = form.cleaned_data['renewal_date']
            area.save()

        return HttpResponseRedirect(reverse('all-rent'))

    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=12)
        form = RenewAreaForm(initial={'renewal_date': proposed_renewal_date})

    context = {
        'form': form,
        'area': area,
    }

    return render(request, 'catalog/rent_this_area.html', context)




