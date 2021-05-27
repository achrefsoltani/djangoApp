from django.urls import path
from .views import FormationListView
from .views import FormationDetailView

urlpatterns = [
    path('', FormationListView.as_view(), name="formation_list"),
    path('<int:pk>/', FormationDetailView.as_view(), name="formation_detail"),
]