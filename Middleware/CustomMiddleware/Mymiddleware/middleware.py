from django.http import HttpResponse

class Vishant:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print('Start',self.middleware_name)
        response=self.get_response(request)
        print('End',self.middleware_name)

class Testmiddleware1(Vishant):
    middleware_name='First Middleware'

class Testmiddleware2(Vishant):
    middleware_name='Second Middleware'

class Testmiddleware1(Vishant):
    middleware_name='Third Middleware'
