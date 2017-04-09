from django.shortcuts import render

def home(request):

	template = "pagina/home.html"
	return render(request,template)

def contacto(request):

	template = "pagina/contactenos.html"
	return render(request,template)