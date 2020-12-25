from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.views.generic import CreateView,UpdateView,View
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User

from django.urls import reverse_lazy,reverse

from .forms import PublisherForm,BookForm, CategoryForm
from public.models import *

class AdminRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):

    def test_func(self):
        return self.request.user.is_superuser

# Create your views here.
@user_passes_test(lambda u: u.is_superuser)
def dashboard(request):
    return render(request, 'admin/dashboard.html')

@user_passes_test(lambda u: u.is_superuser)
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

class PublisherAdd(AdminRequiredMixin, SuccessMessageMixin, View):
    template_name   = 'admin/components/pub_form.html'
    pub_form = PublisherForm
    ctg_form = CategoryForm
    def get_context_data(self, **kwargs):
        context            = {}
        context['pubs'] = Publisher.objects.all().order_by('id')
        context['ctgs'] = BookCategory.objects.all().order_by('id')
        if 'pub_form' not in kwargs:
            context['pub_form'] = self.pub_form
        if 'ctg_form' not in kwargs:
            context['ctg_form'] = self.ctg_form

        return context

    def get(self, *args, **kwargs):
        return render(self.request, self.template_name, self.get_context_data())

    def post(self, *args, **kwargs):
        ctxt = {}
        if 'publisher' in self.request.POST:
            pub_form = PublisherForm(self.request.POST)
            if pub_form.is_valid():
                pub_form.save()
                messages.success(self.request,"Publication added successfully!")
                return HttpResponseRedirect(reverse('admin_app:add_pub'))

        elif 'category' in self.request.POST:
            ctg_form = CategoryForm(self.request.POST)
            if ctg_form.is_valid():
                ctg_form.save()
                messages.success(self.request,"Category added successfully!")
                return HttpResponseRedirect(reverse('admin_app:add_pub'))
        return render(self.request, self.template_name, self.get_context_data(**ctxt))

class PubCommonEdit(AdminRequiredMixin, SuccessMessageMixin, View):
    template_name   = 'admin/components/pub_form.html'
    pub_form = PublisherForm
    ctg_form = CategoryForm
    def get_object(self):
        try:
            obj = Publisher.objects.get(pk=self.kwargs['pk'])
        except Publisher.DoesNotExist:
            raise Http404('Publisher not found!')
        return obj
    def get_context_data(self, **kwargs):
        context            = {}
        context['publisher'] = self.get_object()
        context['pubs'] = Publisher.objects.all().order_by('id')
        context['ctgs'] = BookCategory.objects.all().order_by('id')
        if 'pub_form' not in kwargs:
            context['pub_form'] = PublisherForm(instance=self.get_object())
        if 'ctg_form' not in kwargs:
            context['ctg_form'] = self.ctg_form

        return context

    def get(self, *args, **kwargs):
        return render(self.request, self.template_name, self.get_context_data())

    def post(self, *args, **kwargs):
        ctxt = {}
        if 'publisher' in self.request.POST:
            pub_form = PublisherForm(self.request.POST,instance=self.get_object())
            if pub_form.is_valid():
                pub_form.save()
                messages.success(self.request,"Publication added successfully!")
                return HttpResponseRedirect(reverse('admin_app:add_pub'))

        elif 'category' in self.request.POST:
            ctg_form = CategoryForm(self.request.POST)
            if ctg_form.is_valid():
                ctg_form.save()
                messages.success(self.request,"Category added successfully!")
                return HttpResponseRedirect(reverse('admin_app:add_pub'))
        return render(self.request, self.template_name, self.get_context_data(**ctxt))

