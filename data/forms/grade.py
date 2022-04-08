from data  import  models
from django.forms import ModelForm
from django import  forms
#校验输入的设备信息字段不能为空
class GradeModelForm(ModelForm):
    class Meta:
        model = models.Grade
        fields = "__all__"
        widgets = {
            'grade_name':forms.TextInput(attrs={'class':'form-control','placeholder':'班级名称'}),
        }
        error_messages = {
            'grade_name':{
                'required':'不能为空'
            },
        }