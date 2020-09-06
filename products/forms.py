from django import forms
from .models import Product, ProductComment
from tinymce import widgets

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = (
            'title',
            'producer',
            'price',
            'category',
            'discount_price',
            'product_image',
            'stock',
            'description',
            'minimum_order',
            'packing',
            'payment_type',
            'shipping',
            'origin',
            'made_in',
            'delivery',
            'samples',
            'remarks',

        )




class TinyMCEWidget(widgets.TinyMCE):
    def use_required_attribute(self, *args):
        return False


class ProductCommentForm(forms.ModelForm):
    content = forms.CharField()

    class Meta:
        model = ProductComment
        fields = ('content',)