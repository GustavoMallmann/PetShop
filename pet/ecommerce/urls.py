from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    ##
    path('produtos', views.ProductsView.as_view(), name='pagina_de_produtos'),
    path('produtos/<int:id>', views.Individual_product.as_view(),
         name='detalhe_produto'),
    ##
    path('registrar', views.create_client, name='criar_cliente'),
    # path('atualizar_cadastro',, name='atualizar_cadastro'),
    # path('login',, name='login'),
    # path('carrinho',, name='carrinho'),
    # path('sobre',, name='sobre'),
    # path('comprar',, name='comprar'),

]
