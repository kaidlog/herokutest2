from rest_framework import serializers

from .models import Category, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # 3.3.0 版本之後 model form 改成 用 exclude的寫法
        fields = '__all__'
        # field = (
        #     "id",
        #     "name",
        #     "get_absolute_url",
        #     "description",
        #     "price",
        #     "get_image",
        #     "get_thumbnail"
        # )
class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = '__all__'
        # fields = (
        #     "id",
        #     "name",
        #     "get_absolute_url",
        #     "products",
        # )
