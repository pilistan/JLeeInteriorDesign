"""mysite URL Configuration

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
from django.conf.urls.static import static
from django.conf import settings
from portfolio import views

#from portfolio.views import update

from personal.views import (
	home_screen_view,

	)


from account.views import (
    registration_view,
    logout_view,
    login_view, 
    account_view,
    )


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', home_screen_view, name="home"), 
    path('', views.home, name="home"), 
    path('register/', registration_view, name="register"),
    path('logout/', logout_view, name="logout"),
    path('login/', login_view, name="login"),
    path('account/', account_view, name="account"),
    #path("update_server/", update, name="update"),
    #path('blog/', include('blog.urls')),

]
 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)