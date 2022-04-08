from data  import  models
from django.forms import ModelForm
from django import  forms
#校验输入的设备信息字段不能为空
class StudentModelForm(ModelForm):
    class Meta:
        model = models.Student
        fields = "__all__"
        widgets = {
            'numid':forms.TextInput(attrs={'class':'form-control','placeholder':'学号'}),
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'姓名'}),
            'grade':forms.Select(attrs={'class':'form-control','placeholder':'所属班级'}),
            'birth':forms.TextInput(attrs={'class':'form-control','placeholder':'生日'}),
            'gender':forms.Select(attrs={'class':'form-control','placeholder':'性别'}),
            'study_time':forms.TextInput(attrs={'class':'form-control','placeholder':'入学时间'}),
            'password':forms.TextInput(attrs={'class':'form-control','placeholder':'登陆密码'}),
            'addr':forms.TextInput(attrs={'class':'form-control','placeholder':'家庭地址'}),
            'number':forms.TextInput(attrs={'class':'form-control','placeholder':'身份证号'}),
            'other':forms.TextInput(attrs={'class':'form-control','placeholder':'备注'}),
        }
        error_messages = {
            'numid':{
                'required':'不能为空'
            },
            'name': {
                'required': '不能为空'
            },
            'grade': {
                'required': '不能为空'
            },
            'birth': {
                'required': '不能为空'
            },
            'gender': {
                'required': '不能为空'
            },
            'study_time': {
                'required': '不能为空'
            },
            'password': {
                'required': '不能为空'
            },
            'addr': {
                'required': '不能为空'
            },
            'number': {
                'required': '不能为空'
            },
            'other': {
                'required': '不能为空'
            },
        }