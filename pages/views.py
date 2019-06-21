from .models import Page
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

class StaffRequiredMixin(object):
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin,self).dispatch(request,*args,**kwargs)


# Create your views here.
class pageListView(ListView):
    model = Page
    

class pageDetailView(DetailView):
    model = Page

@method_decorator(staff_member_required, name= 'dispatch')
class PageCreate( CreateView):
    model = Page
    fields = ['title','content','order']
    success_url = reverse_lazy('pages:pages')

    

class PageUpdate(UpdateView):
    model = Page
    fields = ['title','content','order']
    template_name_suffix = '_update_form'
    def get_success_url(self):
        return reverse_lazy('pages:update', args = [self.object.id])  