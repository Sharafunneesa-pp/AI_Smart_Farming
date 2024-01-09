from django.contrib import admin
from django.urls import path
from .import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index),
    path('index', views.index, name='index'),
    path('get_bot_response', views.get_bot_response, name='get_bot_response'),
    path('registration',views.registration),
    path('register',views.register),
    path('login/', views.login, name='login'),
    path('login/check_login', views.check_login, name='check_login'),
    path('logout/',views.logout),
    path('edit_profile',views.edit_profile,name='edit_profile'),
    path('crop_prediction',views.crop_prediction),
    path('predict_crop',views.predict_crop),
    path('print_crop/<int:id>',views.print_crop),

    path("ftlzr_sugstn/<int:id>",views.ftlzr_sugstn),
    path('print_ftlzr<int:id>',views.print_ftlzr),
    path('print_ftlzr/<int:id>',views.print_ftlzr),
    path('ftlzr_sugstn/predict_ftlzr',views.predict_ftlzr),
    path('ftlzr_sugstn/view_your_fertilizer/<str:name>',views.view_your_fertilizer),
    path('ftlzr_sugstn/print_ftlzr/<int:id>',views.print_ftlzr),

    path('ftlzr_prediction',views.ftlzr_prediction),
    path('ftlzr_sugstn/buy_product/<int:id>',views.buy_product),
    path('ftlzr_sugstn/view_your_fertilizer/buy_product/<int:id>',views.buy_product),
    path('ftlzr_sugstn/view_your_fertilizer/buy_product/addpurchase',views.addpurchase),
    path('ftlzr_sugstn/purchase_history',views.purchase_history),
    path('predict_ftlzr',views.predict_ftlzr),

    path('disease_pred',views.disease_pred),
    path('addfile',views.addfile),
    path('view_users',views.view_users),
    path('product1',views.product1),

    path('add_product',views.add_product),
    path('view_product',views.view_product),
    path('update_product_details/<int:id>',views.update_product_details),
    path('update_product_details/update_product/<int:id>',views.update_product),
    path('delete_product_details/<int:id>',views.delete_product_details),
    path('view_your_fertilizer/<str:name>',views.view_your_fertilizer),
    path('view_your_fertilizer/buy_product/<int:id>',views.buy_product),
    path('view_your_fertilizer/buy_product/addpurchase',views.addpurchase),
    path('view_ftlzr',views.view_ftlzr),
    path('search_products',views.search_products),
    path('user_purchase_history',views.user_purchase_history),

    path('view_your_pesticide/<str:name>',views.view_your_pesticide),
    path('view_your_pesticide/buy_product/<int:id>',views.buy_product),
    path('view_your_pesticide/buy_product/addpurchase',views.addpurchase),
    path('view_your_pesticide/purchase_history',views.purchase_history),

    path('buy_product/<int:id>',views.buy_product),
    path('buy_product/addpurchase',views.addpurchase),
    path('purchase_history/', views.purchase_history, name='purchase_history'),
    path('purchase_history/update_status/<int:id>/', views.update_status, name='update_status'),

    path('report_user',views.report_user),
    path('report_crop',views.report_crop),
    path('report_fertilizer',views.report_fertilizer),
    path('report_product',views.report_product),
    path('report_transaction',views.report_transaction),
    path('date_range',views.date_range),
    
    path('admin/', admin.site.urls),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)