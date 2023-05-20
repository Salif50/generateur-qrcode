from django.shortcuts import render

def home(request):

    return render(request, 'cryptage/index.html')