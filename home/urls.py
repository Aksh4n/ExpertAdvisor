from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.home, name="home"),
    path("contact", views.contact, name="contact"),
    path("product/<int:product_id>/", views.product_detail, name="product_detail"),
    path("register/", views.register_user, name="register"),
    path("login/", views.login_user, name="login"),
    path("logout_user", views.logout_user, name="logout"),
    path("profile/", views.profile, name="profile"),
    path("MQL/", views.MQL, name="MQL"),
    path(
        "password-reset/", auth_views.PasswordResetView.as_view(), name="password_reset"
    ),
    path(
        "password-reset/done/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path("updateprofile/", views.updateprofile, name="updateprofile"),
    path("ideas", views.ideas, name="ideas"),
    #path('initiate-payment/', views.initiate_payment, name='initiate_payment'),
    #path('get-product-details/<int:product_id>/', views.get_product_details, name='get_product_details'),
    #path('payment-callback/', views.payment_callback, name='payment_callback'),
]
