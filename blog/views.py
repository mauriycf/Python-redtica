from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .models import Categoria,Entrada,Document
from .forms import UserForm,PerfilForm
from django.contrib.auth import logout
# Create your views here.

"""class IndexView(ListView):

	template_name = 'index.html'
	model = Entrada

class EntradaDetailView(DetailView):
	template_name = 'entrada_detail.html'
	model = Entrada"""

"""def index(request):
	queryset = Entrada.object.all()
	context = {
		"template_name": "index.html",
		"queryset": queryset,
	}

	return render(request, "index.html", context)"""
class IndexView(ListView):

	template_name = 'index.html'
	model = Entrada

class post_list(ListView):
	template_name = 'post_list.html'
	model = Entrada

class biblioteca(ListView):
	template_name = 'biblioteca.html'
	model = Document

def post_detail(request, slug=None):
	instance = get_object_or_404(Entrada, slug=slug)
	context = {
		"title": instance.titulo,
		"instance": instance,
	}

	return render(request, "entrada_detail.html", context)


class UserFormView(ListView):
	form_class = UserForm
	template_name = 'user/registration_form.html'

	def get(self, request):
		form = self.form_class()
		return render(request, self.template_name, {'form': form})

	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():

			user = form.save(commit=False)
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()

			user = authenticate(username=username, password=password)

			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect('user/perfil_form.html')
		return render(request, self.template_name, {'form': form})

class PerfilForm(ListView):
	form_class = PerfilForm
	template_name = 'user/perfil_form.html'

	def get(self, request):
		form = self.form_class()
		return render(request, self.template_name, {'form': form})

	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():

			form.save()

			if form is not None:
				return redirect('user/perfil.html')
		return render(request, self.template_name, {'form': form})


def logout(request):
    logout(request)