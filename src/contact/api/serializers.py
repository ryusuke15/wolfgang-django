from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from rest_framework import serializers

from contact.models import Contact, Product, Video_link
import datetime
#Create Contact 
class ContactCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=120)
    email = serializers.EmailField()
    message = serializers.CharField()
    #Save Contact
    def create(self, validated_data):
        #Email Function         
        form_name = self.data.get('name')
        form_email = self.data.get('email')
        form_message = self.data.get('message')
        subject = 'Contact Notification from'+ ' '+ form_name
        from_email = settings.EMAIL_HOST_USER
        body  = 'Name: %s<br/>Contact: %s<br/>Message: %s<br/>'%(form_name, form_email,form_message)
        to = 'info@wolfgangdouglas.com'    
        html_content = body
        text_content = 'This is an example'
        msg = EmailMultiAlternatives(
            subject, 
            text_content, 
            from_email, 
            [to],
            )
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return Contact.objects.create(**validated_data)

class Video_linkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video_link
        fields = ('__all__')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('__all__')
