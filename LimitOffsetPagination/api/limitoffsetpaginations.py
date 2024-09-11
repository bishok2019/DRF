from rest_framework.pagination import LimitOffsetPagination

class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 5
    # limit_query_param ='mylimit'
    # offset_query_param = 'myoffset'
    # max_limit = 10
    pass
# http://127.0.0.1:8000/studentapi/?limit=4
# http://127.0.0.1:8000/studentapi/?limit=8&offset=10