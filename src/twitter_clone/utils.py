from rest_framework.exceptions import APIException
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

class Pagination(PageNumberPagination):
    page_size = None
    max_page_size = None
    page_size_query_param = "page_size"


class ExceptionUnauthorized401(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_code = "Wrong credentials"


class ExceptionForbidden403(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_code = "Forbidden"


class ExceptionNotFound404(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_code = "does not exist"


class ExceptionBadRequest400(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_code = "does not exist"


class ExceptionConflict409(APIException):
    status_code = 409
    default_code = "Conflict"


class ExceptionServerError500(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_code = "internal server error"


class ExceptionAuthenticationFailed(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_code = "authentication failed"
