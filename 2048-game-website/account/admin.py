from django.contrib import admin
from .models import MyUser

# Register your models here.
@admin.register(MyUser)
class ActiveUser(admin.ModelAdmin):
	list_display=['first_name','last_name','is_active','is_superuser','username']
	search_fields=['user_name','first_name','email']
	actions_on_bottom=True
	date_hierarchy='date_joined'
