from data  import  models
from django.forms import ModelForm
from django import  forms
#校验输入的设备信息字段不能为空
class ZhuanModelForm(ModelForm):
    class Meta:
        model = models.Zhuanye
        fields = "__all__"
        widgets = {
            'zhuanye_name':forms.TextInput(attrs={'class':'form-control','placeholder':'专业名称'}),
        }
        error_messages = {
            'zhuanye_name':{
                'required':'不能为空'
            },
        }