from django import forms
from app.models import *

class TopicForm(forms.ModelForm):
    class Meta():
        model=Topic
        fields="__all__"
    
class WebpageForm(forms.ModelForm):
    class Meta():
        model=Webpage
        fields="__all__"
        #fields=['topic_name','name']#here it will get only topic_name and name
        #exclude=['topic_name','name']#here it will get only url and email
        #labels={'topic_name':'Topic','url':'u'}#it will change their actualcolumn name to usercolumn name
        widgets={'name':forms.PasswordInput,'url':forms.PasswordInput}# it will update the data into password


class AccessRecordForm(forms.ModelForm):
    class Meta():
        model=AccessRecord
        fields="__all__"
        #fields=['name','author']#here it will take only name and author
        #exclude=['name','author']# here it will take only date
        #labels={'name':'NAME','date':'DATE'}#here it will change their column name into user given name
        widgets={'author':forms.PasswordInput}#it will change into password 

