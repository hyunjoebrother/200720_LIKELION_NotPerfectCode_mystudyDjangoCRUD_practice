from django.shortcuts import render, redirect, get_object_or_404
#HTML 화면에 data가 나오도록 한다
from .models import Blog #model에 있는 Blog 클래스를 import

# Create your views here.
def blog(req): #app 기능 구현 - > HTML 화면에 띄우기

    blogs=Blog.objects #blogs라는 객체는 저장하고, {}를 html에 넘겨주겠다
    #home.html에 나타날 객체 object blogs 변수를 지정

    return render(req, 'blog.html', {'blogs':blogs}) #키 값을 블로그로 들여옴 
    #'blogs라는 변수 지정': 객체에 사용한다
    #req요청이 들어오면 return반환한다 -> home.html을 render주다


#CRUD 시작! 다른 함수들도 만들자

def new(req):
    return render(req, 'new.html')


def create(req):
    #form을 통해 받은 data를 POST 객체에 넣어준다
    #POST에 저장한 data를 save() method로 DB에 저장
    #다시 'home'으로 redirect -> redirect함수는 위에 import해준다

    if req.method=="POST":
        blog=Blog()
        blog.title=req.POST['title']
        blog.body=req.POST['body']
        blog.save()
    return redirect('/blog/'+str(blog.id))
    #return render(req, 'new.html')

    #새 글쓰기는 완료 ㅇㅇ 근데 바로 home으로 안 돌아가서 일단 UD해봄
    #blog.id는 해당 객체의 번호

def detail(request, blog_id):
    blog=get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html',{'blog':blog})
    #위에 get_어쩌구 import해주기