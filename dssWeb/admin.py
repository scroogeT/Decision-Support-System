from django.contrib import admin
from import_export import resources
from leaflet.admin import LeafletGeoAdmin
from .models import *
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

#import-export resource
class customerResource(resources.ModelResource):
    class Meta:
        model = customer
        #to eplicitly assign fields to be exported
        #fields = ('id','address', 'location')
@admin.register(importedOrders)
class importCustAdmin(ImportExportModelAdmin):
    pass
    #https://simpleisbetterthancomplex.com/packages/2016/08/11/django-import-export.html

'''
                importing Data

>>> import tablib
>>> from import_export import resources
>>> from core.models import Book
>>> book_resource = resources.modelresource_factory(model=Book)()
>>> dataset = tablib.Dataset(['', 'New book'], headers=['id', 'name'])
>>> result = book_resource.import_data(dataset, dry_run=True)
>>> print result.has_errors()
False
>>> result = book_resource.import_data(dataset, dry_run=False)
'''


'''
                    exporting data

from dssWeb.admin import customerResource
dataset = customerResource().export()
print (dataset.csv)
id,user,address,location
1,1,,SRID=4326;POINT (31.025390625 -17.896728515625)
2,2,,SRID=4326;POINT (29.8333740234375 -19.45623359601801)

'''

class customerAdmin(LeafletGeoAdmin):
    pass

# Register your models here.
admin.site.register(truck)
admin.site.register(consignment)
admin.site.register(driver)
admin.site.register(customer, customerAdmin)
admin.site.register(distributionPoint)
admin.site.register(deliveryState)
#admin.site.register(importedOrders, importCustAdmin)


