from django.shortcuts import render

# Create your views here.
def index(req):
    title = "My Blog"
    return render(req, "home.html", {"title": title, "body": "How are you?"})
