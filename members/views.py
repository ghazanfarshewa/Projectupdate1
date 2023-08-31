from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member
from .forms import MemberForm

def members(request):
  
  if request.method == 'POST':
    form = MemberForm(request.POST)
    if form.is_valid():
      form.save()
  
  
  form = MemberForm()
  mymembers = Member.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'mymembers': mymembers,
    'form': form,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))