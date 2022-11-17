from django.http import HttpResponse
from django.views import View

class HelloView(View):
    
    def get(self, request, *args, **kwargs):
        name = self.request.GET.get('name')
        message = self.request.GET.get('message')
        return HttpResponse(f"Hello {name}! {message}!")