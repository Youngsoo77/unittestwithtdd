from django.shortcuts import render
# from django.http import HttpResponse


# Create your views here.
def home_page(request):
    # return HttpResponse('<html><title>Hello world Unittest with TDD</title></html>')
    return render(request, 'home.html')
