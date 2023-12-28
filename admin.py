from django.contrib import admin

from result.models import Enquiry
from result.models import Interview
from result.models import Placement

class Saveenquiry (admin.ModelAdmin):
    en=('name','email','phone')
admin.site.register(Enquiry,Saveenquiry)

class Saveplacement (admin.ModelAdmin):
    placem=('candidate','image')
admin.site.register(Placement,Saveplacement)
    
# Register your models here.

class Saveinterview(admin.ModelAdmin):
    interv=('date','description')
admin.site.register(Interview,Saveinterview)
