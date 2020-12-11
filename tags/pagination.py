from rest_framework.pagination import PageNumberPagination

class MyPaginationClass(PageNumberPagination):
<<<<<<< Updated upstream
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 5
=======
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 100
>>>>>>> Stashed changes
