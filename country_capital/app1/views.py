from django.shortcuts import render
import requests
import random
# Create your views here.

def get_country(countries_list, country):
    for c in countries_list:
        if country == c.get('name'):
            break
    return c

def Guess_Capital(request):
    url = 'https://countriesnow.space/api/v0.1/countries/capital'
    context = {}
    resp = requests.get(url)
    countries_list = resp.json()['data']
    random_country = random.randint(0, len(countries_list))
    country_name = countries_list[random_country].get('name')
    context['country_name'] = country_name

    if request.method == 'POST':
        country = request.POST.get('country')
        capital = request.POST.get('capital')
        result = get_country(countries_list, country)
        if not capital == result.get('capital'):
            context['answer'] = result.get('capital')
    return render(request, 'country.html', context)