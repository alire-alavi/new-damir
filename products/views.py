import json

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework import viewsets, status, generics, mixins
from .models import Product, Rating, ProductComment
from .serializers import ProductSerializer, ProductCommentSerializer, ProductDetailSerializer, RatingSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view


from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.renderers import JSONRenderer

from django.shortcuts import render, redirect, reverse
from django.db.models import Q
from django.views import View
from django.core.exceptions import ObjectDoesNotExist

from .forms import ProductCommentForm

from .models import Product, ProductComment
from .serializers import ProductSerializer, ProductDetailSerializer, ProductCommentSerializer
from .permissions import IsProducer, IsOwnerOrReadOnly

from categories.models import Category
from users.serializers import UserSerializer
from users.models import ProducerProfile
"""
################################################################
            ##          ############         ##
           ## #         ##        ##         ##
          ##   #        ##        ##         ##
         ##     #       ##        ##         ##
        ## # # # #      ############         ##
       ##         #     ##                   ##
      ##           #    ##                   ##
     ##             #   ##                   ##
##################################################################
"""
class ProductListView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class ProductDetailView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'slug'

class ProductRUDView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly, IsProducer    )
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()
    lookup_field = 'slug'


class ProducersProductListView(ListAPIView):
    # permission_classes = (IsAuthenticated,)
    serializer_class = ProductDetailSerializer

    def get_queryset(self, request, *args, **kwargs):
        queryset = Product.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(user__username=username)
        return queryset

class ProducerProductPublicListView(ListAPIView):
    permission_classes = (AllowAny, )
    serializer_class = ProductSerializer

    def get_queryset(self):
        company = self.kwargs['company_name']
        return Product.objects.filter(producer__company_name=company)


class ProductCreationView(CreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()


    def perform_create(self, serializer):
        producer = ProducerProfile.objects.get(user=self.request.user)
        serializer.save(producer=producer)




@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        # 'users': reverse('user-list', request=request, format=format),
        'products': reverse('product-list', request=request, format=format),
        # 'comments' : reverse('product-comments', request=request, format=format)
    })

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    @action(methods=['POST'], detail=True)
    def rate_product(self, request, pk=None):
        if 'stars' in request.data:
            product = Product.objects.get(id=pk)
            stars = request.data['stars']
            user = request.user
            try:
                rating = Rating.objects.get(user=user.id, product=product.id)
                rating.stars = stars
                rating.save()

                serializer = RatingSerializer(rating, many=True)
                response = {'message': 'rating has been updated', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)
            except:
                rating = Rating.objects.create(user=user, product=product, stars=stars)
                serializer = RatingSerializer(rating, many=False)
                response = {'message': 'rating created', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)


        else:
            response = {'message': 'Please enter stars for the rating'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['POST'], detail=True)
    def comment_on_product(self, request, pk=None, name=None):
        if 'content' in request.data:
            product = Product.objects.get(id=pk, title=name)
            content = request.data['content']
            user = request.user
            try:
                comment = ProductComment.objects.get(user=user.id, product=product.id, is_confirmed=True)
                comment.content = content
                comment.is_confirmed = False
                comment.save()

                serializer = ProductCommentSerializer(comment, many=True)
                response = {"message" : "comment edited wait for the team to revise it",
                            "result" : serializer.data}
                return Response(response, status=status.HTTP_201_CREATED)

            except:
                comment = ProductComment.objects.create(user=user, product=product,
                                                        content=content , is_confirmed=False)
                serializer = ProductCommentSerializer(comment, many=False)
                response = {"message" : "comment posted wait for our to team to review it",
                            'result' : serializer.data}
                return Response(response, status=status.HTTP_200_OK)

        else:
            responser = {'message' : 'please fill the required fields' }
            return Response(responser, status=status.HTTP_400_BAD_REQUEST)


    def perform_create(self, serializer):
        serializer.save(producer=self.request.user)


class ProductsByCategory(generics.ListAPIView):
    serializer_class = ProductDetailSerializer
    permission_classes = (AllowAny,)


    def get_queryset(self):
        category = self.kwargs['category']
        queryset = Product.objects.all()

