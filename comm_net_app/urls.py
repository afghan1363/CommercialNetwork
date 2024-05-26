from django.urls import path
from comm_net_app import views

app_name = 'comm_net_app'

urlpatterns = [
    path('link/create/', views.OrganizationCreateAPIView.as_view()),
    path('link/<int:pk>/retrieve/', views.OrganizationRetrieveAPIView.as_view()),
    path('link/list/', views.OrganizationListAPIView.as_view()),
    path('link/<int:pk>/update/', views.OrganizationUpdateAPIView.as_view()),
    path('link/<int:pk>/destroy/', views.OrganizationDestroyAPIView.as_view()),
    # path('product/create')
]
