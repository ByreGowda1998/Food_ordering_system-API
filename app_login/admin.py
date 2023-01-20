from django.contrib import admin

# Register your models here.
from  app_login.models import User,Contact,Profile
# Register your models here.
admin.site.register(User)
admin.site.register(Contact)
admin.site.register(Profile)