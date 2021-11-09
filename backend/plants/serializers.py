from rest_framework import serializers
from .models import Domain, Kingdom, Phylum, Class, Order, Family, Genus, Species, Plant


class DomainSerlializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields = "__all__"


class KingdomSerlializer(serializers.ModelSerializer):
    class Meta:
        model = Kingdom
        fields = "__all__"


class PhylumSerlializer(serializers.ModelSerializer):
    class Meta:
        model = Phylum
        fields = "__all__"


class ClassSerlializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = "__all__"


class OrderSerlializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class FamilySerlializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = "__all__"


class GenusSerlializer(serializers.ModelSerializer):
    class Meta:
        model = Genus
        fields = "__all__"


class SpeciesSerlializer(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields = "__all__"


class PlantSerlializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = "__all__"
