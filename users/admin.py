from django.contrib import admin
from django.contrib.auth.hashers import make_password
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if 'password' in form.changed_data or not change:
            raw_password = form.cleaned_data.get('password')
            obj.password = make_password(raw_password)
        super().save_model(request, obj, form, change)
