from ennarroot import views
from django.urls import path,include

app_name='ennarroot'
urlpatterns = [
    path('',views.index ,name='home'),
    path('Admin/',views.admin,name='Admin'),
    path('admin_login/',views.adminLogin,name='admin_login'),
    path('admin_desk/',views.adminDesk,name='admin_desk'),
    path('logout/',views.logout,name='logout'),
    path('upload_product/',views.uploadForm,name='productupload'),
    path('upload/',views.productUpload,name='upload'),
    path('view_products/',views.viewProducts,name='viewproducts'),
    path('enquiry/',views.enquirey,name='enquiry'),
    path('save_enq/',views.saveEnquirey,name='save_enq'),
    path('contact/',views.contactus,name='contact'),
    path('<int:product_id>/',views.orderproduct,name='orderproduct')


]
