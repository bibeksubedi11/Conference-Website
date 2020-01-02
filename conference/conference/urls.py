"""conference URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from website import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index' ),
    path('about', views.AboutView.as_view(), name='about'),
    path('speakers', views.speakers, name='speakers'),
    path('schedule', views.ScheduleView.as_view(), name='schedule'),
    path('blog/<int:pk>', views.BlogSingleView.as_view(), name='blogSingle'),
    path('blog', views.BlogView.as_view(), name='blog'),
    path('comment/<int:pk>',views.commentview, name='comment'),
    path('contact', views.contactview, name ='contact'),
    path('join',views.joinview, name='join'),
    

    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

