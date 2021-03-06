"""SE4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import include, path

urlpatterns = [
    path('task_board/', include('task_board.urls')),
    path('task_manager/', include('task_manager.urls')),
    path('admin/', admin.site.urls),
    path('check_out/', include('check_out.urls')),
	path('item_locator/', include('item_locator.urls')),
	path('', include('login.urls')),
	path('price_checker/', include('price_checker.urls')),
	path('returns/', include('returns.urls')),
	path('shopping_list/', include('shopping_list.urls')),
	path('analytics/', include('analytics.urls')),
]