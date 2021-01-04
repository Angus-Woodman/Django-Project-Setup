from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='adoption-index'), # route for /adoption/
    path('about/', views.about, name='adoption-about'), # route for /adoption/about
    # path('<id>/', views.show, name='adoption-show'), # route for /adoption/:id
    path('<int:id>/', views.show, name='adoption-show') # to accept only numbers as id param
]
