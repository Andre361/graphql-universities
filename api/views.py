from django.shortcuts import render
from .models import University
import requests


async def update_database():

    r = requests.get(
        "https://raw.githubusercontent.com/Hipo/university-domains-list/master/world_universities_and_domains.json"
    )
    r.raise_for_status()
    data = r.json()

    for x in data:
        University.objects.create(
            country=x["country"],
            name=x["name"],
            web_pages=x["web_pages"],
            alpha_two_code=x["alpha_two_code"],
            state_province=x["state_province"],
            domains=x["domains"],
        )


@app.get("/search", tags=["Search"])
async def search(
    country: Optional[str] = None,
    name: Optional[str] = None,
    alpha_two_code: Optional[str] = None,
    domain: Optional[str] = None,
):

    if country and name:
        query = (
            "SELECT * FROM universities WHERE country ILIKE '%"
            + country
            + "%' AND name ILIKE '%"
            + name
            + "%'"
        )
        return await database.fetch_all(query)

    elif alpha_two_code and name:
        query = (
            "SELECT * FROM universities WHERE alpha_two_code ILIKE '%"
            + alpha_two_code
            + "%' AND name ILIKE '%"
            + name
            + "%'"
        )
        return await database.fetch_all(query)

    elif country:
        query = "SELECT * FROM universities WHERE country ILIKE '%" + country + "%'"
        return await database.fetch_all(query)

    elif name:
        query = "SELECT * FROM universities WHERE name ILIKE '%" + name + "%'"
        return await database.fetch_all(query)

    elif alpha_two_code:
        query = (
            "SELECT * FROM universities WHERE alpha_two_code ILIKE '%"
            + alpha_two_code
            + "%'"
        )
        return await database.fetch_all(query)

    elif domain:
        query = "SELECT * FROM universities WHERE domains && '{" + domain + "}'"
        return await database.fetch_all(query)


@app.get("/", include_in_schema=False)
async def index():
    return RedirectResponse("/docs")
