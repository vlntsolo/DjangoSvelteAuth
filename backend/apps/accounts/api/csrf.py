import logging

from apps.accounts.api.router import accounts_router
from apps.core.schemas import BaseResponseSchema
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie


@accounts_router.post("/auth/csrf-token")
@ensure_csrf_cookie
@csrf_exempt
def get_csrf_token(request):
    logging.debug("[ACCOUNTS.API.CSRF] get_csrf_token()")

    # Log the request method and the request headers to check for CORS issues
    logging.debug(f"\tRequest Method: {request.method}")
    logging.debug(f"\tRequest Headers: {dict(request.headers)}")

    # Log the CSRF cookie in the response
    csrf_cookie = request.COOKIES.get("csrftoken")
    logging.debug(f"\tCSRF Cookie: {csrf_cookie}")

    return HttpResponse()


@accounts_router.post("/auth/csrf-token/validate", response={200: BaseResponseSchema})
def validate_csrf_token(request):
    logging.debug("[ACCOUNTS.API.CSRF] validate_csrf_token()")

    # Log request headers for CORS debug information
    headers = dict(request.headers)
    logging.debug(f"\tRequest Headers: {dict(request.headers)}")

    csrf_token_header = request.META.get("HTTP_X_CSRFTOKEN")
    logging.debug(f"\tCSRF Token (Header): {csrf_token_header}")

    # Log CSRF cookie to compare against the CSRF token in the request
    csrf_cookie = request.COOKIES.get("csrftoken")
    logging.debug(f"\tCSRF Cookie: {csrf_cookie}")

    # Check if the CSRF token matches the cookie and log the result
    if csrf_token_header == csrf_cookie:
        message = "CSRF token is valid and matches the CSRF cookie."
        logging.debug(f"\t{message}")
    else:
        message = "CSRF token is INVALID or DOES NOT match the CSRF cookie."
        logging.debug(f"\t{message}")

    return 200, BaseResponseSchema(
        success=True,
        message=message,
        headers=headers,  
        csrf_cookie=csrf_cookie,
        http_x_csrftoken=csrf_token_header,
    ) # type: ignore


@accounts_router.post("/auth/csrf-token/validate-csrf-exempt", response={200: BaseResponseSchema})
@csrf_exempt
def validate_csrf_token_csrf_exempt(request):
    logging.debug("[ACCOUNTS.API.CSRF] validate_csrf_token_csrf_exempt()")

    # Log request headers for CORS debug information
    headers = dict(request.headers)
    logging.debug(f"\tRequest Headers: {dict(request.headers)}")

    csrf_token_header = request.META.get("HTTP_X_CSRFTOKEN")
    logging.debug(f"\tCSRF Token (Header): {csrf_token_header}")

    # Log CSRF cookie to compare against the CSRF token in the request
    csrf_cookie = request.COOKIES.get("csrftoken")
    logging.debug(f"\tCSRF Cookie: {csrf_cookie}")

    # Check if the CSRF token matches the cookie and log the result
    if csrf_token_header == csrf_cookie:
        message = "CSRF token is valid and matches the CSRF cookie."
        logging.debug(f"\t{message}")
    else:
        message = "CSRF token is INVALID or DOES NOT match the CSRF cookie."
        logging.debug(f"\t{message}")

    return 200, BaseResponseSchema(
        success=True,
        message=message,
        headers=headers,  
        csrf_cookie=csrf_cookie,
        http_x_csrftoken=csrf_token_header,
    ) # type: ignore
