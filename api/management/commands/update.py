from django.core.management.base import BaseCommand
import requests
from api.models import University


def fetch():
    r = requests.get(
        "https://raw.githubusercontent.com/Hipo/university-domains-list/master/world_universities_and_domains.json"
    )
    r.raise_for_status()
    return r.json()


def update_database():
    data = fetch()
    objects = [University(
                country=x["country"],
                name=x["name"],
                web_pages=x["web_pages"],
                alpha_two_code=x["alpha_two_code"],
                state_province=x["state-province"],
                domains=x["domains"],
            ) for x in data]

    University.objects.bulk_create(objects, ignore_conflicts=True)


class Command(BaseCommand):
    help = "updates the database"

    def handle(self, *args, **options):
        update_database()
        self.stdout.write(self.style.SUCCESS("Successfully updated database"))
