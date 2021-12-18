from django.shortcuts import render
from django.http import HttpResponse
from .models import Skill , Job , Candidate , Title

# Create your views here.

def Home(request):
      return render(request , 'home/home.html')

def CandidateFinder(request):
    candidates = 'A'
    try:
        id = request.GET['job']
        job = Job.objects.get(id = id)
        job_skills = job.skill.all()
        candidates = Candidate.objects.filter(title = job.title)
        count = [i.id for i in job_skills]
        print(count)
        print(job)
        print(job_skills)
        print(candidates)
        
        for candidate in candidates:
            print(candidate.skill.all())
            counter = 0
            countin = [i.id for i in candidate.skill.all()]
            for i in countin:
                print(i)
                if(i in count):
                    counter+=1
                if(i > count[len(count)-1]):
                    break
            (countin)
            print(counter)
     
    except Exception as e:
        print(e)
    jobs = Job.objects.all()
    return render(request , 'candidateFinder/candidateFinder.html' , {'jobs':jobs , 'candidate' :candidates})
    
 
def Skills(request):
    try:
        name = request.POST['name']
        skill = Skill(name = name)
        skill.save()
    except Exception as e:
        print(e)
    skills = Skill.objects.all()
    return render(request , 'skills/skills.html' , {'skills': skills})

def Titles(request):
    try:
        name = request.POST['name']
        title = Title(name = name)
        title.save()
    except Exception as e:
        print(e)
    titles = Title.objects.all()
    return render(request , 'titles/titles.html' , {'titles': titles})


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
       print(e)
    jobs = Job.objects.all()
    skills = Skill.objects.all()
    titles = Title.objects.all()
    return render(request , 'job/job.html' , {'jobs': jobs , 'skills': skills , 'titles' : titles})


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
        print(e)
    candidates = Candidate.objects.all()
    skills = Skill.objects.all()
    titles = Title.objects.all()
    return render(request , 'candidate/candidate.html' , {'candidates': candidates, 'skills': skills, 'titles' : titles})

