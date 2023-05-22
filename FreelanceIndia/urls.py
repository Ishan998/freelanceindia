from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.client.authcheck,name="mainpage"),
# path('register',views.client.register,name="register"),
path('registercheck',views.client.registercheck,name="registercheck"),
path('fogpas',views.client.passreset,name="fogpas"),
path('pricing',views.client.pricing,name="pricing"),
path('jobabout',views.client.cldash,name="jobabout"),
path('about',views.client.aboutus,name="about"),
path('feedback',views.client.feedback,name="feedback"),
path('jobstatus/<int:id>',views.client.jobstatus,name="jobstatus"),
path('addjob',views.client.addjob,name="addjob"),
path('addjobinfo',views.client.jobdatadd,name="addjobinfo"),
path('removejob/<int:id>',views.client.removejob,name="removejob"),
path('freelancerdashboard',views.client.developerdash,name="freelancerdashboard"),
path('topclients',views.client.topclients,name="topclients"),
path('myfeedbacks',views.client.devfeedback,name="myfeedbacks"),
path('passverification',views.client.passverification,name="passverification"),
path('claims/<int:id>',views.client.claims,name="claims"),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)