from django.shortcuts import render, get_object_or_404
from .models import Job
# Create your views here.

def homepage (request) :
    jobs = Job.objects
    return  render(request,"jobs/homepage.html",{'jobs':jobs})


def details(request,job_id):
    job = get_object_or_404(Job, pk=job_id)
    return render(request, "jobs/details.html",{'job':job})