import imp
from multiprocessing import context
from django.shortcuts import render,redirect
from .models import Note
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import json
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.template.defaultfilters import slugify
# Create your views here.
def homepage(request):
    notes = Note.objects.all()
    
    context = {
        'notes':notes
    }
    return render(request,'homepage.html',context)

def loginPopup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request,username = username,password = password)
        
        if user is not None:
            login(request,user)
            messages.success(request,'Logged in Successfully')
            return redirect("homepage")
        else:
            messages.success(request,'Logged in Successfully')
            return redirect("homepage")

def loginPage(request):
    
    pass        

@login_required
def add_note(request):
    if request.method == "POST":
        title = request.POST.get("title")
        github_link = request.POST.get("github_link")
        description = request.POST.get("description")
        # images = request.POST.get("images")
        steps = request.POST.getlist("steps")
        
        print(steps)
        slug = slugify(title)
        # Saving into the DB model Note
        note = Note.objects.create(
            title = title,
            description = description,
            github_link = github_link,
            slug=slug
        )
        
        
        # Saving steps into a dictionary to save into the model
        steps_list = []
        count = 1
        for step in steps:
            steps_list.append({str(count) : step})
            count+=1
        note.json_steps = json.dumps(steps_list)
        
        note.save()
    
    return render(request,'utils/create_form.html')


def note_details(request,slug):
    
    note = Note.objects.get(slug = slug)
    
    note_steps = json.loads(note.json_steps)
    keys = []
    vals = []
    list_of_list = []
    for i in note_steps:
        temp = []
        for k in i.keys():
            # keys.append(k)
            temp.append(k)
        for v in i.values():
            temp.append(v)
            # vals.append(v)
        list_of_list.append(temp)
        
    print(list_of_list)
    note_lists = list(note_steps)
    # print(note_lists)
    context = {
        'note':note,
        'steps':list_of_list
    }    
    return render(request,'details.html',context)

def search_view(request):

    if request.is_ajax():
        res= None
        string = request.POST.get('note')
        notes = Note.objects.filter(title__icontains = string)
        if len(notes) > 0 and len(string) > 0:
            print(len(notes))
            data = []
            for pos in notes:
                item = {
                    "pk":pos.pk,
                    "title":pos.title,
                    "slug":pos.slug
                }
                data.append(item)
            res = data
        else:
            res = "No Note Found..."
            
        return JsonResponse({'data':res})
    
    return JsonResponse("{}")


def suggest_edit(request,slug):
    
    return render(request,'utils/edit_form.html')