from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import CreateView,UpdateView
from django.contrib.messages.views import SuccessMessageMixin

from django.urls import reverse_lazy

from .forms import PublisherForm
from public.models import *

# Create your views here.

def dashboard(request):
    return render(request, 'admin/dashboard.html')

def add_pub(request):
    if request.method != 'POST':
        pubs = Publisher.objects.all()
        
        return render(request, 'admin/components/pub_form.html', context={'pubs':pubs})
    else:
        pub_name = request.POST['pub_name']
        add_pub_query = Publisher(publisher=pub_name)
        add_pub_query.save()
        messages.success(request, 'Publisher saved successfully!')
        return redirect('admin_app:add_pub')

class PublisherAdd(SuccessMessageMixin, CreateView):
    model           = Publisher
    form_class      = PublisherForm
    template_name   = 'admin/components/pub_form.html'
    success_url     = reverse_lazy('admin_app:add_pub')
    success_message = "Publication added successfully!"
    def get_context_data(self, **kwargs):
        context            = super().get_context_data(**kwargs)
        context['pubs'] = Publisher.objects.all().order_by('id')
        return context
        
class PublisherEdit(SuccessMessageMixin,UpdateView):
    model           = Publisher
    form_class      = PublisherForm
    template_name   = 'admin/components/pub_form.html'
    success_url     = reverse_lazy('admin_app:add_pub')
    success_message = "Publication Edited successfully!"
    def get_context_data(self, **kwargs):
        context            = super().get_context_data(**kwargs)
        context['pubs'] = Publisher.objects.all().order_by('id')
        return context

def publisher_delete(request, pub_id):
    pub = Publisher.objects.delete(id=pub_id)
    pub.save()
    messages.success(request,'Publication deleted successfully!')
    return redirect('admin_app:add_pub')