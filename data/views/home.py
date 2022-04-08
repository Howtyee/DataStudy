from django.shortcuts import HttpResponse,render,redirect
from data import models
from data.forms.grade import GradeModelForm
from data.forms.batch import BatchModelForm
from data.forms.student import StudentModelForm
from data.forms.teach import TeachModelForm
from data.forms.score import ScoreModelForm
from data.forms.kecheng import KeModelForm
from data.forms.zhuanye import ZhuanModelForm
from data.forms.selectke import SelectKeModelForm

from functools import wraps
STU = {"status":None}
TEA = {"status":None}

def check_login(func):
    @wraps(func)  #装饰器修复技术
    def inner(request,*args,**kwargs):
        #已经登录过的继续执行
        ret = request.get_signed_cookie("is_login", default="0", salt="dsb")
        if ret == "1":
            return func(request,*args,**kwargs)
        #没有登录过的跳转登录界面
        else:
            #获取当前访问的URl
            next_url = request.path_info
            print(next_url)
            return redirect("/data/login/?next={}".format(next_url))
    return inner

@check_login
def index(request):
    return render(request,'index.html')
@check_login
def stuindex(request):
    return render(request,'stuindex.html')
@check_login
def teaindex(request):
    return render(request,'teaindex.html')

# @check_login
def login(request):
    errmsg = ""
    if request.method == "POST":
        usertype = request.POST['seltype']
        username = request.POST['username']
        password = request.POST['password']
        next_url = request.GET.get("next")
        if usertype == "学生":
            stu_obj = models.Student.objects.filter(name=username,password=password)
            if stu_obj:
                STU["status"] = username
                if next_url:
                    rep = redirect(next_url)
                else:
                    rep = redirect('/data/stuindex/')
                rep.set_signed_cookie("is_login", "1", salt="dsb", max_age=60 * 60 * 24 * 7)
                return rep
            else:
                return render(request, 'login.html', {"errmsg": "用户名或密码输入错误"})
        elif usertype == "教师":
            tea_obj = models.Teacher.objects.filter(name=username,password=password)
            if tea_obj:
                TEA["status"] = username
                if next_url:
                    rep = redirect(next_url)
                else:
                    rep = redirect('/data/teaindex/')
                rep.set_signed_cookie("is_login", "1", salt="dsb", max_age=60 * 60 * 24 * 7)
                return rep
            else:
                return render(request, 'login.html', {"errmsg": "用户名或密码输入错误"})
        else:
            object = models.UserManager.objects.filter(username=username, password=password)
            if object:
                if next_url:
                    rep = redirect(next_url)
                else:
                    rep = redirect('/data/index/')
                rep.set_signed_cookie("is_login", "1", salt="dsb", max_age=60 * 60 * 24 * 7)
                return rep
            else:
                return render(request, 'login.html', {"errmsg": "用户名或密码输入错误"})
    return render(request, 'login.html')

def logout(request):
    rep = redirect("/data/login/")
    rep.delete_cookie("is_login")
    return rep

def stulogout(request):
    rep = redirect("/data/login/")
    rep.delete_cookie("is_login")
    STU['status'] = None
    return rep

def tealogout(request):
    rep = redirect("/data/login/")
    rep.delete_cookie("is_login")
    TEA['status'] = None
    return rep



#班级信息展示
@check_login
def teachgradeinfolist(request):
    grade_queryset = models.Grade.objects.all()
    return render(request, 'teachgradeinfolist.html', {"grade_queryset": grade_queryset})
def teachkechenginfolist(request):
    grade_queryset = models.Kecheng.objects.all()
    return render(request, 'teachkechenginfolist.html', {"grade_queryset": grade_queryset})
def teachzhuanyeinfolist(request):
    grade_queryset = models.Zhuanye.objects.all()
    return render(request, 'teachzhuanyeinfolist.html', {"grade_queryset": grade_queryset})
#班级信息展示
@check_login
def gradeinfolist(request):
    grade_queryset = models.Grade.objects.all()
    return render(request, 'gradeinfolist.html', {"grade_queryset": grade_queryset})

