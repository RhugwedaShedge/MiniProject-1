from django.shortcuts import render, HttpResponse

# Create your views here.


def home_view(request, *args, **kwargs):
	#print(request)
	#print(request.user)
	

	return render(request, "farmers/index.html", {})

