from django.shortcuts import render
from django.http import HttpResponse
import random
from django.conf import settings


# Create your views here.
def accueil(request):
	user_gived = ''
	if request.COOKIES.get('my_cookie'):
		user_gived = request.COOKIES['my_cookie']
		response = render(request,'page_accueil.html',{'user_gived' : user_gived})
	else :
		user_gived = random.choice(settings.USER_NAMES)
		response = render(request,'page_accueil.html',{'user_gived' : user_gived})
		response.set_cookie('my_cookie',user_gived,max_age=settings.COOKIE_AGE)
	return(response)
	csrftoken = getCookie('csrftoken')
	console.log(csrftoken)


	# Create your views here.
def inscription(request):
 	response = render(request,'inscription.html')
 	return response

	# Create your views here.
def connexion(request):
	response = render(request,'connexion.html')
	return response

