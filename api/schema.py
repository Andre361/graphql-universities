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
    filter_by_alpha_two_code = graphene.List(UniversityType,alpha_two_code=graphene.String(required=True))
    filter_by_domain = graphene.List(UniversityType,domain=graphene.String(required=True))
    filter_by_country_and_name = graphene.List(UniversityType,country=graphene.String(required=True),name=graphene.String(required=True))
    filter = graphene.List(
        UniversityType, name=graphene.String(),country=graphene.String(),alpha_two_code=graphene.String(),web_pages=graphene.List(graphene.String),domains=graphene.List(graphene.String),
    )

    def resolve_all_universities(parent, info):
        return University.objects.all()

    def resolve_filter_by_name(parent, info, name):
        return University.objects.filter(name__icontains=name)

    def resolve_filter_by_country(parent, info, country):
        return University.objects.filter(country__icontains=country)

    def resolve_filter_by_country_and_name(parent,info,country,name):
        return University.objects.filter(name__icontains=name).filter(country__icontains=country)

    def resolve_filter_by_alpha_two_code(parent,info,alpha_two_code):
        return University.objects.filter(alpha_two_code__icontains=alpha_two_code)

    def resolve_filter_by_domain(parent,info,domain):
        return University.objects.filter(domains__icontains=domain)

    def resolve_filter_by_alpha_two_code_and_name(parent,info,alpha_two_code,name):
        University.objects.filter(name__icontains=name).filter(alpha_two_code__icontains=alpha_two_code)

    def resolve_filter(parent,info,**kwargs):
        # alternative method of resolving based on arguments provided
        name = kwargs.get('name')
        country= kwargs.get('country')
        if name and country:
            return University.objects.filter(name__icontains=name).filter(country__icontains=country)




schema = graphene.Schema(query=Query)
