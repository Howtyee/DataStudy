from data  import  models
from django.forms import ModelForm
from django import  forms
#校验输入的设备信息字段不能为空
class SelectKeModelForm(ModelForm):
    class Meta:
        model = models.SelectGrade
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '学生名称'}),
            'kecheng_name':forms.Select(attrs={'class':'form-control','placeholder':'课程名称'}),

        }
        error_messages = {
            'name':{
                'required':'不能为空'
            },
            'kecheng_name': {
                'required': '不能为空'
            },
        }