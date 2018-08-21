from random import Random
from goodstudy.settings import EMAIL_FROM
from django.core.mail import send_mail

from apps.user.models import EmailCaptcha


def random_num(randomlenth=8):
    my_str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    lenth = len(chars) - 1
    random = Random()
    for i in range(randomlenth):
        my_str += chars[random.randint(0, lenth)]
    return my_str


def send_email(email, send_type='register'):
    email_captcha = EmailCaptcha()
    code = random_num(16)
    email_captcha.code = code
    email_captcha.email = email
    email_captcha.send_type = send_type
    email_captcha.save()

    email_title = ''
    email_body = ''

    if send_type == 'register':
        email_title = '乐之在线网注册激活链接'
        email_body = '请点击一下链接激活您的账户：http://127.0.0.1:8000/active/{0}'.format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass

    else:
        email_title = '乐之在线网找回密码链接'
        email_body = '请点击一下链接进入页面重置您的密码：http://127.0.0.1:8000/resetpwd/{0}'.format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
