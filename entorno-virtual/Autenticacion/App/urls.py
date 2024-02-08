from django.contrib import admin
from django.urls import path, include
from App.views import SigSocial, Products, Products_Category1,   ProductoListCreateView, ProductoListCreateViewDiscontain, OrdersListCreateView
from . import views
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets




from allauth.socialaccount.views import login_error, signup, connections, login_cancelled
# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('router', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('accounts/', include('allauth.urls')),
    path("login/error/", login_error, name="socialaccount_login_error"),
    path("signup/", signup, name="socialaccount_signup"),
    path("connections/", connections, name="socialaccount_connections"),
    path(
        "login/cancelled/",
        login_cancelled,
        name="socialaccount_login_cancelled",
    ),
    path('', views.home, name='home'),
    path("SignupSocial/", SigSocial.as_view(), name="socialaccount_signup"),
    path("Products/", Products, name="products_food"),
    path("Products/Beverages", Products_Category1, name="beverages"),
    path('api/products/',  ProductoListCreateView.as_view(), name='mymodel-list-create'),
    path('api/products/Discontain',  ProductoListCreateViewDiscontain.as_view(), name='mymodel-list-create-Disc'),
    path('api/OrdersRegion',  OrdersListCreateView.as_view(), name='orders-list'),
]

