import datetime
from datetime import timezone


class LogIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR', 'Noma’lum IP')
        now = datetime.datetime.now()
        print(f"[{now}] So‘rov IP: {ip}")

        response = self.get_response(request)
        return response


class UserAgentMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        now = timezone.now()
        user_agent = request.headers.get('user-agent')
        print(f"User Agent: {user_agent}")

        response = self.get_response(request)
        return response

