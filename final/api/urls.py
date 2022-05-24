from django.urls import path
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from api.views import my_profile, BookViewSet, JournalViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'journals', JournalViewSet)

urlpatterns = [
    path(r'profile/my', my_profile),
    path(r'login/', obtain_jwt_token),
    path(r'token-refresh/', refresh_jwt_token),

]

urlpatterns += router.urls
