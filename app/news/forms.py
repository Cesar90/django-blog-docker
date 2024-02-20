from django import forms
from .models import Category, News
import re
from django.core.exceptions import ValidationError

# class NewsForm(forms.Form):
    # title = forms.CharField(max_length=150, label='Title news', widget=forms.TextInput(attrs={"class":"form-control"}))
    # content = forms.CharField(label="Conten news", required=False, widget=forms.Textarea(attrs={"class":"form-control","rows":5}))
    # is_published = forms.BooleanField(label="Is published?", initial=True)
    # category = forms.ModelChoiceField(empty_label="Select Category",queryset=Category.objects.all(), widget=forms.Select(attrs={"class":"form-control"}))
    
class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        # fields = '__all__'
        fields = ['title','content','is_published','category']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'content': forms.Textarea(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class':'form-control'}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match('\d', title):
            raise ValidationError("Title contains number")
        return title