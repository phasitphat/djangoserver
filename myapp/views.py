##restapi
from rest_framework import viewsets
from myapp.models import Customer, CustomerSerializer
# from myapp.models import User, UserSerializer
# from myapp.models import Address, AddressSerializer
# from myapp.models import Phone, PhoneSerializer
from django.http import HttpResponseRedirect, HttpResponse
from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response, render , redirect

from myapp.models import ContactUs, ContactUsSerializer
from myapp.models import Order, OrderSerializer
from myapp.models import Report, ReportSerializer
from myapp.models import Payment, PaymentSerializer
from myapp.models import Category, CategorySerializer
from myapp.models import Product, ProductSerializer, NewProductSerializer,PredictProductSerializer,RandomProductSerializer
from myapp.models import ProductInOrder, ProductInOrderSerializer
from myapp.models import Cart, CartSerializer
from myapp.loaded_pickle import loadForest
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.clickjacking import xframe_options_exempt
from django.forms.models import model_to_dict
# from myapp.predict_image import predictImage

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse,JsonResponse

from django.shortcuts import render
from django.views.generic import View
from random import randint
import json
# from django.db.models import Max

loaded_forest = 0;
x = 0;
i = 0;
sequence = 0
seq = 0

loaded_forest = loadForest()

if(loaded_forest!=0):
    print "Already Load loaded_forest Succecss"
else:
    print "Load loaded_forest Succecss"

def predictImage(img1,img2,num):

    loaded_forest.predict([img1,img2])
    p = loaded_forest.predict_proba([img1,img2])
    c = loaded_forest.classes_
    
    pC = []
    count = 0
    while( count < len( p[0] )):
        pC.append( ( p[0][count] , c[count] ) )
        count += 1
        
    pC.sort(reverse=True,key=lambda tup: tup[0])

    numberOfPic = num

    if(len(pC) >= numberOfPic):
        pC = pC[0:numberOfPic]

    predict_id=[]

    for i in pC:
        predict_id.append(i[1])

    return predict_id

@xframe_options_exempt
@csrf_exempt
def Predict(request):

    global seq
    global sequence

    if request.method == 'POST':

        print "IN POST"

        data = json.loads(request.body)
        sequence = data['sequencelist']
        seq = sequence

        print "sequence : "
        print seq
        print seq[-2]
        print seq[-1]

        x = predictImage(seq[-2],seq[-1],10)
        queryset = Product.objects.all().filter(pk__in=x)
        serializer_class = PredictProductSerializer

        print x
        # print queryset

        return HttpResponse(json.dumps({'status':'ok'}), content_type="application/json")

    elif request.method == 'GET':

        print "IN GET"

        seq = sequence
        x = predictImage(seq[-2],seq[-1],10)
        queryset = Product.objects.all().filter(pk__in=x).values('id','product_image')
        serializer_class = PredictProductSerializer

        print x
        return JsonResponse({"queryset":list(queryset)})

def Orderlist(request):
    order_list = Order.objects.all().order_by('-id')
    return render(request, 'orderlist.html', {'order_list': order_list})

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class NewProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-id')[:10]
    serializer_class = NewProductSerializer

class RandomProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('?')[:10]
    serializer_class = RandomProductSerializer

class PredictProductViewSet(viewsets.ModelViewSet):

    print "Sequence IN ViewSet"
    print seq

    x1=randint(1,227)
    x2=randint(1,227)

    # if(len(seq) == 0):

    seq = [x1,x2]
    x = predictImage(seq[-2],seq[-1],10)
    queryset = Product.objects.all().filter(pk__in=x)
    serializer_class = PredictProductSerializer
    print seq[-2]
    print seq[-1]
    print x1
    print x2
    print x
    print queryset


class ProductInOrderViewSet(viewsets.ModelViewSet):
    queryset = ProductInOrder.objects.all()
    serializer_class = ProductInOrderSerializer

def Home(request):
    order_list = Order.objects.all().order_by('-id')
    return render(request, 'home.html', {'order_list': order_list})

def WaitingPayment(request):
    order_list = Order.objects.all().order_by('-id')
    return render(request, 'waitingpayment.html', {'order_list': order_list})

def Paid(request):
    order_list = Order.objects.all().order_by('-id')
    return render(request, 'paid.html', {'order_list': order_list})

def ReportPayment(request):
    order_list = Order.objects.all().order_by('-id')
    return render(request, 'reportpayment.html', {'order_list': order_list})

def Close(request):
    order_list = Order.objects.all().order_by('-id')
    return render(request, 'close.html', {'order_list': order_list})

def Detail(request, id):
    order_list = Order.objects.all().filter(id=id)
    return render(request, 'detail.html', {'id': id,'order_list': order_list})

def Contact(request):
    contactus_list = ContactUs.objects.all().order_by('-id')
    return render(request, 'contactus.html', {'contactus_list': contactus_list})

def ContactusDetail(request, id):
    contactus_list = ContactUs.objects.all().filter(id=id)
    return render(request, 'contactusdetail.html', {'id': id,'contactus_list': contactus_list})