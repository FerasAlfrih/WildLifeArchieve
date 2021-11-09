from django.urls import path
from . import views

urlpatterns = [
    path('animals/', views.AnimalsView.as_view()),
    path('animals/speciess/', views.SpeciessView.as_view()),
    path('animals/genuss/', views.GenussView.as_view()),
    path('animals/familys/', views.FamilysView.as_view()),
    path('animals/orders/', views.OrdersView.as_view()),
    path('animals/classes/', views.ClasssView.as_view()),
    path('animals/phylums/', views.PhylumsView.as_view()),
    path('animals/kingdoms/', views.KingdomsView.as_view()),
    path('animals/domains/', views.DomainsView.as_view()),
    path('animals/<slug:animal_slug>',  views.AnimalDetailsView.as_view()),
]