class CategoryCommonEdit(AdminRequiredMixin, SuccessMessageMixin, View):
    template_name   = 'admin/components/pub_form.html'
    pub_form = PublisherForm
    ctg_form = CategoryForm
    def get_object(self):
        try:
            obj = BookCategory.objects.get(pk=self.kwargs['pk'])
        except BookCategory.DoesNotExist:
            raise Http404('Category not found!')
        return obj
    def get_context_data(self, **kwargs):
        context            = {}
        context['category'] = self.get_object()
        context['pubs'] = Publisher.objects.all().order_by('id')
        context['ctgs'] = BookCategory.objects.all().order_by('id')
        if 'pub_form' not in kwargs:
            context['pub_form'] = self.pub_form
        if 'ctg_form' not in kwargs:
            context['ctg_form'] = CategoryForm(instance=self.get_object())

        return context

    def get(self, *args, **kwargs):
        return render(self.request, self.template_name, self.get_context_data())

    def post(self, *args, **kwargs):
        ctxt = {}
        if 'publisher' in self.request.POST:
            pub_form = PublisherForm(self.request.POST)
            if pub_form.is_valid():
                pub_form.save()
                messages.success(self.request,"Publication added successfully!")
                return HttpResponseRedirect(reverse('admin_app:add_pub'))

        elif 'category' in self.request.POST:
            ctg_form = CategoryForm(self.request.POST, instance=self.get_object())
            if ctg_form.is_valid():
                ctg_form.save()
                messages.success(self.request,"Category added successfully!")
                return HttpResponseRedirect(reverse('admin_app:add_pub'))
        return render(self.request, self.template_name, self.get_context_data(**ctxt))

@user_passes_test(lambda u:u.is_superuser)
def publisher_delete(request, pub_id):
    pub = Publisher.objects.get(id=pub_id)
    pub.delete()
    messages.success(request,'Publication deleted successfully!')
    return redirect('admin_app:add_pub')

@user_passes_test(lambda u:u.is_superuser)
def category_delete(request, ctg_id):
    ctg = BookCategory.objects.get(id=ctg_id)
    ctg.delete()
    messages.success(request,'Category deleted successfully!')
    return redirect('admin_app:add_pub')

class BookAdd(AdminRequiredMixin, SuccessMessageMixin, CreateView):
    model           = Book
    form_class      = BookForm
    template_name   = 'admin/components/book_form.html'
    success_url     = reverse_lazy('admin_app:add_book')
    success_message = "Book added successfully!"
    def get_context_data(self, **kwargs):
        context            = super().get_context_data(**kwargs)
        context['books'] = Book.objects.all().order_by('id')
        return context

    def save(self, request):
        obj = super().save(commit=False)
        obj.createdBy = request.user
        obj.save()

class BookEdit(AdminRequiredMixin, SuccessMessageMixin, UpdateView):
    model           = Book
    form_class      = BookForm
    template_name   = 'admin/components/book_form.html'
    success_url     = reverse_lazy('admin_app:add_book')
    success_message = "Book edited successfully!"
    def get_context_data(self, **kwargs):
        context            = super().get_context_data(**kwargs)
        context['books'] = Book.objects.all().order_by('id')
        return context

@user_passes_test(lambda u:u.is_superuser)
def book_delete(request,book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    messages.success(request, 'Book removed successfully!')
    return redirect('admin_app:add_book')

@user_passes_test(lambda u:u.is_superuser)
def booked_orders_list(request):
    booked_orders = OrderBooking.objects.all()
    return render(request, 'admin/components/booked_orders.html', context={'booked_orders':booked_orders})

@user_passes_test(lambda u:u.is_superuser)
def view_selling_reports(request):
    selling_reports = BookSelling.objects.all().order_by('id').reverse()
    return render(request, 'admin/components/view_selling_reports.html', context={'sold_books':selling_reports})

@user_passes_test(lambda u:u.is_superuser)
def view_buying_reports(request):
    buying_reports = BookBuying.objects.all().order_by('id').reverse()
    return render(request, 'admin/components/view_buying_reports.html', context={'bought_books':buying_reports})

@user_passes_test(lambda u:u.is_superuser)
def view_customer_list(request):
    customer_list = User.objects.filter(is_superuser=False, is_staff=False)
    return render(request, 'admin/components/view_customers_list.html', context={'customers':customer_list})