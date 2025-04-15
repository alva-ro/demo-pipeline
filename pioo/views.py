from django.http import JsonResponse
from datetime import datetime

def ping(request):
    return JsonResponse({'ping': 'pang', 'date': datetime.now().isoformat()})