app_name = 'trade_auth'
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include, path,re_path
from currency import views

urlpatterns = [
	
	path('',views.index,name="home"),
     path('create/', views.create_person, name='create_person'),
     path('register/', views.register_data, name='register_data'),
     path('user_register/', views.register, name='register'),
     path('user_login/', views.user_login, name='login'),
     path('logout/', views.user_logout, name='logout'),
     path('admin1/', views.Admin,name='newuser')
     # path('reg',views.Register,name='newreg')
	 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)