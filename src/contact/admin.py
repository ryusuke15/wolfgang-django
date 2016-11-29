from django.contrib import admin

# Register your models here.
from .models import Contact, Video_link, Product
class ContactAdmin(admin.ModelAdmin):
    list_display = ["__unicode__","email","received","message"]
    class Meta:
            model = Contact

class Video_linkAdmin(admin.ModelAdmin):
    list_display =["__unicode__","videoId"]
    list_editable=["videoId"]
    class Meta:
            model = Video_link

class ProductAdmin(admin.ModelAdmin):
    list_display = ["__unicode__","price","link","admin_image"]
    list_editable = ["price","link"]
    class Meta:
        model = Product

admin.site.register(Contact, ContactAdmin)
admin.site.register(Video_link, Video_linkAdmin)
admin.site.register(Product, ProductAdmin)
