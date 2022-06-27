from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import requests
from urllib3 import HTTPResponse
from requests_oauthlib import OAuth1
import pprint
import os
from dotenv import load_dotenv


load_dotenv()

pp = pprint.PrettyPrinter(indent=2, depth=2)
# Create your views here.
def index(request):
    endpoint = 'https://favqs.com/api/qotd'
    API_response = requests.get(endpoint)
    responseJSON = API_response.json()
    author = responseJSON['quote']['author']
    quote = responseJSON['quote']['body']
    response = render(request, 'fav_quotes_app/index.html', {'author': author, 'quote': quote})
    return response
    
def all_quotes(request):
    print('---------got a request-----------')
    auth = os.environ['apikey']
    head = {'Authorization': 'Token token=' + auth}
    endpoint = 'https://favqs.com/api/quotes'
    API_response = requests.get(url=endpoint, headers=head)
    data = API_response.json()
    print(data)
    response = render(request, 'fav_quotes_app/all_quotes.html', data)
    return response
    
    
    