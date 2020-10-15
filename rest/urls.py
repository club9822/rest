"""rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from customuser.views import UserViewSet,UserProfileView
from product.views import ProductViewSet, ProductCategoryViewSet
# from exam.views import ExamsViewSet
from exam.views import ExamsViewSet, QuestionViewSet, ChoiceViewSet, AnswerViewSet
from order.views import CartViewSet, OrderViewSet, DiscountViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'carts', CartViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'discounts', DiscountViewSet)
router.register(r'users', UserViewSet)
# router.register('users/<int:pk>/', UserProfile)
router.register(r'products', ProductViewSet)
router.register(r'product-category', ProductCategoryViewSet)
router.register(r'exams', ExamsViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'choices', ChoiceViewSet)
router.register(r'answers', AnswerViewSet)
urlpatterns = [
    path('api/v1/users/profile/<int:pk>/', UserProfileView.as_view()),
    # path('customuser/profile/<int:pk>/', UserProfileView.as_view()),
    path('admin/', admin.site.urls),
    url(r'^api/v1/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    url(r'^api-auth/', include('rest_framework.urls')),

]
# urlpatterns = format_suffix_patterns(urlpatterns)
