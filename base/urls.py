from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
  path('', views.home),  
  # path('detail/<int:pk>', views.detail,name='detail')
  path('advocates/<str:username>/', views.advocate_details, name='advocate-detail'),
  path('endpoints/', views.endpoints),
  path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  path('advocates/', views.advocate_list, name="advocates"),
  path('advocates/<str:username>/', views.advocate_detail, name="advocate-details"),
  path('companies/', views.companies_list),  
   
  # path('', views.home),
  # path('movies/', views.movies),
  # path('movies/<int:id>', views.detail),
  
  # path('', views.EndpointsHome.as_view()),
  # path('advocates/', views.AdvocateList.as_view(), name="advocates"),
  # path('advocates/<str:username>/', views.AdvocateDetail.as_view()),  
]
urlpatterns = format_suffix_patterns(urlpatterns)