from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'runder_app/index.html')

def test(request):
    return render(request, 'runder_app/test.html')