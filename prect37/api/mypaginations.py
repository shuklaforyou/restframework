from rest_framework.pagination import PageNumberPagination

class MyPageNumberpaginations(PageNumberPagination):
    page_size = 6
    page_query_param = 'p'
    page_size_query_param = 'records'
    max_page_size = 5
    last_page_strings = 'end'
