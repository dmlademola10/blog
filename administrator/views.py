from django.shortcuts import render

# Create your views here.
def index(req):
    title = "My Blog(Admin)"
    return render(req, "admin/login.html", {"title": title})


def home(req):
    title = "My Blog - Home(Admin)"
    return render(req, "home.html", {"title": title, "body": "How are you?"})
