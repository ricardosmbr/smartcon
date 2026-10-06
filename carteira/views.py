from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from contrato.models import Contrato, ContratActions, ContratToken
from .forms import MostrarCarteira,CarteiraNovaForm, NovoTokenForm
from .models import Carteira, CarteiraToken
from cliente.models import Cliente
from django.contrib import messages
from eth_account import Account
from itertools import chain
from web3 import Web3, HTTPProvider
from django.conf import settings
from contrato.arquivo import AbiToken
from sistema.utils import saldo_token

@login_required
def carteira_mostrar(request):
	template_name = 'carteira_mostrar.html'
	cliente = Cliente.objects.filter(id_usuario = request.user.pk)
	carteira = Carteira.objects.filter(id_cliente__in=cliente).select_related('id_cliente').order_by('id_cliente__name', 'name')

	context = {}
	form = MostrarCarteira()
	if request.method == 'POST':
		pesquisa = request.POST.get("pescli", "").strip()
		carteira = carteira.filter(name__icontains=pesquisa)
	context['carteiras'] = carteira
	return render(request, template_name, context)

@login_required
def carteira_gerar(request):
	template_name = 'carteira_gerar.html'
	context = {}
	if request.method == 'POST':
		form = CarteiraNovaForm(request.POST,user=request.user.id)
		if form.is_valid():
			form.save()
			messages.success(request,"Carteira gerada com sucesso",extra_tags='text-success')
			return redirect('car:carteira')	
		else:messages.success(request,"Erro ao gerar carteira",extra_tags='text-danger')

	form = CarteiraNovaForm(user=request.user.id)
	context['form'] = form
	return render(request, template_name, context)

@login_required
def carteira_apagar(request,pk):
	carteira = get_object_or_404(Carteira, pk=pk)
	carteira.delete()
	messages.success(request,"Carteira apagada com sucesso",extra_tags='text-success')
	return redirect('car:carteira')

@login_required
def carteira_amostra(request,pk):
	template_name = 'carteira_amostra.html'
	carteira = get_object_or_404(Carteira, pk=pk)
	tk = []
	lista = []
	tokining = CarteiraToken.objects.filter(id_carteira=carteira.id)
	w3 = Web3(HTTPProvider(settings.PROVEDOR))
	try:
		bal = w3.eth.get_balance(carteira.public_key)
		carteira.saldo = saldo_token(str(bal), 18)
	except Exception:
		messages.error(
			request,
			'Não foi possível consultar a rede Sepolia agora. Exibindo o último saldo salvo.'
		)
	if tokining:
		for tk in tokining:
			if tk.id_token:
				tok = ContratToken.objects.get(pk = tk.id_token)
				#abi = tok.id_contrato.abi
				abi = AbiToken()
				adr = tok.id_contrato.contract_address
			else:
				abi = AbiToken()
				adr = w3.to_checksum_address(tk.contract)

			try:
				erc20 = w3.eth.contract(address=adr,abi=abi)
				tk.saldo = erc20.functions.balanceOf(carteira.public_key).call()
				tk.saldo = saldo_token(str(tk.saldo),tk.digitos)
				tk.save()				
			except:
				print('Erro na requisição de saldo')
				continue

	form = MostrarCarteira(instance=carteira)
	context = {
		'form':form,
		'tok':tokining,
		'tk':carteira.id
	}
	return render(request, template_name, context)

@login_required
def token_novo(request,tk):
	template_name = 'token_novo.html'
	carteira = Carteira.objects.get(pk=tk)
	form = NovoTokenForm()
	if request.method == 'POST':
		form = NovoTokenForm(request.POST)
		if form.is_valid():
			address = form.cleaned_data['token']
			abi = AbiToken()
			w3 = Web3(HTTPProvider(settings.PROVEDOR))
			try:
				erc20 = w3.eth.contract(address=address, abi=abi)
				saldo = erc20.functions.balanceOf(carteira.public_key).call()
				simbolo = erc20.functions.symbol().call()
				nome = erc20.functions.name().call()
				digitos = erc20.functions.decimals().call()
			except Exception:
				form.add_error(
					'token',
					'Não foi possível consultar esse contrato na Sepolia. Confira o endereço e se o contrato ERC-20 está publicado nessa rede.'
				)
			else:
				CarteiraToken.objects.create(
					id_carteira=carteira,
					contract=address,
					saldo=saldo,
					simbolo=simbolo,
					digitos=digitos,
					token=nome,
				)
				return redirect('car:carteira_amostra', carteira.id)
		
	context = {
		'form':form
	}
	return render(request, template_name, context)

@login_required
def token_apagar(request,pk):
	carteira = CarteiraToken.objects.get(pk=pk)
	carteira.delete()
	messages.success(request,"Token apagada com sucesso",extra_tags='text-success')
	return redirect('car:carteira')

@login_required
def consultar(request):
	template_name = 'carteira_consultar.html'
	context = {}
	if request.method == 'POST':
		pesquisa = request.POST.get("pescart")
		w3 = Web3(HTTPProvider(settings.PROVEDOR))
		try:
			bal = w3.eth.get_balance(pesquisa)
		except Exception as e:
			messages.success(request,e,extra_tags='text-danger')
			return redirect('car:consultar')

		print(bal)
		context['bal'] = saldo_token(str(bal),18)
		return render(request, template_name, context)	
	return render(request, template_name, context)
