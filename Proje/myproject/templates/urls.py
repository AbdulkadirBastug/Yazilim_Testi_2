from django import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('index/',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('blog/',views.blog,name='blog'),
    path('industry/',views.industry,name='industry'),
    path('singleBlog/<int:post_id>/',views.singleBlog,name='singleBlog'),
    path('singleIndustry/<int:post_id>/',views.singleIndustry,name='singleIndustry'),
    path('blogSave/',views.blogSave,name='blogSave'),
    path('industrySave/',views.industrySave,name='industrySave'),
    path('logout/',views.logout,name='logout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)