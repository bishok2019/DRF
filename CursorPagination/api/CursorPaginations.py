# For per View Only
from rest_framework.pagination import CursorPagination

class MyCursorPagination(CursorPagination):
    page_size = 3
    ordering ='-roll'
    cursor_query_param = 'cu'