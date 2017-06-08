##restapi
from django.conf.urls import url
from rest_framework import routers
from myapp.views import CartViewSet, CustomerViewSet, ContactUsViewSet, OrderViewSet, ReportViewSet, PaymentViewSet, CategoryViewSet, PredictProductViewSet, NewProductViewSet,ProductViewSet, ProductInOrderViewSet ,RandomProductViewSet
from myapp.views import Home,Detail,Predict
from myapp import views

router = routers.DefaultRouter()
router.register(r'customers', CustomerViewSet)
# router.register(r'addresss', AddressViewSet)
router.register(r'contactuss', ContactUsViewSet)
# router.register(r'phones', PhoneViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'reports', ReportViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'categorys', CategoryViewSet)

router.register(r'newproducts', NewProductViewSet)
router.register(r'products', ProductViewSet)
router.register(r'predictproducts', PredictProductViewSet)

# router.register(r'randomproducts', RandomProductViewSet)

router.register(r'productinorders', ProductInOrderViewSet)
router.register(r'carts', CartViewSet)

# router.register(r'predicts', Predict)
# router.register(r'home', Home)
# router.register(r'detail', Detail)

urlpatterns = [
    url(r'^predicts/$', Predict)
]
urlpatterns +=  router.urls