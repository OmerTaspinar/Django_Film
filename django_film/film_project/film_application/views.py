from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")
def film_lists(request):
    return render(request,"film_lists.html")
def film_details(request,film_name):
    return render(request,"film_details.html",{
        "slug":film_name
    })