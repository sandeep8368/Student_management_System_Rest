from django.urls import path,include
from app.views import studentViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'student',studentViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
