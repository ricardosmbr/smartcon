from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterForm(forms.ModelForm):

	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Digite seu Nome'}))
	email = forms.EmailField(label='E-mail',widget=forms.TextInput(attrs={'placeholder':'Digite seu E-mail'}))
	password1 = forms.CharField(label='Senha',widget=forms.PasswordInput)
	password1.widget.attrs.update({'placeholder':'Digite uma Senha'})
	password2 = forms.CharField(label='Confirma senha',widget=forms.PasswordInput)
	password2.widget.attrs.update({'placeholder':'Repita a Senha'})

	def clean_password2(self):
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError(
				'As senhas são diferentes'
			)
		return password2 

	def clean_email(self):
		email= self.cleaned_data['email']
		queryset = User.objects.filter(email=email).exclude(pk=self.instance.pk)
		if queryset.exists():
			raise forms.ValidationError('Email já existe')
		return email


	def save(self,commit=True):
		user = super(RegisterForm, self).save(commit=False)
		user.set_password(self.cleaned_data['password1'])
		if commit:
			user.save()
		return user	

	class Meta:
		model = User
		fields = ['username','email']
			

class EditAccountForm(forms.Form):

	class Meta:
		model = User
		fields = ['username','email','name']