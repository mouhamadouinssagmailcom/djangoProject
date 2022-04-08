from rest_framework import serializers
from .models import Category, Product


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [

            'id',
            'name',
            'description',
            'price',
            'get_image',
            'get_thumbnail'

        ]


class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializers(many=True)

    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'products'

        ]
