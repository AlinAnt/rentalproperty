from django.urls import path, include
from . import views
from django.contrib import admin
from django.conf.urls import url
from django.contrib.auth.views import auth_login, auth_logout

urlpatterns = [

    path('', views.index, name='index'),
    path('areas/', views.AreaListView.as_view(), name='areas'),
    path('tareas/', views.TypeAreaListView.as_view(), name='tareas'),
    path('areas/<int:pk>', views.AreaDetailView.as_view(), name='area-detail'),
    path('tareas/<int:pk>', views.TypeAreaDetailView.as_view(), name='typearea-detail'),
    path('register/', views.RegisterList.as_view(), name='register'),

]

urlpatterns += [
    path('myAreas/', views.RentalAreasByUserListView.as_view(), name='my-rent'),
    path('rental/', views.RentalBooksAllListView.as_view(), name='all-rent'),
]

urlpatterns += [
    path('area/<uuid:pk>/renew/', views.renew_area_seller, name='renew-area-seller'),
]



