import graphene
from graphene_django import DjangoObjectType
from graphql import GraphQLError
from .models import University


class UniversityType(DjangoObjectType):
    class Meta:
        model = University
        fields = ("name", "country", "alpha_two_code", "domains", "web_pages")


class Query(graphene.ObjectType):
    all_universities = graphene.List(
        UniversityType,
        name=graphene.String(),
        country=graphene.String(),
        alpha_two_code=graphene.String(),
        domain=graphene.String(),
    )

    def resolve_all_universities(parent, info, **search):
        try:
            name = search.get("name")
            country = search.get("country")
            alpha_two_code = search.get("alpha_two_code")
            domain = search.get("domain")
            if country and name:
                return University.objects.filter(name__icontains=name).filter(
                    country__icontains=country
                )
            elif alpha_two_code and name:
                return University.objects.filter(name__icontains=name).filter(
                    alpha_two_code__iexact=alpha_two_code
                )
            elif country:
                return University.objects.filter(country__icontains=country)
            elif name:
                return University.objects.filter(name__icontains=name)
            elif alpha_two_code:
                return University.objects.filter(
                    alpha_two_code__icontains=alpha_two_code
                )
            elif domain:
                return University.objects.filter(domains__icontains=domain)

        except Exception:
            raise GraphQLError("You did not provide any arguments.")


schema = graphene.Schema(query=Query)
