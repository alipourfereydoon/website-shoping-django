from django.urls import path
from . import views

# urlpatterns=[
#     path('',views.home)
# ]

app_name='home_app'

urlpatterns=[
    path('',views.home,name='main')
]