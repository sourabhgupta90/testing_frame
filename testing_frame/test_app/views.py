from django.http import HttpResponse
from django.utils import simplejson 

def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")

def fire_ajax(request):
    #print request.GET['title']
    return_dict = {'message': 'bla bla bla','code':324}
    json = simplejson.dumps(return_dict)
    return HttpResponse(json, mimetype="application/x-javascript")