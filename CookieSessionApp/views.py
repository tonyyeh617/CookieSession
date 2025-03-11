from urllib import response
from django.shortcuts import render
from django.http import HttpResponse


def set_cookie(request,key=None,value=None):
    # print(key)
    # print(value)
    # return HttpResponse("ok")
    response = HttpResponse('Cookie 儲存完畢!')
    response.set_cookie(key,value)
    return response

def get_cookie(request,key=None):
    if key in request.COOKIES:
        return HttpResponse(f"{key}:{request.COOKIES[key]}")
    else:
        return HttpResponse('Cookie 不存在!')	

def get_allcookies(request):
    if request.COOKIES!=None:
        strcookies=""
        for key1,value1 in request.COOKIES.items():
            strcookies= strcookies + key1 + ":" + value1 + "<br>"
        return HttpResponse('%s' %(strcookies))
    else:
        return HttpResponse('Cookie 不存在!')	

def set_cookie2(request,key=None,value=None):
    response = HttpResponse('Cookie 有效時間1小時!')
    response.set_cookie(key,value,max_age=3600)
    return response		

def delete_cookie(request,key=None):

    if key in request.COOKIES:
        response = HttpResponse('Delete Cookie: '+key)	
        response.delete_cookie(key)
        return response
    else:
        return HttpResponse('No cookies:' + key)	

import datetime
def index(request):
    #列出dict的key
    # for value in request.COOKIES.keys():
    #     print(value)

    if "counter" in request.COOKIES: #若counter變數存在，即加1
        counter=int(request.COOKIES["counter"])
        counter+=1
    else:#若counter變數不存在，即初始化		
        counter=1
    # response = HttpResponse('今日瀏覽次數：' + str(counter)) #建立物件
    response = render(request,"index.html",locals()) #將cookie傳到templates
    #https://www.codenong.com/17057536/


    #設定counter變數到期時間，
    tomorrow = datetime.datetime.now() + datetime.timedelta(days = 1) #取得現在日期時間再將日期加1日
    #print(tomorrow) #2021-06-12 11:06:01.667359
    tomorrow = datetime.datetime.replace(tomorrow, hour=0, minute=0, second=0) #設定時分秒為0:0:0
    #print(tomorrow) #2021-06-12 00:00:00.087386
    expires = datetime.datetime.strftime(tomorrow, "%a, %d-%b-%Y %H:%M:%S GMT")#利用strftime函式將日期換成指定的格式
    response.set_cookie("counter",counter,expires=expires)#以expires參數設定到期時間
    return response	

def set_session(request,key=None,value=None):
    request.session[key]=value
    return HttpResponse('Session 儲存完畢!')
    
def get_session(request,key=None):
    if key in request.session:
        return HttpResponse(f"{key}:{request.session[key]}")
    else:
        return HttpResponse('Session 不存在!')

def get_allsessions(request):
    print(request.session.items()) #check
    if len(request.session.items()):
        strsessions=""
        for key1,value1 in request.session.items():
            strsessions= strsessions + key1 + ":" + str(value1) + "<br>"
        return HttpResponse(strsessions)
    else:
        return HttpResponse('Session 不存在!')	

def vote(request):
    #print(request.session.items()) #check
    if not "vote" in request.session:
        request.session["vote"]=True
        msg="您第一次投票!"		
    else:		
        msg="您已投過票!"	

    return HttpResponse(msg)	
		
def set_session2(request, key=None, value=None):
    response = HttpResponse("session儲存完畢")
    request.session[key]=value
    request.session.set_expiry(10)# 30秒 表示會話在瀏覽器關閉時過期
    #request.session.set_expiry(0)# 0 表示會話在瀏覽器關閉時過期
    
    return response
    # return HttpResponse("ok")

def delete_session(request,key=None):
    if key in request.session:
        response = HttpResponse('Delete Session: '+key)	
        del request.session[key]
        return response
    else:
        return HttpResponse('No Session:' + key)

def login(request):
    #預設帳號密碼
    username = "tony"
    password = "1234"
    if request.method == 'POST':
        if not 'username' in request.session:
            if request.POST['username']==username and request.POST['password']==password:
                request.session['username']=username #儲存Session
                message=username + " 您好，登入成功！"
                status="login"
            else:
                status=""
                message="密碼或帳號錯誤"

    else:
        if 'username' in request.session:
            if request.session['username']==username:
                message=request.session['username'] + " 您已登入過了！"
                status="login"				
    return render(request, 'login.html',locals())
    
def logout(request):
    if 'username' in request.session:
        message=request.session['username'] + ' 您已登出!'
        status=""
        del request.session['username']	#刪除Session	
    return render(request, 'login.html',locals())        

