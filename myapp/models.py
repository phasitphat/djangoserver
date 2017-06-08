#!/usr/bin/python
#-*-coding: utf-8 -*
from __future__ import unicode_literals

from django.db import models
from rest_framework import serializers

from django.contrib.auth.models import AbstractUser

# Create your models here.
from django.contrib.auth.models import User


class Customer(models.Model):
    # user = models.ForeignKey(User,default='3', on_delete=models.CASCADE )
    username = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=200, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    gender= models.CharField(max_length=50, blank=True, null=True)
    age = models.CharField(max_length=3, blank=True, null=True)
    tel = models.CharField(max_length=10, blank=True, null=True)
    typeofphone=models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    jobs =models.CharField(max_length=50, blank=True, null=True)
    address=models.CharField(max_length=500, blank=True, null=True)
    postcode=models.CharField(max_length=10, blank=True, null=True)
    def __unicode__(self):
        return u"%s: %s"%(self.id,self.username)

class ContactUs(models.Model):
    # customer_id = models.CharField(max_length=5, blank=True, null=True)
    customer = models.ForeignKey(Customer, blank=True, null=True)
    subject = models.CharField(max_length=50, blank=True, null=True)
    content = models.CharField(max_length=1000, blank=True, null=True)
    def __unicode__(self):
        return u"%s: %s"%(self.id,self.subject)

class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = (
            'id',
            'customer',
            'subject',
            'content',
        )


class CustomerSerializer(serializers.ModelSerializer):

    contactus_set = ContactUsSerializer(many=True,read_only=True)


    class Meta:
        model = Customer
        fields = (
                'id',
                "username",
                "password",
                "first_name",
                "last_name",
                "gender",
                "age",
                "tel",
                "typeofphone",
                "email",
                "jobs",
                "address",
                "postcode",
                "contactus_set",
        )



############## Customer ######################################## Order #################


class Category(models.Model):
    category_name = models.CharField(max_length=20)
    category_detail = models.CharField(max_length=100)
    def __unicode__(self):
        return u"%s: %s"%(self.id,self.category_name)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'category_name',
            'category_detail'
        )

class Product(models.Model):
    category_id = models.ForeignKey(Category, blank=True, null=True)
    product_name = models.CharField(max_length=100, blank=True, null=True)
    product_price = models.CharField(max_length=5, blank=True, null=True)
    product_quantity = models.CharField(max_length=3, blank=True, null=True)
    product_detail = models.CharField(max_length=200, blank=True, null=True)
    product_image = models.ImageField(upload_to='product_images', blank=True, null=True)
    def __unicode__(self):
        return u"%s: %s"%(self.id,self.product_name)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'category_id',
            'product_name',
            'product_price',
            'product_quantity',
            'product_detail',
            'product_image',
        )
        
class NewProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'category_id',
            'product_name',
            'product_price',
            'product_quantity',
            'product_detail',
            'product_image',
        )

class PredictProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'category_id',
            'product_name',
            'product_price',
            'product_quantity',
            'product_detail',
            'product_image',
        )


class RandomProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'category_id',
            'product_name',
            'product_price',
            'product_quantity',
            'product_detail',
            'product_image',
        )

class Order(models.Model):
    customer = models.ForeignKey(Customer, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    tracking = models.CharField(max_length=20,blank=True, null=True)
    status_payment = models.CharField(
        choices=(
            ('1', 'Waiting Payment'),
            ('2', 'Paid'),
            ('3', 'Report Problem'),
            ('4', 'Close'),
            ),
        max_length=20, default='1'
        )
    total_price = models.CharField(max_length=5,blank=True, null=True)
    def __unicode__(self):
        return u"id : %s customer_id : %s"%(self.id,self.customer)

class ProductInOrder(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True)
    customer = models.ForeignKey(Customer, blank=True, null=True)
    order = models.ForeignKey(Order, blank=True, null=True)
    product_name = models.CharField(max_length=30, blank=True, null=True)

    totalprice_per_product = models.CharField(max_length=5, blank=True, null=True) #null true
    status_order = models.CharField(max_length=10, blank=True, null=True)         #null true
    def __unicode__(self):
        return u"%s"%(self.id)

class ProductInOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInOrder
        fields = (
            'id',
            'product',
            'customer',
            'order',
            'product_name',
            'totalprice_per_product',
            'status_order',
        )

class Cart(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True)
    customer = models.ForeignKey(Customer, blank=True, null=True)
    order = models.ForeignKey(Order, blank=True, null=True)
    product_name = models.CharField(max_length=30, blank=True, null=True)
    totalprice_per_product = models.CharField(max_length=5, blank=True, null=True)
    def __unicode__(self):
        return u"%s"%(self.id)

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = (
            'id',
            'product',
            'customer',
            'order',
            'product_name',
            'totalprice_per_product',
        )

class Report(models.Model):
    order = models.ForeignKey(Order, blank=True, null=True)
    customer = models.ForeignKey(Customer, blank=True, null=True)
    content_report = models.CharField(max_length=1000)
    contact = models.CharField(max_length=200,blank=True, null=True)
    def __unicode__(self):
        return u"%s: %s"%(self.id,self.customer)

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = (
            'id',
            'order',
            'customer',
            'contact',
            'content_report',
        )

class Payment(models.Model):
    order = models.ForeignKey(Order, blank=True, null=True)
    customer = models.ForeignKey(Customer, blank=True, null=True)
    payment_owner = models.CharField(max_length=20, blank=True, null=True)
    payment_target = models.CharField(max_length=20, blank=True, null=True)
    payment_datetime = models.CharField(max_length=50, blank=True, null=True)
    customer_name = models.CharField(max_length=50, blank=True, null=True)
    total_price = models.CharField(max_length=50, blank=True, null=True)
    # bill_image = models.ImageField(upload_to="bill_images")
    def __unicode__(self):
        return u"%s"%(self.id)

class PaymentSerializer(serializers.ModelSerializer):

    # payment_target= serializers.CharField(source='get_payment_target_display')
    class Meta:
        model = Payment
        fields = (
            'id',
            'order',
            'customer',
            'payment_owner',
            'payment_target',
            'payment_datetime',
            'customer_name',
            'total_price',
            # 'bill_image',
        )



class OrderSerializer(serializers.ModelSerializer):

    report_set = ReportSerializer(many=True,read_only=True)
    payment_set = PaymentSerializer(many=True,read_only=True)
    productinorder_set = ProductInOrderSerializer(many=True,read_only=True)

    class Meta:
        model = Order
        fields = (
            'id',
            'customer',
            'created_at',
            'tracking',
            'status_payment',
            'total_price',
            'report_set',
            'payment_set',
            'productinorder_set',
        )

############################################################################

