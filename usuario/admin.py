from django.contrib import admin
from .models import Usuario

class UsuarioAdmin(admin.ModelAdmin):
	
	list_display = ['username','date_joined','update_at','is_staff_display']
	search_field = ['name','access']
	exclude = ('password',)

	@admin.display(boolean=True, ordering='is_staff', description='Master')
	def is_staff_display(self, obj):
		value = obj.is_staff
		if value in (True, 1, '1'):
			return True
		if value in (False, 0, '0'):
			return False
		return None

admin.site.register(Usuario,UsuarioAdmin)
