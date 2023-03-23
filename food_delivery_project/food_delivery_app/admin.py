from django.contrib import admin
from .models import Customer,Restaurant,orders,orderItems,Status,Items,deliveryPersonnel,Address,CustAddress,CustNos,RestAddress,restPhNos,personnelAddr,Reviews,Authenticate,Delivery,payInfo,Payment
# from import_export import resources
# from import_export.admin import ImportExportModelAdmin
# Register your models here.

admin.site.register(Customer)
admin.site.register(Restaurant)
admin.site.register(orders)
admin.site.register(orderItems)
admin.site.register(Status)
admin.site.register(Items)
admin.site.register(deliveryPersonnel)
admin.site.register(Address)
admin.site.register(CustAddress)
admin.site.register(CustNos)
admin.site.register(RestAddress)
admin.site.register(restPhNos)
admin.site.register(personnelAddr)
admin.site.register(Reviews)
admin.site.register(Authenticate)
admin.site.register(Delivery)
admin.site.register(payInfo)
admin.site.register(Payment)