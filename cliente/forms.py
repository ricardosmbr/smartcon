from django import forms
from sistema.mail import send_mail_template
from .models  import Cliente
from carteira.models import Carteira
from eth_account import Account
from web3 import Web3
import random


class ClienteNovoForm(forms.ModelForm):

	name = forms.CharField(label='Nome',widget=forms.TextInput(attrs={'placeholder':'Digite seu Nome'}))
	name.widget.attrs.update({'size':'25'}) 
	cpf = forms.CharField(label='CPF', required=False, widget=forms.TextInput(attrs={'placeholder':'000.000.000-00'}))
	tel = forms.CharField(label='Telefone', required=False, widget=forms.TextInput(attrs={'placeholder':'(00) 00000-0000','class':'tel'}))

	class Meta:
		model = Cliente
		fields = ['name','cpf','tel']

	def clean_cpf(self):
		return self.cleaned_data.get('cpf') or None

class EditarCliente(forms.ModelForm):

	name = forms.CharField(label='Nome')
	name.widget.attrs.update({'size':'25'}) 
	cpf = forms.CharField(label='CPF', required=False, widget=forms.TextInput(attrs={'class':'cpf'}))
	tel = forms.CharField(label='Telefone', required=False, widget=forms.TextInput(attrs={'class':'tel'}))


	class Meta:
		model = Cliente
		fields = ['name','cpf','tel']

	def clean_cpf(self):
		return self.cleaned_data.get('cpf') or None

class MostrarCliente(forms.ModelForm):

	name = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}))
	name.widget.attrs.update({'size':'25'}) 
	cpf = forms.CharField(label='CPF',widget=forms.TextInput(attrs={'class':'cpf','readonly':'True'}))
	tel = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}))


	class Meta:
		model = Cliente
		fields = ['name','cpf','tel']

