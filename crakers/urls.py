from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from crakerapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('adminloginpage/',views.adminloginpage,name='adminloginpage'),
    path('adminlogin/',views.adminlogin,name='adminlogin'),
    path('admindashboard/',views.admindashboard,name='admindashboard'),
    path('admingetitems/',views.admingetitems,name='admingetitems'),
    path('additem/',views.add_item,name='additem'),
    path('deleteitem/',views.delete_item,name='deleteitem'),
    path('placeorder/',views.place_order,name='placeorder'),
    path('adminorderpage/',views.adminorderpage,name='adminorderpage'),
    path('getorderitems/<int:order_id>/', views.getorderitems, name='getorderitems'),
    path('orderdelevired/<int:order_id>/', views.orderdelevired, name='orderdelevired'),
    path('deleteorder/<int:order_id>/', views.deleteorder, name='deleteorder'),
    path('downloadreport/',views.download_report,name='downloadreport'),
    path('invoice/<int:order_id>/', views.generate_invoice_pdf, name='generate_invoice_pdf'),
    path('admin_logout_view/',views.admin_logout_view,name='admin_logout_view'),
    path('getorders/',views.getorders,name='getorders'),
    path('adminitemcountpage/',views.adminitemcountpage,name='adminitemcountpage'),
    path('getitemcounts/',views.get_item_counts,name='getitemcounts'),
]#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
