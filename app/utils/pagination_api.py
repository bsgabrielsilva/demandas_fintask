from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class PaginacaoPersonalizada(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'items_size'
    max_page_size = 10

    def get_paginated_response(self, data):
        return Response({'count': self.page.paginator.count,
                         'next': self.page.next_page_number() if self.page.has_next() else None,
                         'previous':  self.page.previous_page_number() if self.page.has_previous() else None,
                         'current': self.page.number,
                         'query_param': "?page=",
                         'page_size_query': self.page_size_query_param,
                         'page_size': self.page_size,
                         'total_pages': self.page.paginator.num_pages,
                         'results': data})