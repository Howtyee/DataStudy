from django.db import models

# Create your models here.

# 账户表信息
class UserManager(models.Model):
    username = models.CharField(verbose_name="用户名", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=64)
    usertype = models.CharField(verbose_name='用户类型', max_length=32)
    def __str__(self):
        return self.username

#班级表
class Grade(models.Model):
    grade_name = models.CharField(verbose_name="班级名称",max_length=128)
    def __str__(self):
        return self.grade_name

class Kecheng(models.Model):
    kecheng_name = models.CharField(verbose_name="课程名称",max_length=128)
    def __str__(self):
        return self.kecheng_name

class Zhuanye(models.Model):
    zhuanye_name = models.CharField(verbose_name="专业名称",max_length=128)
    def __str__(self):
        return self.zhuanye_name


#考试批次表
class Batch(models.Model):
    batch_name = models.CharField(verbose_name="考试批次",max_length=128)
    def __str__(self):
        return self.batch_name

#学生信息表
class Student(models.Model):
    numid = models.CharField(verbose_name="学号",max_length=128)
    name = models.CharField(verbose_name="姓名",max_length=128)
    grade = models.ForeignKey(verbose_name="所属班级",to=Grade,on_delete=models.CASCADE)
    birth = models.CharField(verbose_name="生日",max_length=128)
    gender_choice = (
        (1, '男'),
        (2, '女'),
    )
    gender = models.IntegerField(verbose_name='性别', choices=gender_choice)
    study_time = models.CharField(verbose_name="入学时间",max_length=128)
    password = models.CharField(verbose_name="登陆密码",max_length=64)
    addr = models.CharField(verbose_name="家庭地址",max_length=128)
    number = models.CharField(verbose_name="身份证",max_length=128)
    other = models.CharField(verbose_name="备注",max_length=128)
    def __str__(self):
        return self.name

#学生选择课程表
class SelectGrade(models.Model):
    name = models.CharField(verbose_name="姓名", max_length=128)
    kecheng_name = models.ForeignKey(verbose_name="班级名称", to=Kecheng,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

#成绩表
class Score(models.Model):
    grade_name = models.ForeignKey(verbose_name="所属班级",to=Grade,on_delete=models.CASCADE)
    batch_name = models.ForeignKey(verbose_name="所属考试批次",to=Batch,on_delete=models.CASCADE)
    stu_name = models.ForeignKey(verbose_name="选择学生姓名",to=Student,on_delete=models.CASCADE)
    project = models.CharField(verbose_name="科目", max_length=128)
    score = models.IntegerField(verbose_name="成绩", max_length=128)
    def __str__(self):
        return self.project

#教师表
class Teacher(models.Model):
    numid = models.CharField(verbose_name="工号", max_length=128)
    name = models.CharField(verbose_name="姓名", max_length=128)
    grade = models.ForeignKey(verbose_name="所带班级", to=Grade, on_delete=models.CASCADE)
    birth = models.CharField(verbose_name="生日", max_length=128)
    gender_choice = (
        (1, '男'),
        (2, '女'),
    )
    gender = models.IntegerField(verbose_name='性别', choices=gender_choice)
    study_time = models.CharField(verbose_name="入职时间", max_length=128)
    password = models.CharField(verbose_name="登陆密码", max_length=64)
    addr = models.CharField(verbose_name="家庭地址", max_length=128)
    number = models.CharField(verbose_name="身份证", max_length=128)
    other = models.CharField(verbose_name="备注", max_length=128)

    def __str__(self):
        return self.numid















