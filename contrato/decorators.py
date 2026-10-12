from functools import wraps

from django.shortcuts import get_object_or_404

from .models import Contrato, ContratToken


def permition_conrequired(view_func):
	@wraps(view_func)
	def _wrapper(request, *args, **kwargs):
		contracts = Contrato.objects.select_related('id_cliente')
		if not request.user.is_staff:
			contracts = contracts.filter(id_cliente__id_usuario=request.user)
		contrato = get_object_or_404(contracts, pk=kwargs['pk'])
		request.contrato = contrato
		return view_func(request, *args, **kwargs)
	return _wrapper


def permition_tokenrequired(view_func):
	@wraps(view_func)
	def _wrapper(request, *args, **kwargs):
		tokens = ContratToken.objects.select_related('id_contrato__id_cliente')
		if not request.user.is_staff:
			tokens = tokens.filter(id_contrato__id_cliente__id_usuario=request.user)
		token = get_object_or_404(tokens, pk=kwargs['pk'])
		request.token = token
		request.contrato = token.id_contrato
		return view_func(request, *args, **kwargs)
	return _wrapper
