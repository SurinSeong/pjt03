from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    stock_name = forms.CharField(max_length=100)

    class Meta:
        model = Comment
        fields = ('stock_name', )    # 사용자로부터 입력받을 필드