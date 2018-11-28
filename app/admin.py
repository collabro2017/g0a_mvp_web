from django.contrib import admin
from app.models import EmailDatabase

admin.AdminSite.site_header = "Administrator Site"


# Register your models here.

admin.site.register(EmailDatabase)

