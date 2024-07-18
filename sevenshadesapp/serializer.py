from rest_framework import  serializers
from sevenshadesapp.models import MainCategory,MySubCategory,Brands,Product,ProductDetails,AdminLogin,Banner,SignUp,UserAddress
class  MainCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=MainCategory
        fields = '__all__'




class  MySubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=MySubCategory
        fields = '__all__'

class  MySubCategoryGetSerializer(serializers.ModelSerializer):
    maincategoryid=MainCategorySerializer(many=False)
    class Meta:
        model=MySubCategory
        fields = '__all__'



class  BrandsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Brands
        fields = '__all__'



class  ProductGetSerializer(serializers.ModelSerializer):
    maincategoryid= MainCategorySerializer(many=False)
    subcategoryid=MySubCategorySerializer(many=False)
    brandid= BrandsSerializer(many=False)
    
    class Meta:
        model=Product
        fields = '__all__'


class  ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields = '__all__'


class  ProductDetailsGetSerializer(serializers.ModelSerializer):
    maincategoryid= MainCategorySerializer(many=False)
    subcategoryid=MySubCategorySerializer(many=False)
    brandid= BrandsSerializer(many=False)
    productid=ProductSerializer(many=False)
    class Meta:
        model=ProductDetails
        fields = '__all__'


class  ProductDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductDetails
        fields = '__all__'


class  AdminLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=AdminLogin
        fields = '__all__'


class  BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Banner
        fields = '__all__'

class  SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model=SignUp
        fields = '__all__'

class UserAddressGetSerializer(serializers.ModelSerializer):
    id=SignUpSerializer(many=False)
    class Meta:
        model = UserAddress
        fields = '__all__'

class  UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserAddress
        fields = '__all__'


# class  SearchSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Search
#         fields = '__all__'




