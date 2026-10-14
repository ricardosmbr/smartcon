from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ClienteNovoForm, EditarCliente, MostrarCliente
from .models  import Cliente
from contrato.models import Contrato, ContratActions, ContratToken
from carteira.models import Carteira, CarteiraToken
from .decorators import permition_required
from django.contrib import messages
from eth_account import Account
from itertools import chain
from web3 import Web3, HTTPProvider
from django.conf import settings
from django.utils import timezone
from django.db.models import Q

@login_required	
def cliente(request):
	base_clientes = Cliente.objects.filter(id_usuario=request.user.pk)
	clientes = base_clientes.order_by('-create_at')
	template_name = 'cliente.html'
	pesquisa = request.GET.get('q', '').strip()
	if pesquisa:
		clientes = clientes.filter(Q(name__icontains=pesquisa) | Q(cpf__icontains=pesquisa) | Q(tel__icontains=pesquisa))
	context = {
		'clientes': clientes,
		'pesquisa': pesquisa,
		'total_clientes': base_clientes.count(),
		'novos_este_mes': base_clientes.filter(create_at__year=timezone.localdate().year, create_at__month=timezone.localdate().month).count(),
	}		
	return render(request, template_name, context)

@login_required
def cliente_novo(request):
	context = {}
	template_name = 'cliente_register.html'
	if request.method == 'POST':
		form = ClienteNovoForm(request.POST)
		if form.is_valid():
			cliente = form.save(commit=False)
			cliente.id_usuario = request.user
			cliente.save()
			messages.success(request,"Cliente cadastrado com sucesso",extra_tags='text-success')
			return redirect('cli:cliente')
	else:
		form = ClienteNovoForm()
	context['form'] = form
	return render(request, template_name, context)

@login_required
@permition_required
def cliente_editar(request,pk):
	template_name = 'cliente_editar.html'
	cliente = request.cliente
	context = {}
	if request.method == 'POST':
		form = EditarCliente(request.POST or None, instance=cliente)
		if form.is_valid():
			form.save()
			messages.success(request,"Cliente salvo com sucesso",extra_tags='text-success')
			return redirect('cli:cliente')
		else:messages.success(request,"Erro",extra_tags='text-danger')
	else:
		form = EditarCliente(instance=cliente)
	context['form'] = form
	return render(request, template_name, context)			

@login_required
@permition_required
def cliente_mostrar(request,pk):
	template_name = 'cliente_mostrar.html'
	cliente = request.cliente
	context = {}
	form = MostrarCliente(instance=cliente)
	if request.method == 'POST':
		return redirect('cli:cliente')
	context.update({'form': form, 'cliente': cliente})
	return render(request, template_name, context)

@login_required
@permition_required
def cliente_apagar(request,pk):
	cliente = request.cliente
	if request.method != 'POST':
		return render(request, 'cliente_confirmar_apagar.html', {'cliente': cliente})
	cliente.delete()
	messages.success(request,"Cliente apagado com sucesso",extra_tags='text-success')
	return redirect('cli:cliente')

@login_required
def cliente_pesquisa(request):
	return redirect('cli:cliente')

