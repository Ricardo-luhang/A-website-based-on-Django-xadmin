from django import forms
from captcha.fields import CaptchaField
from apps.user.models import UserInfo


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    captcha = CaptchaField()


class ForgetForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField('验证码错误')


class ModefyForm(forms.Form):
    password1 = forms.CharField(required=True, min_length=5)
    password2 = forms.CharField(required=True, min_length=5)


class UploadIamgForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['image']


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['nick_name', 'birth_day', 'gender', 'address', 'mobile_num']
