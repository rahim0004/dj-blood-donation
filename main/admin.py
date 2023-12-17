from django.contrib import admin
from .models import User, StemCellDonor, SCDonorShippingAddress, SCDonorContactPerson1, SCDonorContactPerson2
# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email']

admin.site.register([StemCellDonor, SCDonorShippingAddress, SCDonorContactPerson1, SCDonorContactPerson2])