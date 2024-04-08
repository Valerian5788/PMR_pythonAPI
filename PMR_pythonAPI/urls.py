"""
URL configuration for PMR_pythonAPI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from pythonAPI_PMR import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('TecStopAroundStation/', views.arrets_de_bus_zone),
    path('jsonFacilities', views.get_all_facilities),
    path('jsonComposition/<int:id>', views.getFacilitiesOfATrain),
    path('CharleroiTri/<str:day>', views.getCrowdManagementOfDayCharleroi),
    path('NamurTri/<str:day>', views.getCrowdManagementOfDayNamur),
    path('tecDocument', views.documentation_bus),
    path('documentationInstallations/', views.documentationInstallations),
    path('documentationCrowd', views.documentationCrowdCharleroi),
    path('documentationCrowdNam', views.documentationCrowdNamur),
    path('compositionDocumentation', views.documentationTrain),
    path('Documentation', views.GetDocumentationView),
    path('GetHauteurQuai/<str:city>', views.GetHauteurQuaiByCity)
]
