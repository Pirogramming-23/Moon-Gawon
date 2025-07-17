from django import forms
from .models import DevTool
from .models import Idea

class DevToolForm(forms.ModelForm):
    class Meta:
        model = DevTool
        fields = ['name', 'type', 'description']
        labels = {
            'name': '툴 이름',
            'type': '툴 종류',
            'description': '툴 설명',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': '툴 이름'}),
            'type': forms.TextInput(attrs={'placeholder': '툴 종류'}),
            'description': forms.Textarea(attrs={'placeholder': '툴 설명'}),
        }

from django import forms
from .models import Idea, DevTool  # DevTool 모델이 있어야 함

class IdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields = ['title', 'dev_tool', 'interest', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': '아이디어 제목'}),
            'dev_tool': forms.Select(),  # 드롭다운 설정
            'interest': forms.NumberInput(attrs={
                'placeholder': '0~100',
                'min': 0,
                'max': 100
            }),
            'content': forms.Textarea(attrs={'placeholder': '아이디어 설명'}),
        }