## ✨ Github Link

- https://github.com/SE-gmentation/yumyumgood_subgroup2

## 📢 SubGroup N

- 간단히 서브그룹 주제 소개 
  - 예)왕왕왕 저는 은서예원이구요 서브그룹1 주제는 ~~
  - 예)SSD에서 2(개수조절),3(메뉴선택),5(결제)를 선택해서 ~~
- 개발한 기능 ( 간단히 소제목 형식으로 )
  - 예) 접속 시간에 구매가능한 학식당 별 메뉴 조회 및 선택
  - 예) 선택한 메뉴 개수조절 및 결제를 통한 QR생성 및 DB 재고 업데이트

<br/>

## 🔨 Tech stacks & Language


- 예) Python3
- 예) Mongo DB
- 예) 흠냐
- 예) 뭐쓰지 ^^..

<br/>

## 🔎 Getting Started
1. Clone this repository

   ```bash
   $ git clone https://github.com/SE-gmentation/yumyumgood_subgroup2.git
   ```

2. 가상환경(venv) 설치 

   ```bash
   $ python -m venv venv 
   ```

3. 가상환경(venv) 실행

   ```bash
   $ source venv\Scripts\activate
   ```
   
4. Install Requirements for project

   ```bash
   $ pip install -r requirements.txt 
   ```
   
5. Migration for DB (Command execution location must be where manage.py is located.) 

   ```bash
   $ python manage.py makemigrations
   $ python manage.py migrate
   ```
   
6. Create Superuser for Admin -> Set Username & Password (Command execution location must be where manage.py is located.) 

   ```bash
   $ python manage.py createsuperuser
   ```
   
7. Run (Command execution location must be where manage.py is located.) 

   ```bash
   $ python manage.py runserver
   ```

> DB 내용(Profile(User), Menu, Cafeteria)은 서버가 실행 된 로컬에서 http://127.0.0.1:8000/admin/ 사이트를 통해 일괄적으로 작성 및 관리하여 데모를 진행했습니다. 관련하여 궁금하신 점은 Issues 부탁드립니다.

<br/>

## 📸 Features & Demo Screenshot

- **데이터 불러오기 및 데이터 파싱 후 DB구축**
  - 이 부분에 기능 설명
  - 해당 기능 관련 사진을 기능 설명과 동시에 첨부하는거 어떨까요? 아래처럼(^^사심듬뿍)
  ![image](https://user-images.githubusercontent.com/65647080/120084870-afea4180-c10e-11eb-81e7-12899a6c0253.png)

- **( UC-4 )  DB구축 및 현재 접속한 시간대에 구매 가능한 학식당 별 메뉴 조회**
  - 먼저, 포탈 내 학식당 페이지에 접속하여 dummy data로 이용할 식단 데이터를 csv형태로 불러와 nosql인 몽고 db에 어쩌궁
  - 그래서 뫄뫄모마뫄 어쩌구 저쩌구 예외처리는 어쩌구 저쩌구
- **( UC-4 )  메뉴 선택**
  - 던던댄스
  - 아 던던댄스 던던댄스 저스트 댄스,, 
- **( UC-2 ) 장바구니에서 담은 메뉴 개수 조절**
  - 개수 조절의 범위는 ~~
  - DB 재고 수량을 파악하여 최대수량을 넘지 않는 선에서 ~~
- **( UC-5 ) 결제 금액 계산 및 QR코드 생성 및 유효시간 핸들링**
  - 에이쎄엡 내 반쪽 아니?
  - 완 전 카피~

<br/>

## 📍 SSD(Class Diagram) 대조표

>   | 클래스명(함수명) |  SSD 내 컨셉(클래스)이름  |
>   | --- | ---  |
>   |**class Date Converter** : YYYY-MM-dd 형태로 url의 param으로 Date를 받음 |Date Accessor(Date Storage 객체)|
>   |**profile = Profile.objects.get(user = request.user)** : sqlite에서 현재 접속한 User에 대한 정보를 조회|User DB Accessor|
>   |**menus = Menu.objects.filter(sale_date = date, cafeteria = profile.Cafeteria)** : sqlite에서 현재 접속한 user의 식당인 지, 판매 날짜가 일치하는 지 확인한 메뉴 데이터를 조회 |Menu DB Accessor|
>   |**return render(request,'manager/initialpage.html', data)** |interfacePage := render(menuList)|
>   |**return render(request,'manager/manage_read.html', data)** |savePage := saveRender()|
>   |**return render(request,'manager/manage_update.html', data)** |editPage := renderEdit()|
>   |**def menu_edit(request, date)** |updateStatus(status)|
>   |**status=request.POST.get('status['+str(i)+']')**<br>**quantity=request.POST.get('quantity['+str(i)+']')**<br>#DB에 바꿀 내용들<br>**changeMenu.status=status**<br>**changeMenu.quantity=quantity**|setStatus, setAmount|
>   |**def menu_update(request, date)**|edit(), save()|
>   |views.py|Controller|

<br/>

## 💻 참고사항
- 코드작업은 organization 내 yumyumgood_subgroup2에서 진행 했습니다.
- DB 내용(Profile(User), Menu, Cafeteria)은 서버가 실행 된 로컬에서 http://127.0.0.1:8000/admin/ 사이트를 통해 일괄적으로 작성 및 관리하여 데모를 진행했습니다. 관련하여 궁금하신 점은 Issues 부탁드립니다.
- Subgroup2는 Github의 Issues를 적극 활용하여 구현(개발)을 진행했습니다.



