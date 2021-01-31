# MyInTime
간단한 Django blog 프로젝트 입니다.

블로그를 개발하고 AWS와 도커로 배포합니다.



자세히 알아보기 :

https://www.notion.so/AWS-Docker-348bcf9982df4b02b5fe937293ef3dd6



## Features
- 블로그 메인 화면 : 부트스트랩 사용
- 사용자 블로그 글 쓰기
- CKEditor : 글쓰기 페이지 꾸미기
- 블로그 세부 화면 구성
- 댓글 추가
- MyInTime 카운트
- AWS Lightsail



## Installation
```
pip install -r requirements.txt
cd pjt_MyInTime
python manage.py runserver
```

**requirements.txt** \
asgiref==3.3.1  
Django==3.1.5 \
django-ckeditor==6.0.0  \
django-js-asset==1.2.2  \
pytz==2020.5 \
sqlparse==0.4.1  

 

---



https://hub.docker.com/r/hjc960/django-test

```
docker pull hjc960/django-test:blog2
docker run -it -d -p 8000:8000 hjc960/django-test:blog2
```

