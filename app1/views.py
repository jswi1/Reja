import django.http
from django.shortcuts import render, redirect
from .models import Student, Reja

def students(request):
    if request.method == 'POST':
        Student.objects.create(
            ism=request.POST.get("ismi"),
            yosh=request.POST.get("y"),
            nechinchi_kurs=request.POST.get("n_k"),
            student_raqami=request.POST.get("s_t"),
        )
    db = request.GET.get("qidirish")
    if db == None:
        hamma = Student.objects.all().order_by("ism")
    else:
        hamma = Student.objects.filter(ism=db)
    return render(request, "studentlar.html", {"students":hamma})

def stu_qoshish(request, ch):
    if request.method =='POST':
        s1 = Student.objects.get(id=ch)
        s1.ism.objects.get("ismi")
        s1.yosh.objects.get("y")
        s1.nechinchi_kurs.objects.get("n_k")
        s1.student_raqami.objects.get("s_t")
        return redirect("/students")
    s = Student.objects.get(id=ch)
    return render(request, "stu_edit.html", {"student":s})

def rejalar(request):
    if request.method == 'POST':
        if request.POST.get("s") == "True":
            natija = False
        else:
            natija = True
        Reja.objects.create(
            sarlavha=request.POST.get("s"),
            sana=request.POST.get("sana"),
            batafsil=request.POST.get("b"),
            bajarildi=request.POST.get("bajarildi"),
            student=stu
        )
    s = Student.objects.all()
    return render(request, "rejalar.html", {"stu": s})
