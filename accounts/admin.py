from django.contrib import admin

from .models import BankAccountType, User, UserAddress, UserBankAccount


class MyAdmin1(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'account_no')
    

class MyAdmin2(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'user')

class MyAdmin3(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'account_no')

admin.site.register(BankAccountType)
admin.site.register(User,MyAdmin1)
admin.site.register(UserAddress,MyAdmin2)
admin.site.register(UserBankAccount,MyAdmin3)
