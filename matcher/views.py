from django.shortcuts import render
from django.db.models import Count
from .models import Skill , Job , Candidate , Title

# Create your views here.


def Home(request):
      return render(request , 'home/home.html')

# The function gets a Job ,Looking for the candidates with the same title
# Goes through all the skills of the job and checks which candidate has more suitable skills
def CandidateFinder(request):
    candidates = ""
    job = ""
    try:
        id = request.GET['job']
        job = Job.objects.get(id = id)
        candidates = Candidate.objects.filter(title = job.title)
        candidates = candidates.filter(skill__in = job.skill.all()).annotate(sum=Count('id')).order_by('-sum')
        print(candidates)
        
    except Exception as e:
        err = e
    
    jobs = Job.objects.all()
    return render(request , 'candidateFinder/candidateFinder.html' , {'jobs':jobs , 'candidates' :candidates , 'job':job} )
    

# This function adds skills to the table Skill
def Skills(request):
    try:
        name = request.POST['name']
        skill = Skill(name = name)
        skill.save()
    except Exception as e:
        err = e
    skills = Skill.objects.all()
    return render(request , 'skills/skills.html' , {'skills': skills})

# This function adds titles to the table Title
def Titles(request):
    try:
        name = request.POST['name']
        title = Title(name = name)
        title.save()
    except Exception as e:
        err = e
    titles = Title.objects.all()
    return render(request , 'titles/titles.html' , {'titles': titles})

# This function adds jobs to the table Jobs
# After selecting a job title and required skills
def Jobs(request):
    try:
        title = request.POST['title']
        name = request.POST.getlist('name')
        job = Job(title = Title.objects.get(id = title))
        job.save() 
        for i in name:
            job.skill.add(Skill.objects.get(id = int(i)))  
        print(job.skill.all())
    except Exception as e:
       err = e
    jobs = Job.objects.all()
    skills = Skill.objects.all()
    titles = Title.objects.all()
    return render(request , 'job/job.html' , {'jobs': jobs , 'skills': skills , 'titles' : titles})

# This function adds candidate to the table Candidates
# After selecting a candidate title and skills
def Candidates(request):
    try:
        title = request.POST['title']
        name = request.POST.getlist('name')
        candidate = Candidate(title = Title.objects.get(id = title))
        candidate.save()
        for i in name:
            candidate.skill.add(Skill.objects.get(id = int(i)))  
        print(candidate.skill.all())
    except Exception as e:
        err = e
    candidates = Candidate.objects.all()
    skills = Skill.objects.all()
    titles = Title.objects.all()
    return render(request , 'candidate/candidate.html' , {'candidates': candidates, 'skills': skills, 'titles' : titles})

