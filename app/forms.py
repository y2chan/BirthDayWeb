from django import forms
from .models import Message, Photo

class MessageForm(forms.ModelForm):
    # 필드를 명시적으로 정의하고, 레이블을 변경합니다.
    nickname = forms.CharField(label='이름')
    message = forms.CharField(label='서윤이에게 하고 싶은 말', widget=forms.Textarea)

    class Meta:
        model = Message
        fields = ['nickname', 'message', 'image']


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image', 'description']
