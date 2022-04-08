from data  import  models
from django.forms import ModelForm
from django import  forms
#校验输入的设备信息字段不能为空
class ScoreModelForm(ModelForm):
    class Meta:
        model = models.Score
        fields = "__all__"
        widgets = {
            'grade_name':forms.Select(attrs={'class':'form-control','placeholder':'所属班级'}),
            'batch_name':forms.Select(attrs={'class':'form-control','placeholder':'考试批次'}),
            'stu_name':forms.Select(attrs={'class':'form-control','placeholder':'学生姓名'}),
            'project':forms.TextInput(attrs={'class':'form-control','placeholder':'科目'}),
            'score':forms.TextInput(attrs={'class':'form-control','placeholder':'成绩'}),
        }
        error_messages = {
            'grade_name':{
                'required':'不能为空'
            },
            'batch_name': {
                'required': '不能为空'
            },
            'stu_name': {
                'required': '不能为空'
            },
            'project': {
                'required': '不能为空'
            },
            'score': {
                'required': '不能为空'
            },
        }