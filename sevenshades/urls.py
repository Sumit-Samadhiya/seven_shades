"""
URL configuration for sevenshades project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from sevenshadesapp import maincategory_views,mysubcategory_views,brands_views,product_views,productdetails_views,admin_login_view,userinterface,banner_views,signup_views

from django.urls import include,re_path


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api/maincategory_submit',maincategory_views.MainCategory_Submit),
    re_path(r'^api/maincategory_list',maincategory_views.MainCategory_List),
    re_path(r'^api/editmaincategory_icon',maincategory_views.EditCategory_Icon),
    re_path(r'^api/editmaincategory_data',maincategory_views.EditCategory_Data),
    re_path(r'^api/deletemaincategorydata',maincategory_views.DeleteCategory_Data),



    re_path(r'^api/mysubcategory_submit',mysubcategory_views.MySubCategory_Submit),
    re_path(r'^api/mysubcategory_list',mysubcategory_views.MySubCategory_List),
    re_path(r'^api/editmysubcategory_icon',mysubcategory_views.EditMySubCategory_Icon),
    re_path(r'^api/editmysubcategory_data',mysubcategory_views.EditMySubCategory_Data),
    re_path(r'^api/deletemysubcategorydata',mysubcategory_views.DeleteMySubCategory_Data),
   



    re_path(r'^api/brand_submit',brands_views.Brands_Submit),
    re_path(r'^api/brand_list',brands_views.Brands_List),
    re_path(r'^api/editbrand_icon',brands_views.EditBrands_Icon),
    re_path(r'^api/editbrand_data',brands_views.EditBrands_Data),
    re_path(r'^api/deletebranddata',brands_views.DeleteBrands_Data),


    re_path(r'^api/product_submit',product_views.Product_Submit),
    re_path(r'^api/product_list',product_views.Product_List),
    re_path(r'^api/editproduct_icon',product_views.EditProduct_Icon),
    re_path(r'^api/editproduct_data',product_views.EditProduct_Data),
    re_path(r'^api/deleteproductdata',product_views.DeleteProduct_Data),
    re_path(r'^api/product_mysubcategory_list_by_maincategoryid',product_views.mysubcategory_list_by_maincategoryid),



    re_path(r'^api/productdetails_submit',productdetails_views.ProductDetails_Submit),
    re_path(r'^api/productdetails_list',productdetails_views.ProductDetails_List),
    re_path(r'^api/editproductdetails_icon',productdetails_views.EditProductDetails_Icon),
    re_path(r'^api/editproductdetails_data',productdetails_views.EditProductDetails_Data),
    re_path(r'^api/deleteproductdetails',productdetails_views.DeleteProductDetails_Data),
    re_path(r'^api/productdetail_product_list_by_subcategoryid',productdetails_views.Productdetail_product_list_by_subcategoryid),
    re_path(r'^api/productdetail_brand_list_by_productid',productdetails_views.Productdetail_brand_list_by_productid),



    re_path(r'^api/check_admin_login',admin_login_view.CheckAdminLogin),

   #users
    re_path(r'^api/user_main_category_list',userinterface.User_MainCategory_List),
    re_path(r'^api/user_mysubcategory_list_by_maincategoryid',userinterface.user_mysubcategory_list_by_maincategoryid),
    re_path(r'^api/user_brand_list',userinterface.Brands_List),
    re_path(r'^api/user_banner_list',userinterface.Banner_List),
    re_path(r'^api/user_subcategory_list',userinterface.Subcategory_List),
    re_path(r'^api/user_category_list',userinterface.Category_List),
    re_path(r'^api/user_brand_list',userinterface.Brands_List),
    re_path(r'^api/user_maincategory_list',userinterface.MainCategory_List),
    re_path(r'^api/user_products_maincategory',userinterface.User_Products_Maincategory),
    re_path(r'^api/user_productsdetails_by_id',userinterface.User_ProductsDetails_By_Id),
    
    

#banner
    re_path(r'^api/banner_submit',banner_views.Banner_Submit),

#signup
    re_path(r'^api/signup_submit',signup_views.SignUp_Submit),
    re_path(r'^api/check_costumer_login',signup_views.CheckCostumerLogin),
    re_path(r'^api/fetch_user_address',signup_views.FetchUserAddress),
    re_path(r'^api/address_submit',signup_views.Address_Submit),


]
