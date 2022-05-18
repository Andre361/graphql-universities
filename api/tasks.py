import requests
# from background_task import background
from .models import University

r = requests.get(
    "https://raw.githubusercontent.com/Hipo/university-domains-list/master/world_universities_and_domains.json"
)
r.raise_for_status()
data = r.json()


# @background(schedule=5)
def update_database():
    objects = []
    objects_to_update = [i for i in University.objects.all()]
    # objects_to_create = [i for i in ]
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
    
update_database()