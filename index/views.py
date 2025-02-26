from django.shortcuts import render

# Indexpage/Homepage
def index(request):
  return render(request,"index.html")