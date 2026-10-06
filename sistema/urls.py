from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from sistema import views

app_name = 'sis'

urlpatterns = [
	path('entrar/',LoginView.as_view(template_name='login.html'), name='login'),
	path('sair/', LogoutView.as_view(next_page='home'), name='logout'),
	path('registro/',views.register ,name='registrar'),
	path('painel/',views.painel ,name='painel'),
	path('ip/',views.ip_cliente ,name='ip_cliente'),
]
