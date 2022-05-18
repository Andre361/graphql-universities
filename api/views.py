import requests
from django.http import HttpResponse


def fetch(request):

    response = requests.get(
        "https://raw.githubusercontent.com/Hipo/university-domains-list/master/world_universities_and_domains.json"
    )
    response.raise_for_status()
    data = response.json()
    return data