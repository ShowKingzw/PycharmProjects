from django.shortcuts import render,HttpResponse 
from CampusServices.models import User 
from django.urls import reverse
# 登录函数 
def index(request): 
    if request.method == "POST": 
        username = request.POST.get("username") 
        password = request.POST.get("password") 
        # 查询数据库中是否存在该用户名 
        try: 
            user = User.objects.get(name=username) 
        except User.DoesNotExist: 
            return render(request, 'index.html', {'error': '该用户不存在！'}) 
 
        # 检查密码是否匹配 
        if user.password == password: 
            # 用户信息正确后，返回一个Http响应 
            #return HttpResponse('密码匹配，跳转到KK的网页') 
            return render(request,"maps.html")
        else: 
            return render(request, 'index.html', {'error': '输入密码错误！'}) 
    # 如果不是POST请求，返回登录页面 
    return render(request, 'index.html') 
# 注册函数 
def register(request): 
    if request.method == 'POST': 
        username = request.POST.get('username') 
        password = request.POST.get('password') 
        password2 = request.POST.get('password2') 
        # 检查用户名是否已存在 
        if User.objects.filter(name=username).exists(): 
            return render(request, 'register.html', {'error': "该用户名已注册!"}) 
        # 检查密码和确认密码是否一致 
        if password != password2: 
            return render(request, 'register.html', {'error': "密码不一致,请重新输入！"}) 
        # 这里假设你有一个名为User的模型来存储用户信息 
        user = User(name=username, password=password) 
        # 将用户信息插入app_user表 
        user.save() 
        # 注册成功，返回登录页面并携带注册成功信息 
        return render(request, 'index.html', {'error': '注册成功！'}) 
    # 如果不是POST请求，返回注册页面 
    return render(request, 'register.html') 

def maps(request):
    return render(request,'maps.html')
def lnglat(request):
    return render(request,'lnglat.html')
def route(request):
    return render(request,'route.html')