def is_valid_queryparam(param):
    return param != '' and param is not None


def filter(request):
    qs = Product.objects.all()
    categorise = Category.objects.all()
    title_contains_query = request.GET.get('title_contains')
    title_or_category_query = request.GET.get('title_or_category')
    price_min = request.GET.get('price_min')
    price_max = request.GET.get('price_max')
    category = request.GET.get('category')

    if is_valid_queryparam(title_contains_query):
        qs = qs.filter(title__icontains=title_contains_query)

    elif is_valid_queryparam(title_or_category_query):
        qs = qs.filter(Q(title__icontains=title_or_category_query)
                       | Q(category__title__icontains=title_or_category_query)
                       ).distinct()

    if is_valid_queryparam(price_min):
        qs = qs.filter(price__gte=price_min)

    if is_valid_queryparam(price_max):
        qs = qs.filter(price__lt=price_max)

    if is_valid_queryparam(category) and category != 'Choose...':
        qs = qs.filter(category__title=category)

    return qs


class VueFilterView(generics.ListAPIView):
    serializer_class = ProductDetailSerializer

    def get_queryset(self):
        qs = filter(self.request)
        return qs
"""
END OF:
################################################################
            ##          ############         ##
           ## #         ##        ##         ##
          ##   #        ##        ##         ##
         ##     #       ##        ##         ##
        ## # # # #      ############         ##
       ##         #     ##                   ##
      ##           #    ##                   ##
     ##             #   ##                   ##
##################################################################
"""

def products_list_view(request):
    queryset = Product.objects.all()
    sered_data = ProductDetailSerializer(queryset, many=True).data
    json_string = json.dumps(sered_data)
    return render(request, 'views/products.html', {'products': json_string})


class ProductDetailView(View):
    form = ProductCommentForm()

    def get(self, request, slug, *args, **kwargs):
        try:
            form = ProductCommentForm
            queryset = Product.objects.get(slug=slug)
            serialized_q_set = ProductDetailSerializer(queryset).data
            json_product = json.dumps(serialized_q_set)
            context = {
                'product': json_product,
                'object' : queryset,
            }
            return render(request, 'views/product.html', context)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request, slug, *args, **kwargs):
        form = ProductCommentForm(request.POST or None)
        if form.is_valid():
            product = Product.objects.get(slug=slug)
            form.instance.user = self.request.user
            form.instance.product = product
            # form.instance.content = json.loads(request.POST['content'])
            form.instance.content = request.POST['content']
            form.save()
            return redirect(reverse("products:product_detail", kwargs={'slug': slug}))
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


def product_detail_view(request, slug):
    product = Product.objects.get(slug=slug)
    sered_data = ProductDetailSerializer(product).data
    json_string = json.dumps(sered_data)
    return render(request, 'views/product.html', {'product': json_string})

def user_panel_view(request):
    serialized_user = UserSerializer(request.user).data
    producer = ProducerProfile.objects.get(user=request.user)
    user_products = Product.objects.filter(producer=producer)
    serialized_products = ProductDetailSerializer(user_products, many=True).data
    json_products = json.dumps(serialized_products)
    json_user_profile_data = json.dumps(serialized_user)
    context = {
        'user': json_user_profile_data,
        'products': json_products,
    }
    return render(request, 'views/userPanel.html', context)




def product_paginated(request, page):
    page_number = page
    products = Product.objects.all()
    products_quantity = Product.objects.all().count()
    products_pages = products_quantity/12
    first_obj = 12*(page_number-1)
    last_obj = 12*(page)

    page_products = products[first_obj:last_obj]
    serialized_products = ProductDetailSerializer(page_products, many=True).data
    json_products_data = json.dumps(serialized_products)
    previous_page = page - 1 
    next_page = page + 1
    json_page_data = f'[{{ "previous_page" : {previous_page}, "next_page" : {next_page} }}]'

    context = {
        'products' : json_products_data,
        'pageData' : json_page_data,
    }
    return render(request, 'views/products.html', context)