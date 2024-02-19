from django import forms
from .models import Category

class NewsForm(forms.Form):
    title = forms.CharField(max_length=150, label='Title news', widget=forms.TextInput(attrs={"class":"form-control"}))
    content = forms.CharField(label="Conten news", required=False, widget=forms.Textarea(attrs={"class":"form-control","rows":5}))
    is_published = forms.BooleanField(label="Is published?", initial=True)
    category = forms.ModelChoiceField(empty_label="Select Category",queryset=Category.objects.all(), widget=forms.Select(attrs={"class":"form-control"}))
