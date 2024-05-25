from rest_framework.viewsets import ModelViewSet
from producto.api.serializers import ProductoSerializer, CategoriaSerializer
from producto.models import Producto, Categoria


class CategoriaApiViewset(ModelViewSet):
    serializer_class = CategoriaSerializer
    queryset = Categoria.objects.all()


class ProductoApiViewset(ModelViewSet):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.all()
