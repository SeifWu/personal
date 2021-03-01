from django.contrib.auth.models import User, Group
from django.http import HttpResponse, Http404
from rest_framework import viewsets, status
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from app.common.utils.pagination import CustomPagination
from seen.models import Category
from seen.serializers import UserSerializer, GroupSerializer, CategorySerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request):
        queryset = self.get_queryset()

        # 分页
        page_obj = CustomPagination(request=request)
        # print(page_obj.get_page_size(request=request))
        page_list = page_obj.paginate_queryset(queryset=queryset, request=request, view=self)

        serializer = CategorySerializer(page_list, many=True)

        return page_obj.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetail(APIView):
    @staticmethod
    def get_object(pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Http404

    def get(self, request, pk):
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk):
        category = self.get_object(pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        category = self.get_object(pk)
        category.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
