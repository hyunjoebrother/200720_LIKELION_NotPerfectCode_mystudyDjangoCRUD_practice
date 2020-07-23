from django.db import models

# Create your models here.
class Blog(models.Model): #글쓰기 형태 ㅇㅇ model 다 만들고 -> migrate -> 데이터 전송 요청
    title=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    body=models.TextField()
    
    #migrate까지 하고 /admin 사이트 들어가니까 로그인해야함 -> admin 계정 만들자
    #hyunjoe31/hyunjoe31@gmail.com/cl132435로 만들었음 -> 로그인하면 admin 들어가진다

    #글 썼는데 제목이 object(1)임 ㅇㅇ 내가 입력한 title이 반환되도록 함수를 만들자
    #Blog 클래스 내부에 함수 써야한다

    def __str__(self):
        return self.title
