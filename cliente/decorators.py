from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from cliente.models import Cliente

def permition_required(view_func):
	def _wrapper(request, *args,**kwargs):
		pk = kwargs['pk']
		cliente = get_object_or_404(Cliente,pk=pk)
		has_permition = request.user.is_staff
		if not has_permition:
			try:
				cliente = Cliente.objects.get(
					id_usuario=request.user.pk,
					pk=pk
				)
			except cliente.DoesNotExist:
				messages.error(request,'Desculpe, mas voce não tem permissão',extra_tags='text-danger')
			else:
				has_permition = True

		if not has_permition:
			return redirect('cli:cliente')
			
		request.cliente = cliente
		return view_func(request, *args,**kwargs)
	return _wrapper