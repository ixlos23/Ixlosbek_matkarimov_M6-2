from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, FormView
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import UserForm, UserProfileForm

from apps.forms import RegisterForm
from django.shortcuts import render
from .models import Category, Product



class HomeTemplateView(ListView):
    model = Product
    template_name = 'apps/product/product-grid.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product-details.html'
    context_object_name = 'detail'


class HomeView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = ''
    success_url = reverse_lazy('home')


class RegisterFormView(FormView):
    template_name = 'login_registr/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return redirect('login')




@login_required
def profile_update(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.userprofile)

    return render(request, 'profile_update.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })




def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()

    if category_slug:
        category = Category.objects.get(slug=category_slug)
        products = products.filter(category=category)

    return render(request,'product_list.html', {
        'category': category,
        'categories': categories,
        'products': products
    })
