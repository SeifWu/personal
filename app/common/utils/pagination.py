from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPagination(PageNumberPagination):
    def __init__(self, request):
        self.page_size_query_param = 'pageSize'
        self.page_query_param = 'current'
        self.page_size = self.get_page_size(request=request)
        self.max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'pageSize': self.page_size,
            'current': self.page.number,
            'data': data,
        })
