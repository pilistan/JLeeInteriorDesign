from django.shortcuts import render
from .models import Project
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt
# def update(request):
#     if request.method == "POST":
#         '''
#         pass the path of the diectory where your project will be 
#         stored on PythonAnywhere in the git.Repo() as parameter.
#         Here the name of my directory is "test.pythonanywhere.com"
#         '''
#         repo = git.Repo("www.jleeinteriorsesign.com") 
#         origin = repo.remotes.origin

#         origin.pull()

#         return HttpResponse("Updated code on PythonAnywhere")
#     else:
#         return HttpResponse("Couldn't update the code on PythonAnywhere")

def home(request):
	projects = Project.objects.all()
	return render(request, 'portfolio/home.html', {'projects':projects})
