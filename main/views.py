from django.http import HttpResponse, HttpRequest
from datetime import datetime

def home(request: HttpRequest):
    return HttpResponse(f'''<h1>Hello, {request.user.email}</h1>''')
