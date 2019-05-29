from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def accueil(request):
	# if some data is sent
	if request.method == 'POST':   # il y a des donnees envoye par l'intermedaiaire du formuaire
		# get submitted value
		cookie = request.POST.get('text', None)  # on les recupere les valeur du formulaire
	
		# setting the cookie in the request to pass it to the templqte engine
		request.COOKIES['mycookie'] = cookie # je modifie mon discionnaire request pour donner la valeur de ce qui a ete saisi a la cle mycookie 
		response = render(request,'page_accueil.html') # recuperation de la valeur de la fonction render 


		# set the value in the response as cookie 
		response.set_cookie('my_cookie',cookie,42) # creation du cookie, avec sa duree de vie definie dans le settings
		return response

	# if the pqge is just refreshed
	return render(request,'page_accueil.html')

	template = loader.get_template('page_accueil.html')
	context = {}
	return HttpResponse(template.render(context, request))
