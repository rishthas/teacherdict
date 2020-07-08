
import csv,io
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Subject,Teacher
from .forms import CreateNewTeacher
from django.contrib import messages

def index(request):
    context={}
    if request.method == "POST":
        form    =   CreateNewTeacher(request.POST,request.FILES)
        if form.is_valid():
            tech = form.save()
            context['form']= form
            context["id"] = tech.id
            
    else:
        form = CreateNewTeacher()
        context['form']= form
        
    return render(request,'app/index.html',context)


def listTeachers(request):
    subjects = Subject.objects.all()
    teacherLastList=[]
    context={}
    if request.method == "POST":
        if request.POST.get('last_name') and request.POST.get('subject').strip():
            print("=============In First Condition===========")
            teacherList = Teacher.objects.filter(last_name__startswith=request.POST.get('last_name')).filter(subjects__id=request.POST.get('subject')).all()
        elif request.POST.get('last_name') and not request.POST.get('subject').strip():
            print("=============In Second Condition===========")
            teacherList = Teacher.objects.filter(last_name__startswith=request.POST.get('last_name')).all()
        elif not request.POST.get('last_name').strip() and request.POST.get('subject').strip():
            print("=============In Second Condition===========")
            teacherList = Teacher.objects.filter(subjects__id=request.POST.get('subject')).all()
        else:
            print("=============In Last Condition===========")
            teacherList = Teacher.objects.all()     
            
    else:
        teacherList = Teacher.objects.all()
    
    for teacher in teacherList:
        teach = {}
        teach["id"] = teacher.id
        teach["first_name"] = teacher.last_name
        teach["last_name"] = teacher.last_name
        teach["email_id"] = teacher.email_id
        teach["subjects"] = []
        for subject in teacher.subjects.all(): 
            subjectJSON = {}
            subjectJSON["subject_name"] = subject.subject_name
            teach["subjects"].append(subjectJSON)

        teacherLastList.append(teach)
    print(teacherLastList)
    context['teacherList'] =   teacherLastList
    context['subjects'] = subjects
    return render(request,'app/listTeachers.html',context)

def teacher(request,inid):
    teacher= Teacher.objects.get(id=inid)
    print(teacher)
    context={ 'teacher':teacher }
    return render(request,'app/teacher.html',context)


def upload(request):
    prompt = {
        "order":"Order of CSV should be first_name,last_name,profil_pic,email_id,phone_no,room_no,subjects"
    }
    if request.method == "GET":
        return render(request,'app/upload_csv.html',prompt)
    
    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request,'Not a csv file!')
        return render(request,'app/upload_csv.html',prompt)
    
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)

    for column in csv.reader(io_string,delimiter=','):
        if not Teacher.objects.filter(email_id= column[3].strip()).exists():
            teacher = Teacher(
                first_name  =   column[0],
                last_name   =   column[1],
                profil_pic  =   column[2],
                email_id    =   column[3],
                phone_no    =   column[4],
                room_no     =   column[5]
            )
            
            subjects = column[6].strip().split(',')
            for subject in subjects:
                if not Subject.objects.filter(subject_name=subject.strip()).exists():
                    sub=Subject(subject_name=subject.strip(),subject_desc=subject.strip())
                    sub.save()
                else:
                    sub=Subject.objects.filter(subject_name=subject.strip())
                    sub.save()
                teacher.subjects.add(sub)
            teacher.save()last_name
            print(subjects)
    messages.success(request,'All the details are uploaded')
    return render(request,'app/upload_csv.html',prompt)


