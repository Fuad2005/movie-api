from rest_framework.pagination import PageNumberPagination


class StandardPagitation(PageNumberPagination):
    page_size = 5