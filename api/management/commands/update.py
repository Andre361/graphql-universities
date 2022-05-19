from django.core.management.base import BaseCommand, CommandError
import requests
from api.models import University

def fetch():
    r = requests.get(
        "https://raw.githubusercontent.com/Hipo/university-domains-list/master/world_universities_and_domains.json"
    )
    r.raise_for_status()
    return  r.json()


def update_database():
    data = fetch()
    objects = []
    for x in data:
        objects.append(University(
            country=x["country"],
            name=x["name"],
            web_pages=x["web_pages"],
            alpha_two_code=x["alpha_two_code"],
            state_province=x["state-province"],
            domains=x["domains"],
        ))
    saved_objects = list(University.objects.all())
    objects_to_create = [i for i in objects if i not in saved_objects]
    return University.objects.bulk_create(objects_to_create,ignore_conflicts=True)

class Command(BaseCommand):
    help="updates the database when new objects are added"
    
    def handle(self,*args,**options):
        data = fetch()
        objects = []
        for x in data:
            objects.append(University(
                country=x["country"],
                name=x["name"],
                web_pages=x["web_pages"],
                alpha_two_code=x["alpha_two_code"],
                state_province=x["state-province"],
                domains=x["domains"],
            ))
        
        University.objects.bulk_create(objects,ignore_conflicts=True)
        self.stdout.write(self.style.SUCCESS('Successfully closed updated'))
