from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from orders.views import OrderViewSet

router = routers.SimpleRouter()
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url('^api/v1/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls'))
]

