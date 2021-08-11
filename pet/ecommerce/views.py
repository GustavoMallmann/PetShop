from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import User_creation_form
from .models import Produto
import pdb
# Create your views here.


def home(request):
    return HttpResponse('Bem vindo!')


def create_client(request):

    form = User_creation_form()

    if request.method == 'POST':
        form = User_creation_form(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'ecommerce/criarCliente.html', context)


class Individual_product(DetailView):

    model = Produto
    template_name = 'ecommerce/produto_x.html'
    context_object_name = 'produto'

    def get_object(self):
        id_ = self.kwargs.get('id')  # chave primaria, id do produto
        return get_object_or_404(Produto, id=id_)


class ProductsView(ListView):
    # carregar barras opcoes
    model = Produto
    template_name = 'ecommerce/produtos.html'
    context_object_name = 'lista_de_produtos'
