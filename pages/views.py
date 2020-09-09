import json
import os

from django.contrib.auth import authenticate, login
from django.http import QueryDict
from django.views.generic import View
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.http.response import HttpResponseBadRequest, HttpResponse, JsonResponse
from website.settings import BASE_DIR
from django.core.files.uploadhandler import FileUploadHandler
# from django.


#COMPONENTS
from products.models import Product
from products.serializers import ProductDetailSerializer, ProductSerializer

from categories.models import Category, MainCategory
from categories.serializers import CategorySerializer, MainCategorySerializer

from blog.models import  Post
from blog.serializers import PostSerializer

from .forms import SubscriptionForm, DocumentForm, DocumentSerializer
from .models import NewsTellerEmails, Document

class FrontendRenderView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pages/front-end-render.html', {})


class IndexView(View):

    def get(self, *args, **kwargs):
        try:
            products_list = Product.objects.all()
            categories = Category.objects.all()
            main_categories = MainCategory.objects.all()
            posts = Post.objects.all()[:3]
            categories_ser = CategorySerializer(categories, many=True).data
            main_categories_ser = MainCategorySerializer(main_categories, many=True).data
            post_ser = PostSerializer(posts, many=True).data
            categories_ser_json = json.dumps(categories_ser)
            main_categories_ser_json =json.dumps(main_categories_ser)
            post_ser_json = json.dumps(post_ser)

            paginator = Paginator(products_list, 12)
            page = self.request.GET.get('page')

            try:
                products = paginator.page(page)
            except PageNotAnInteger:
                products = paginator.page(1)

            except EmptyPage:
                products = paginator.page(paginator.num_pages)

            products_ser = ProductDetailSerializer(products, many=True).data
            products_ser_json = json.dumps(products_ser)


            context = {
                'products' : products_ser_json,
                'categories' : categories_ser_json,
                'main_categories' : main_categories_ser_json,
                'posts' : post_ser_json,
                'page' : page,
            }
            return render(self.request, "views/index.html", context)
        except ObjectDoesNotExist:
            message = messages.ERROR("سرور ترکیده")
            return HttpResponseBadRequest("Object Does Not Exist")


    def post(self, request, *args, **kwargs):
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            email = request.POST['email']
            if request.user.is_authenticated():
                news_teller, created = NewsTellerEmails.objects.get_or_create(
                    user=request.user,
                    email=email
                )
            else:
                news_teller = NewsTellerEmails.objects.create(
                    email=email
                )
            return redirect("/")

        else:
            message = messages.ERROR("لطفا ایمیل معتبر وارد کنید")
            return HttpResponseBadRequest("form")



def test(request):
    if request.method == 'POST':
        files = request.FILES
        single = files.getlist('file')[0]
        file_name = single.name
        document = Document.objects.create(
            name=file_name,
            document=single,
        )
        location = "location"
        path = f"images/documents/{file_name}"
        context = { 'response' : f'{{location: "{path}"}}'}
        json_context = json.dumps(context)
        render(request, 'views/userPanel.html',json_context)
        return HttpResponse('Done')
    return HttpResponse("this is get")