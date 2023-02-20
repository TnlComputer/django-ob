from django.contrib import admin
from .models import Product

# gestionar los modelos de administracion, con la importacion del ModelAdmin


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "short_description", "stock")
    # agregamos una busqueda y le decimos en cuales campos queremos buscar
    search_fields = ("name", "short_description")

    # agregamos filtros
    list_filter = ("name", "short_description",
                   "description", "stock", "discount_until")

    # gerarquias en el filtrado
    # date_hierarchy = 'discount_until'


admin.site.register(Product, ProductAdmin)
