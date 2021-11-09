from django.urls import path
from . import views

urlpatterns = [
    path('plants/', views.PlantsView.as_view()),
    path('plants/speciess/', views.SpeciessView.as_view()),
    path('plants/genuss/', views.GenussView.as_view()),
    path('plants/familys/', views.FamilysView.as_view()),
    path('plants/orders/', views.OrdersView.as_view()),
    path('plants/classes/', views.ClasssView.as_view()),
    path('plants/phylums/', views.PhylumsView.as_view()),
    path('plants/kingdoms/', views.KingdomsView.as_view()),
    path('plants/domains/', views.DomainsView.as_view()),
    path('plants/<slug:plant_slug>',  views.PlantDetailsView.as_view()),
]
