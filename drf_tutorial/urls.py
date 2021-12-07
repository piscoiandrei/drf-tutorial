from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from quickstartapp import views as qviews

router = routers.DefaultRouter()
router.register(r'users', qviews.UserViewSet)
router.register(r'groups', qviews.GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework')),
    path('snippets/', include('snippets.urls')),
]
