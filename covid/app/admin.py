from django.contrib import admin
from .models import User_Attributes,Hospital,Request
admin.site.register(User_Attributes)
admin.site.register(Hospital)
admin.site.register(Request)