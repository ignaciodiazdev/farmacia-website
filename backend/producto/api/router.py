from rest_framework.routers import DefaultRouter
from producto.api.views import ProductoApiViewset, CategoriaApiViewset

router_producto = DefaultRouter()

router_producto.register(
    prefix='productos',
    viewset=ProductoApiViewset,
    basename='productos'
)

router_categoria = DefaultRouter()

router_categoria.register(
    prefix='categorias',
    viewset=CategoriaApiViewset,
    basename='categorias'
)
