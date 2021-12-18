from django.urls import path
from . import views

app_name = 'app'


urlpatterns = [
    path('CandidateFinder', views.CandidateFinder , name= "CandidateFinder"),
    path('Skill', views.Skills , name = "Skill"),
    path('Title', views.Titles , name = "Title"),
    path('Candidate', views.Candidates , name = "Candidate"),
    path('Job', views.Jobs , name = "Job"),
    path('', views.Home , name = "home"),

]
