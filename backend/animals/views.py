from django.shortcuts import Http404
from .serializers import AnimalSerlializer, DomainSerlializer, KingdomSerlializer, SpeciesSerlializer, GenusSerlializer, FamilySerlializer, OrderSerlializer, ClassSerlializer, PhylumSerlializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Domain, Kingdom, Phylum, Class, Order, Family, Genus, Species, Animal


        

class AnimalsView(APIView):
    def get(self, request, format=None):
        animals = Animal.objects.all()
        serializer = AnimalSerlializer(animals, many=True)
        return Response(serializer.data)

class AnimalDetailsView(APIView):
    def get_object(self, animal_slug,  *args, **kwargs):
        print(animal_slug)
        try:
            return Animal.objects.filter().get(slug=animal_slug)
        except Animal.DoesNotExist:
            raise Http404
    def get(self, request,  animal_slug, format=None):
        animal = self.get_object(animal_slug)
        serializer = AnimalSerlializer(animal)
        return Response(serializer.data)


class SpeciessView(APIView):
    def get(self, request, format=None):
        speciess = Species.objects.all()

        serializer = SpeciesSerlializer(speciess, many=True)
        return Response(serializer.data)


class GenussView(APIView):
    def get(self, request, format=None):
        genuss = Genus.objects.all()

        serializer = GenusSerlializer(genuss, many=True)
        return Response(serializer.data)


class FamilysView(APIView):
    def get(self, request, format=None):
        familys = Family.objects.all()

        serializer = FamilySerlializer(familys, many=True)
        return Response(serializer.data)


class OrdersView(APIView):
    def get(self, request, format=None):
        orders = Order.objects.all()

        serializer = OrderSerlializer(orders, many=True)
        return Response(serializer.data)


class ClasssView(APIView):
    def get(self, request, format=None):
        _classs = Class.objects.all()

        serializer = ClassSerlializer(_classs, many=True)
        return Response(serializer.data)


class PhylumsView(APIView):
    def get(self, request, format=None):
        phylums = Phylum.objects.all()

        serializer = PhylumSerlializer(phylums, many=True)
        return Response(serializer.data)


class KingdomsView(APIView):
    def get(self, request, format=None):
        kingdoms = Kingdom.objects.all()

        serializer = KingdomSerlializer(kingdoms, many=True)
        return Response(serializer.data)


class DomainsView(APIView):
    def get(self, request, format=None):
        domains = Domain.objects.all()

        serializer = DomainSerlializer(domains, many=True)
        return Response(serializer.data)
