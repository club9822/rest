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

from user.views import UserViewSet, UserProfile
from product.views import ProductViewSet, ProductCategoryViewSet
from exam.views import ExamViewSet, QuestionViewSet, ChoiceViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'products', ProductViewSet)
router.register(r'product-category', ProductCategoryViewSet)
router.register(r'exams', ExamViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'choices', ChoiceViewSet)

urlpatterns = [
    # path('accounts/profile/', UserProfile.as_view()),
    path('user/profile/<int:pk>/', UserProfile.as_view()),
    path('admin/', admin.site.urls),
    url(r'^api/v1/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
# urlpatterns = format_suffix_patterns(urlpatterns)
