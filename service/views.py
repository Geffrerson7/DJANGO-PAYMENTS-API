from django.shortcuts import render
from .serializer import ServiceSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .pagination import StandardResultsSetPagination
from .models import Service


class ServiceUserViewSet(viewsets.ModelViewSet):

    queryset = Service.objects.all().order_by("id")
    serializer_class = ServiceSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAuthenticated]
    http_method_names = ["get"]
    throttle_scope = "user-service"


class ServiceAdminViewSet(viewsets.ModelViewSet):

    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAdminUser]
