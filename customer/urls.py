from django.urls import path
from customer import views

urlpatterns=[
    path("register/",views.SignUpView.as_view(),name="signup"),
    path("",views.SignInView.as_view(),name="signin"),
    path("index",views.IndexView.as_view(),name="home"),
    path("products/<int:id>",views.ProductDetailView.as_view(),name="product-detail"),
    path("products/<int:id>/carts/add",views.AddtoCartView.as_view(),name="cart-add"),
    path("customer/carts/list",views.CartlistView.as_view(),name="cart-list"),
    path("carts/<int:id>/change",views.CartRemoveView.as_view(),name="cart-change"),
    path("orders/add/<int:id>",views.MakeOrderView.as_view(),name="create-order"),
    path("orders/list",views.OrderlistView.as_view(),name="order-list"),
    path("order/cancel/<int:id>",views.ordercancelView.as_view(),name="order-cancel"),
    path("discount",views.DiscountProductsView.as_view(),name="offers-list"),
    path("reviews/<int:id>/add",views.ReviewCreateView.as_view(),name="review-add"),
    path("logout",views.signout_view,name="signout"),
]