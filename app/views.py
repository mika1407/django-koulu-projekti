from django.shortcuts import render

# Create your views here.
def landingview(request):
  return render (request, "landingpage.html")