#管理员添加班级信息函数
@check_login
def addgradeinfo(request):
    if request.method == "GET":
        form = GradeModelForm()
        return render(request, 'grade_form.html', {"form": form})
    form = GradeModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/data/gradeinfolist/')
    return render(request, 'grade_form.html', {"form": form})

#管理员编班级信息函数
@check_login
def editgradeinfo(request, nid):
    obj = models.Grade.objects.filter(id=nid).first()
    if request.method == "GET":
        form = GradeModelForm(instance=obj)
        return render(request, 'grade_form.html', {"form": form})
    form = GradeModelForm(data=request.POST, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/data/gradeinfolist/')
    return render(request, 'grade_form.html', {"form": form})

#管理员删除班级信息函数
@check_login
def delgradeinfo(request, nid):
    models.Grade.objects.filter(id=nid).delete()
    return redirect('/data/gradeinfolist/')



#批次信息展示
@check_login
def batchinfolist(request):
    batch_queryset = models.Batch.objects.all()
    return render(request, 'batchinfolist.html', {"batch_queryset": batch_queryset})

#管理员添加批次信息函数
@check_login
def addbatchinfo(request):
    if request.method == "GET":
        form = BatchModelForm()
        return render(request, 'batch_form.html', {"form": form})
    form = BatchModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/data/batchinfolist/')
    return render(request, 'batch_form.html', {"form": form})

#管理员编批次信息函数
@check_login
def editbatchinfo(request, nid):
    obj = models.Batch.objects.filter(id=nid).first()
    if request.method == "GET":
        form = BatchModelForm(instance=obj)
        return render(request, 'batch_form.html', {"form": form})
    form = BatchModelForm(data=request.POST, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/data/batchinfolist/')
    return render(request, 'batch_form.html', {"form": form})

#管理员删除批次信息函数
@check_login
def delbatchinfo(request, nid):
    models.Batch.objects.filter(id=nid).delete()
    return redirect('/data/batchinfolist/')




#学生个人信息展示
@check_login
def studentinfolist(request):
    student_queryset = models.Student.objects.filter(name=STU['status']).all()
    return render(request, 'studentinfolist.html', {"student_queryset": student_queryset})

#添加学生个人信息函数
@check_login
def addstudentinfo(request):
    if request.method == "GET":
        form = StudentModelForm()
        return render(request, 'student_form.html', {"form": form})
    form = StudentModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/data/studentinfolist/')
    return render(request, 'student_form.html', {"form": form})

#编学生个人信息函数
@check_login
def editstudentinfo(request, nid):
    obj = models.Student.objects.filter(id=nid).first()
    if request.method == "GET":
        form = StudentModelForm(instance=obj)
        return render(request, 'student_form.html', {"form": form})
    form = StudentModelForm(data=request.POST, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/data/studentinfolist/')
    return render(request, 'student_form.html', {"form": form})

#删除学生个人信息函数
@check_login
def delstudentinfo(request, nid):
    models.Student.objects.filter(id=nid).delete()
    return redirect('/data/studentinfolist/')


#学生个人信息展示
@check_login
def adminstudentinfolist(request):
    student_queryset = models.Student.objects.all()
    return render(request, 'adminstudentinfolist.html', {"student_queryset": student_queryset})

#管理员添加学生个人信息函数
@check_login
def addadminstudentinfo(request):
    if request.method == "GET":
        form = StudentModelForm()
        return render(request, 'adminstudent_form.html', {"form": form})
    form = StudentModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/data/adminstudentinfolist/')
    return render(request, 'adminstudent_form.html', {"form": form})

#管理员编学生个人信息函数
@check_login
def editadminstudentinfo(request, nid):
    obj = models.Student.objects.filter(id=nid).first()
    if request.method == "GET":
        form = StudentModelForm(instance=obj)
        return render(request, 'adminstudent_form.html', {"form": form})
    form = StudentModelForm(data=request.POST, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/data/adminstudentinfolist/')
    return render(request, 'adminstudent_form.html', {"form": form})

#管理员删除学生个人信息函数
@check_login
def deladminstudentinfo(request, nid):
    models.Student.objects.filter(id=nid).delete()
    return redirect('/data/adminstudentinfolist/')


#修改学生密码
@check_login
def stupasswdlist(request):
    if request.method == "POST":
        password = request.POST['passwd']
        obj = models.Student.objects.filter(name=STU['status']).all().first()
        obj.password = password
        obj.save()
        return  render(request,'stupasswdsuccess.html')
    return render(request,'stupasswdlist.html')


@check_login
def teapasswdlist(request):
    if request.method == "POST":
        password = request.POST['passwd']
        obj = models.Teacher.objects.filter(name=TEA['status']).all().first()
        obj.password = password
        obj.save()
        return  render(request,'teapasswdsuccess.html')
    return render(request,'teapasswdlist.html')

#教师个人信息展示
@check_login
def teachinfolist(request):
    teach_queryset = models.Teacher.objects.filter(name=TEA['status']).all()
    return render(request, 'teachinfolist.html', {"teach_queryset": teach_queryset})

#添加教师个人信息函数
@check_login
def addteachinfo(request):
    if request.method == "GET":
        form = TeachModelForm()
        return render(request, 'teach_form.html', {"form": form})
    form = TeachModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/data/teachinfolist/')
    return render(request, 'teach_form.html', {"form": form})

#编教师个人信息函数
@check_login
def editteachinfo(request, nid):
    obj = models.Teacher.objects.filter(id=nid).first()
    if request.method == "GET":
        form = TeachModelForm(instance=obj)
        return render(request, 'teach_form.html', {"form": form})
    form = TeachModelForm(data=request.POST, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/data/teachinfolist/')
    return render(request, 'teach_form.html', {"form": form})

#删除教师个人信息函数
@check_login
def delteachinfo(request, nid):
    models.Teacher.objects.filter(id=nid).delete()
    return redirect('/data/teachinfolist/')

#教师个人信息展示
@check_login
def teainfolist(request):
    teach_queryset = models.Teacher.objects.all()
    return render(request, 'teainfolist.html', {"teach_queryset": teach_queryset})

#管理员添加教师个人信息函数
@check_login
def addteainfo(request):
    if request.method == "GET":
        form = TeachModelForm()
        return render(request, 'tea_form.html', {"form": form})
    form = TeachModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/data/teainfolist/')
    return render(request, 'tea_form.html', {"form": form})

#管理员编教师个人信息函数
@check_login
def editteainfo(request, nid):
    obj = models.Teacher.objects.filter(id=nid).first()
    if request.method == "GET":
        form = TeachModelForm(instance=obj)
        return render(request, 'tea_form.html', {"form": form})
    form = TeachModelForm(data=request.POST, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/data/teainfolist/')
    return render(request, 'tea_form.html', {"form": form})

#管理员删除教师个人信息函数
@check_login
def delteainfo(request, nid):
    models.Teacher.objects.filter(id=nid).delete()
    return redirect('/data/teainfolist/')

#选择批次查看
@check_login
def search(request):
    if request.method == "POST":
        batch_name = request.POST["systype"]
        print("===================")
        print(batch_name)
        score_queryset = models.Score.objects.filter(batch_name=batch_name).all()
        queryset = models.Batch.objects.all()
        return render(request, 'studentscore.html', {"score_queryset": score_queryset, "queryset": queryset})

@check_login
def studentorderscore(request):
    score_queryset = models.Score.objects.order_by('-score').all()
    return render(request, 'studentscore.html', {"score_queryset": score_queryset})

@check_login
def studentselectgradelist(request):
    score_queryset = models.SelectGrade.objects.filter(name=STU['status']).all()
    return render(request, 'studentselectkechenglist.html', {"student_queryset": score_queryset})

@check_login
def addstudentselectgradelist(request):
    if request.method == "GET":
        form = SelectKeModelForm()
        return render(request, 'student_form.html', {"form": form})
    form = SelectKeModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/data/studentselectgradelist/')
    return render(request, 'student_form.html', {"form": form})


@check_login
def editstudentselectgradelist(request,nid):
    obj = models.SelectGrade.objects.filter(id=nid).first()
    if request.method == "GET":
        form = SelectKeModelForm(instance=obj)
        return render(request, 'student_form.html', {"form": form})
    form = SelectKeModelForm(data=request.POST, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/data/studentselectgradelist/')
    return render(request, 'student_form.html', {"form": form})


@check_login
def delstudentselectgradelist(request,nid):
    models.SelectGrade.objects.filter(id=nid).delete()
    return redirect('/data/studentselectgradelist/')


#学生成绩信息展示
@check_login
def studentscoreinfolist(request):
    score_queryset = models.Score.objects.all()
    queryset = models.Batch.objects.all()
    return render(request, 'studentscore.html', {"score_queryset": score_queryset,"queryset":queryset})

#成绩信息展示
@check_login
def scoreinfolist(request):
    score_queryset = models.Score.objects.all()
    return render(request, 'scoreinfolist.html', {"score_queryset": score_queryset})

#管理员看到的成绩信息展示
@check_login
def adminscoreinfolist(request):
    score_queryset = models.Score.objects.all()
    return render(request, 'adminscoreinfolist.html', {"score_queryset": score_queryset})

#管理员添加教师个人信息函数
@check_login
def addscoreinfo(request):
    if request.method == "GET":
        form = ScoreModelForm()
        return render(request, 'score_form.html', {"form": form})
    form = ScoreModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/data/scoreinfolist/')
    return render(request, 'score_form.html', {"form": form})

#管理员编教师个人信息函数
@check_login
def editscoreinfo(request, nid):
    obj = models.Score.objects.filter(id=nid).first()
    if request.method == "GET":
        form = ScoreModelForm(instance=obj)
        return render(request, 'score_form.html', {"form": form})
    form = ScoreModelForm(data=request.POST, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/data/scoreinfolist/')
    return render(request, 'score_form.html', {"form": form})


@check_login
def delscoreinfo(request, nid):
    models.Score.objects.filter(id=nid).delete()
    return redirect('/data/scoreinfolist/')


@check_login
def adminkechenginfolist(request):
    kecheng_queryset = models.Kecheng.objects.all()
    return render(request, 'adminkechenginfolist.html', {"kecheng_queryset": kecheng_queryset})


@check_login
def addadminkechenginfolist(request):
    if request.method == "GET":
        form = KeModelForm()
        return render(request, 'grade_form.html', {"form": form})
    form = KeModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/data/adminkechenginfolist/')
    return render(request, 'grade_form.html', {"form": form})


@check_login
def editadminkechenginfolist(request, nid):
    obj = models.Kecheng.objects.filter(id=nid).first()
    if request.method == "GET":
        form = KeModelForm(instance=obj)
        return render(request, 'grade_form.html', {"form": form})
    form = KeModelForm(data=request.POST, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/data/adminkechenginfolist/')
    return render(request, 'grade_form.html', {"form": form})

@check_login
def deladminkechenginfolist(request, nid):
    models.Kecheng.objects.filter(id=nid).delete()
    return redirect('/data/adminkechenginfolist/')



@check_login
def adminzhuanyeinfolist(request):
    zhuanye_queryset = models.Zhuanye.objects.all()
    return render(request, 'adminzhuanyeinfolist.html', {"zhuanye_queryset": zhuanye_queryset})


@check_login
def addadminzhuanyeinfolist(request):
    if request.method == "GET":
        form = ZhuanModelForm()
        return render(request, 'grade_form.html', {"form": form})
    form = ZhuanModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/data/adminzhuanyeinfolist/')
    return render(request, 'grade_form.html', {"form": form})


@check_login
def editadminzhuanyeinfolist(request, nid):
    obj = models.Zhuanye.objects.filter(id=nid).first()
    if request.method == "GET":
        form = ZhuanModelForm(instance=obj)
        return render(request, 'grade_form.html', {"form": form})
    form = ZhuanModelForm(data=request.POST, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/data/adminzhuanyeinfolist/')
    return render(request, 'grade_form.html', {"form": form})

@check_login
def deladminzhuanyeinfolist(request, nid):
    models.Zhuanye.objects.filter(id=nid).delete()
    return redirect('/data/adminzhuanyeinfolist/')