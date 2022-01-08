# urls.py
from django.contrib import admin
from django.urls import path

from poll import views as poll_views

admin.site.site_header = "Poll Admin Portal"
admin.site.site_title = "Poll Admin Portal"
admin.site.index_title = "Welcome to Poll "
urlpatterns = [
    path('pkjha/', admin.site.urls),
    path('', poll_views.home, name='home'),
    path('create/', poll_views.create, name='create'),
    path('results/<poll_id>/', poll_views.results, name='results'),
    path('vote/<poll_id>/', poll_views.vote, name='vote'),
]
