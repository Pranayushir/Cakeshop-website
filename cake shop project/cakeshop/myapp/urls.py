from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("home/",views.home, name="home"),
    path("contact/",views.contact, name="contact"),
    path("about/",views.about, name="about"),
    path("menu/",views.menu, name="menu"),
    # path('index/',views.index, name="index"),
    path('signup/',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('logout/',views.LogoutPage,name='logout'),
    path('payment/',views.paymentview,name='payment'),
    # path('cart/',views.cart,name='cart'),
    
    path('add_to_cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart_view'),

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

