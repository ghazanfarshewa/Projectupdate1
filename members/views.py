from multiprocessing import context
from django import template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member
from .forms import MemberForm
from django.shortcuts import redirect
 
 


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



 


def delete_object_function(request, id):
    # OrderSparePart is the Model of which the object is present

    mymember = Member.objects.get(id=id)
    mymember.delete()
    return HttpResponse(template.render(context, request))
  
  
