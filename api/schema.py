import graphene
from graphene_django import DjangoObjectType

from .models import University


class UniversityType(DjangoObjectType):
    class Meta:
        model = University
        fields = "__all__"


class Query(graphene.ObjectType):
    all_universities = graphene.List(UniversityType)
    filter_by_name = graphene.List(UniversityType, name=graphene.String(required=True))
    filter_by_country = graphene.List(
        UniversityType, country=graphene.String(required=True)
    )
    filter = graphene.List(
        UniversityType, name=graphene.String(),country=graphene.String(),alpha_two_code=graphene.String(),web_pages=graphene.List(graphene.String),domains=graphene.List(graphene.String),
    )

    def resolve_all_universities(parent, info):
        return University.objects.all()

    def resolve_filter_by_name(parent, info, name):
        return University.objects.filter(name__icontains=name)

    def resolve_filter_by_country(parent, info, country):
        return University.objects.filter(country__icontains=country)

    def resolve_filter(parent,info,**kwargs):
        name = kwargs.get('name')
        country= kwargs.get('country')
        if name and country:
            return University.objects.filter(name__icontains=name,country__icontains=country)




schema = graphene.Schema(query=Query)
