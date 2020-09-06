from django import forms
from rest_framework import serializers
from .models import Document

class SubscriptionForm(forms.Form):
    email = forms.EmailField(required=True)


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('document',)

class DocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Document
        fields = ('id', 'document',)