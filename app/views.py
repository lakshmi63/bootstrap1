from django.shortcuts import render

# Create your views here.
def style(request):
    return render(request,'style.html')