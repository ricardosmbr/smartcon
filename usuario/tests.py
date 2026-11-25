from unittest.mock import patch
from types import SimpleNamespace

from django.contrib import admin
from django.test import SimpleTestCase

from .admin import UsuarioAdmin
from .forms import PasswordResetForm
from .models import Usuario


class PasswordResetFormTests(SimpleTestCase):

	@patch('usuario.forms.User.objects.filter')
	def test_duplicate_email_is_rejected(self, filter_users):
		filter_users.return_value.count.return_value = 2

		form = PasswordResetForm(data={'email': 'duplicado@example.com'})

		self.assertFalse(form.is_valid())
		self.assertIn(
			'Mais de um usuário foi encontrado com este e-mail.',
			form.errors['email'][0],
		)


class UsuarioAdminTests(SimpleTestCase):

	def test_staff_display_normalizes_database_boolean_strings(self):
		model_admin = UsuarioAdmin(Usuario, admin.site)

		self.assertIs(model_admin.is_staff_display(SimpleNamespace(is_staff='1')), True)
		self.assertIs(model_admin.is_staff_display(SimpleNamespace(is_staff='0')), False)
