from django.contrib.auth import get_user_model
from django import forms
from allauth.account.forms import SignupForm


class UserCreateForm(SignupForm):
    class Meta:
        fields = ("first_name", "last_name", "email", "username", "password1", "password2")
        model = get_user_model()
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].label = ''
        self.fields["first_name"].widget.attrs["placeholder"] = "First Name"
        self.fields["last_name"].label = ''
        self.fields["last_name"].widget.attrs["placeholder"] = "Last Name"
        self.fields["email"].label = ''
        self.fields["email"].widget.attrs["placeholder"] = "Email"
        self.fields["username"].label = ''
        self.fields["username"].widget.attrs["placeholder"] = "Username"
        self.fields["password1"].label = ''
        self.fields["password1"].widget.attrs["placeholder"] = "Password"
        self.fields["password2"].label = ''
        self.fields["password2"].widget.attrs["placeholder"] = "Confirm Password"