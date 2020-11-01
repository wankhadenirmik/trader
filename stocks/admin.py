from django.contrib import admin
from .models import Client
from .models import Company, Company_assets ,Demat ,IPO ,Transaction,Market
# Register your models here.
admin.site.register(Client)
admin.site.register(Company)
admin.site.register(Company_assets)
admin.site.register(Demat)
admin.site.register(IPO)
admin.site.register(Transaction)
admin.site.register(Market)
