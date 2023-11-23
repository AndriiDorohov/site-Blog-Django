from django import forms
from .models import Article, Profile
from django.forms import ModelForm, TextInput, Textarea, Select, FileInput
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from tinymce.widgets import TinyMCE


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ["title", "summary", "full_text", "category", "slug", "og_image"]
        widgets = {
            "title": TextInput(attrs={"class": "form-control", "placeholder": "Title"}),
            "summary": Textarea(
                attrs={"class": "form-control", "placeholder": "Summary"}
            ),
            "full_text": Textarea(
                attrs={"class": "form-control", "placeholder": "Full Text"}
            ),
            "category": Select(
                attrs={
                    "class": "form-control",
                }
            ),
            "slug": TextInput(attrs={"class": "form-control", "placeholder": "Slug"}),
            "og_image": FileInput(
                attrs={
                    "class": "form-control",
                }
            ),
        }


class CommentForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={"rows": 4, "cols": 50}))


class RegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.pop("autofocus", None)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Name", required=True)


class ArticleSearchForm(forms.Form):
    query = forms.CharField(
        label="Search Articles",
        max_length=100,
        widget=forms.TextInput(attrs={"placeholder": "Search for articles..."}),
    )


class NewsletterForm(forms.Form):
    subject = forms.CharField()
    receivers = forms.CharField()
    message = forms.CharField(widget=TinyMCE(), label="Email content")


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')

        if User.objects.filter(username=username).exists():
            self.add_error('username', 'Username is already taken.')

        if User.objects.filter(email=email).exists():
            self.add_error('email', 'This email is already registered.')

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    telephone = forms.CharField(max_length=15, required=False)
    bio = forms.CharField(widget=forms.Textarea, required=False)
    location = forms.CharField(max_length=100, required=False)
    birth_date = forms.DateField(required=False)
    twitter_url = forms.URLField(required=False)
    facebook_url = forms.URLField(required=False)
    instagram_url = forms.URLField(required=False)
    youtube_url = forms.URLField(required=False)
    image = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-profile-image'}))


    class Meta:
        model = Profile
        fields = ['telephone', 'bio', 'location', 'birth_date', 'twitter_url', 'facebook_url', 'instagram_url', 'youtube_url', 'image']
