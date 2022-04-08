from data  import  models
from django.forms import ModelForm
from django import  forms
#校验输入的设备信息字段不能为空
class KeModelForm(ModelForm):
    class Meta:
        model = models.Kecheng
        fields = "__all__"
        widgets = {
            'kecheng_name':forms.TextInput(attrs={'class':'form-control','placeholder':'课程名称'}),
        }
        error_messages = {
            'kecheng_name':{
                'required':'不能为空'
            },
        }