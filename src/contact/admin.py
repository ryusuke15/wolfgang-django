from djangoseo.admin import register_seo_admin
from django.contrib import admin
from contact.seo import MyMetadata


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

register_seo_admin(admin.site, MyMetadata)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Video_link, Video_linkAdmin)
admin.site.register(Product, ProductAdmin)
