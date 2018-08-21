from django.shortcuts import render, redirect
from apps.utils.mixin_utils import LoginRequireMixin
from django.views.generic import View
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
import json
from django.core.urlresolvers import reverse

from apps.user.models import UserInfo, EmailCaptcha, Viewpager
from apps.user.form import LoginForm, RegisterForm, ForgetForm, ModefyForm, UploadIamgForm, UserInfoForm
from apps.utils.email_send import send_email
from apps.operations.models import UserCourse
from apps.course.models import Course, Organizations


class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserInfo.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class ActiveView(View):
    def get(self, request, active_code):
        all_records = EmailCaptcha.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                user = UserInfo.objects.get(email=email)
                user.is_active = True
                user.save()
        else:
            return render(request, 'send_error.html')


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form': register_form})

    def post(self, requeat):
        register_form = RegisterForm(requeat.POST)
        if register_form.is_valid():
            user_name = requeat.POST.get('email', '')
            if UserInfo.objects.filter(email=user_name):
                return render(requeat, 'register.html', {'msg': '该邮箱已注册！'})
            else:
                pass_word = requeat.POST.get('password', '')
                user = UserInfo()
                user.username = user_name
                user.email = user_name
                user.is_active = False
                user.password = make_password(pass_word)
                user.save()
                send_email(user_name, 'register')
                return render(requeat, 'register.html', {'msg': '激活邮件已发送，请注意查收'})
        else:
            return render(requeat, 'register.html', {'register_form': register_form})


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        login_form = LoginForm(request.POST)
        try:
            if login_form.is_valid():
                user_name = request.POST.get('username', '')
                pass_word = request.POST.get('password', '')
                user = UserInfo.objects.get(email=user_name)
                if user.is_active == 0:
                    return render(request, 'login.html', {'msg': '该用户未激活'})
                else:
                    user = authenticate(username=user_name, password=pass_word)
                    if user is not None:
                        login(request, user)
                        return HttpResponseRedirect(reverse('index'))
                    else:
                        return render(request, 'login.html', {'msg': '用户名或密码错误'})
            else:
                return render(request, 'login.html', {'login_form': login_form})
        except UserInfo.DoesNotExist:
            return render(request, 'login.html', {'msg': '您输入的用户名不规范！'})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('index'))


class ForgetpwdView(View):
    def get(self, request):
        forget_cap = ForgetForm()
        return render(request, 'forgetpwd.html', {'forget_cap': forget_cap})

    def post(self, request):
        forgetpwd_form = ForgetForm(request.POST)
        if forgetpwd_form.is_valid():
            email = request.POST.get('email', '')
            send_email(email, 'forget')
            return render(request, 'forgetpwd.html', {'msg': '发送成功，请注意查收'})
        else:
            return render(request, 'forgetpwd.html', {'forgetpwd_form': forgetpwd_form})


class ResetpwdView(View):
    def get(self, request, active_code):
        all_records = EmailCaptcha.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                return render(request, 'password_reset.html', {'email': email})
        else:
            return render(request, 'send_error.html')
        return render(request, 'login.html')


class ModefyPwdView(View):
    def post(self, request):
        modefy_form = ModefyForm(request.POST)
        if modefy_form.is_valid():
            pw1 = request.POST.get('password1')
            pw2 = request.POST.get('password2')
            email = request.POST.get('email')
            if pw1 != pw2:
                return render(request, 'password_reset.html', {'msg': '两次输入的密码不一致'})
            else:
                user = UserInfo.objects.get(email=email)
                user.password = make_password(pw2)
                user.save()
                return render(request, 'login.html')
        else:
            return render(request, 'password_reset.html', {'modefy_form': modefy_form})


class UserInfoView(LoginRequireMixin, View):
    def get(self, request):
        current_nav = 'info'
        return render(request, 'usercenter-info.html', {'current_nav': current_nav})

    def post(self, request):
        userinfo_form = UserInfoForm(request.POST, instance=request.user)
        if userinfo_form.is_valid():
            userinfo_form.save()
            return HttpResponse('{"status": "success"}', content_type='application/json')
        else:
            return HttpResponse(json.dumps(userinfo_form.errors), content_type='application/json')


class UploadIamgView(LoginRequireMixin, View):
    def post(self, request):
        image_form = UploadIamgForm(request.POST, request.FILES, instance=request.user)
        if image_form.is_valid():
            image_form.save()
            return HttpResponse('{"status": "success"}', content_type='application/json')
        else:
            return HttpResponse('{"status": "fail"}', content_type='application/json')


class MyCourseView(LoginRequireMixin, View):
    def get(self, request):
        current_nav = 'course'
        user_course = UserCourse.objects.filter(user=request.user)
        return render(request, 'usercenter-mycourse.html', {'user_course': user_course, 'current_nav': current_nav})


class IndexView(View):
    def get(self, request):
        banner = Viewpager.objects.all().order_by('index')
        courses = Course.objects.filter(is_banner=False)[:5]
        banner_course = Course.objects.filter(is_banner=True)[:2]
        course_org = Organizations.objects.all()[:15]
        return render(request, 'index.html',
                      {
                          'banner': banner,
                          'courses': courses,
                          'banner_course': banner_course,
                          'course_org': course_org,
                      }
                      )
