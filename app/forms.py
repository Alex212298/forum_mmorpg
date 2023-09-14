from django.forms import ModelForm, Textarea
from .models import Posts, Repsponses

from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group

class AddPostForm(ModelForm):
    class Meta:
        model = Posts
        fields = ['heading', 'category', 'content', 'text']

class AddResp(ModelForm):
    class Meta:
        model = Repsponses
        fields = ['resp_text']
