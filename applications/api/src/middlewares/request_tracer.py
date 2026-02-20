from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response


class RequestTracerMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next) -> Response:
        print(f"before call_next: {request.url.path}")
        response = await call_next(request)
        print(f"after call_next: {request.url.path}")
        return response
