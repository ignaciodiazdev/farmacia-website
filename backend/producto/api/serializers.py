from rest_framework import serializers
from producto.models import Producto, Categoria


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class ProductoSerializer(serializers.ModelSerializer):
    categoria = serializers.StringRelatedField()
    categoria_data = CategoriaSerializer(source='categoria', read_only=True)

    class Meta:
        model = Producto
        fields = '__all__'
