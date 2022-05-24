from django.http import HttpResponse
from rest_framework import viewsets, status, mixins
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.models import User, Book, Journal
from api.permissions import IsAdmin
from api.serializers import UserBaseSerializer, BookSerializer, JournalSerializer


@api_view(['GET'])
def my_profile(request):
    if request.user.id:
        user = User.objects.get(id=request.user.id)
        serializer = UserBaseSerializer(user)
        return Response(serializer.data)
    else:
        return HttpResponse(status=status.HTTP_401_UNAUTHORIZED)


class BookViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin
):
    queryset = Book.objects.all()
    permission_classes = [IsAdmin]
    serializer_class = BookSerializer


class JournalViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin
):
    queryset = Journal.objects.all()
    permission_classes = [IsAdmin]
    serializer_class = JournalSerializer
