from data  import  models
from django.forms import ModelForm
from django import  forms
#校验输入的设备信息字段不能为空
class BatchModelForm(ModelForm):
    class Meta:
        model = models.Batch
        fields = "__all__"
        widgets = {
            'batch_name':forms.TextInput(attrs={'class':'form-control','placeholder':'考试批次'}),
        }
        error_messages = {
            'batch_name':{
                'required':'不能为空'
            },
        }