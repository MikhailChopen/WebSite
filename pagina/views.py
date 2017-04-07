from django.shortcuts import render

def home(request):

	template = "pagina/home.html"
	return render(request,template)