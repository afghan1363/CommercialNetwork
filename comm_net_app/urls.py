from django.urls import path, include
from comm_net_app.organization_crud.views import OrganizationView
from comm_net_app.products_crud.views import ProductAPIView, All_ProductAPIView
from rest_framework.routers import DefaultRouter

app_name = 'comm_net_app'


org_router = DefaultRouter()
org_router.register(prefix=r"org", viewset=OrganizationView, basename="org")

product_router = DefaultRouter()
product_router.register(prefix=r"prod", viewset=ProductAPIView, basename="prod")

urlpatterns = [
    path("api/", include(org_router.urls)),
    path("api/<int:org_pk>/", include(product_router.urls)),
    path("api/allproduts/", All_ProductAPIView.as_view())
]
