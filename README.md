## โจ Github Link

- https://github.com/SE-gmentation/yumyumgood_subgroup2

## ๐ข SubGroup 2

- ์ฃผ์  ์๊ฐ 
  - ์ ์ฒด/ํ์๋น ๊ด๋ฆฌ์์ ๋ฉ๋ด ๊ด๋ฆฌ ๋ฐ ํต๊ณ ์๋น์ค๋ฅผ ๋งก์ SUBGROUP2 ๊น์น์/๋ฐฐ์ธ๊ฒฝ ์๋๋ค.
  - ์ด 5๊ฐ์ง์ USE-CASE ์ค ํ์๋น ๋ด๋น ๊ด๋ฆฌ์์ ๊ด๋ จ๋ UC-2, UC-5์ ๊ธฐ๋ฅ์ ๊ตฌํํ์ต๋๋ค.
  - UC2 : ์๋น ๋ด๋น์์ ๋ฉ๋ด ๊ด๋ฆฌ
  - UC5 : Date Picker

- ๊ธฐ๋ฅ ๋ช์ธ
  - ํ์๋น ๋ด๋น ๊ด๋ฆฌ์ ์ธํฐํ์ด์ค ํ์ด์ง ๊ตฌํ
  - ์ ์ํ ํ์๋น ๋ด๋น ๊ด๋ฆฌ์์ ๋ฐ๋ฅธ DB ์กฐํ
  - ๋ ์ง๋ณ ํ์๋น์ ์กฐ/์ค/์์ ๋ฉ๋ด ์กฐํ
  - ์บ๋ฆฐ๋๋ฅผ ํตํ ์กฐํ ๋ ์ง ๋ณ๊ฒฝ๊ณผ DB ์ฐ๊ฒฐ
  - ๋ฉ๋ด ํ๋งค์ํ ๋ฐ ์ฌ๊ณ  ๊ด๋ฆฌ

<br/>

## ๐จ Tech stacks & Language

- Python3
- Django
- sqlite
- HTML
- CSS
- JS
- Bootstrap

<br/>

## ๐ Getting Started
1. Clone this repository

   ```bash
   $ git clone https://github.com/SE-gmentation/yumyumgood_subgroup2.git
   ```

2. ๊ฐ์ํ๊ฒฝ(venv) ์ค์น 

   ```bash
   $ python -m venv venv 
   ```

3. ๊ฐ์ํ๊ฒฝ(venv) ์คํ

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

> DB ๋ด์ฉ(Profile(User), Menu, Cafeteria)์ ์๋ฒ๊ฐ ์คํ ๋ ๋ก์ปฌ์์ http://127.0.0.1:8000/admin/ ์ฌ์ดํธ๋ฅผ ํตํด ์ผ๊ด์ ์ผ๋ก ์์ฑ ๋ฐ ๊ด๋ฆฌํ์ฌ ๋ฐ๋ชจ๋ฅผ ์งํํ์ต๋๋ค. ๊ด๋ จํ์ฌ ๊ถ๊ธํ์  ์ ์ Issues ๋ถํ๋๋ฆฝ๋๋ค.

<br/>

## ๐ธ Features & Demo Screenshot

- **DB๊ตฌ์ถ**
  - UC-2, UC-5 ๊ตฌํ์ ์ํ DB ์ค๊ณ

  - ERD  
  <img src="https://user-images.githubusercontent.com/52988414/119694819-8d46f700-be88-11eb-97ad-f872866d3c4b.png" height=400 />

  - sqlite ์ ์ฉ  
  <img src="https://user-images.githubusercontent.com/52988414/120183484-b67dd380-c24a-11eb-8aaf-caece689e776.png" height=600/>

- **์น์ฑ์ผ๋ก ํ์ด์ง ๊ตฌ์ฑ**
  - ๋ชจ๋ฐ์ผ ํ๋ฉด ํฌ๊ธฐ๋ก ์นํ์ด์ง๋ฅผ ๊ตฌ์ฑ
  
    <img src="https://user-images.githubusercontent.com/52988414/120182754-c34df780-c249-11eb-9d18-8418a8bcbc8f.png" height="300"/>
    <img src="https://user-images.githubusercontent.com/52988414/120183627-e75e0880-c24a-11eb-8df8-c2d50fa1131c.png" height="300"/>

- **( UC-2 )  ๋ด๋น์ ์๋น ๋ณ ์ธํฐํ์ด์ค ํ์ด์ง**
  - ์ ์ํ user์ cafeteria storage๋ฅผ ์กฐํํ์ฌ ์ธํฐํ์ด์ค ํ์ด์ง๋ฅผ ๊ตฌ์ฑํ๋ค.
  <p align="center">
  <img src="https://user-images.githubusercontent.com/52988414/120185111-bf6fa480-c24c-11eb-8b75-0ca1f3f9bdde.png" width=300/>
  </p>
  
- **( UC-2 )  ๋ฉ๋ด ์ํ ๊ด๋ฆฌ**
  - ์๋น ์ ๋ณดํ date storage๋ฅผ ํตํด ์ค๋ ๋ ์ง์ ํด๋นํ๋ ์กฐํ ์ฟผ๋ฆฌ๋ฅผ ๋ณด๋ด Menu๋ฅผ DB์์ ๋ถ๋ฌ์ด.
  - ๋ ์ง ์ ๋ณด๋ url parameter๋ก ์ ์กํจ.  
  <img src="https://user-images.githubusercontent.com/52988414/120187181-71a86b80-c24f-11eb-887c-e052d9885c6a.png" height=25/>

  - Menu ์ ๋ณด๋ก html ํ์ด์ง๋ฅผ ๋ ๋๋งํจ.
  <p align="center">
  <img src="https://user-images.githubusercontent.com/52988414/120186224-2e013200-c24e-11eb-9749-9108c1e1caef.png" width=300/>
  </p>

- **( UC-5 ) ์บ๋ฆฐ๋ ๋ชจ๋ฌ**
  - ์บ๋ฆฐ๋ ๋ฒํผ์ ์ ํํ๋ฉด Modal html์ ๋ ๋๋งํ์ฌ ๋ชจ๋ฌ์ ํ์
  - date storage ๊ธฐ์ค์ผ๋ก ์บ๋ฆฐ๋ ๋ชจ๋ฌ ๊ตฌ์ฑ
  
  <p align="center">
  <img src="https://user-images.githubusercontent.com/52988414/120187405-b3391680-c24f-11eb-9aa4-ef8e16a97c22.png" width=300/>
  </p>

- **( UC-2 ) ๋ฉ๋ด ์ ๋ณด ์์ **

  - ์ ๋ณด ์์  ๋ฒํผ์ ์ ํํ์ฌ ํด๋น ๋ ์ง์ ํ๋งค ๋ฉ๋ด ์ ๋ณด ์์ 
  - ํ๋งค์ํ, ์ฌ๊ณ  ๋ ์ด๋ธ์ ํ์คํธ ๋ฐ์ค๋ก ๋ฐ๊พธ์ด ์์ ํ  ์ ์๋๋ก ํจ
  - ์ ์ฅํ๊ธฐ ๋ฒํผ์ ์ ํํ๋ฉด ๋ณ๊ฒฝ๋ ์ ๋ณด๋ก DB๋ฅผ ์๋ฐ์ดํธํจ.

  <p align="center">
  <img src="https://user-images.githubusercontent.com/52988414/120188028-8e916e80-c250-11eb-8d9b-8e5fee4aa4ed.png" width=300/>
  </p>
  
<br/>

## ๐ SSD(Class Diagram) ๋์กฐํ

>   | SSD ๋ด ์ปจ์(ํด๋์ค)์ด๋ฆ | ํด๋์ค๋ช(ํจ์๋ช) |
>   | --- | ---  |
>   |**class Date Converter** : YYYY-MM-dd ํํ๋ก url์ param์ผ๋ก Date๋ฅผ ๋ฐ์ |Date Accessor(Date Storage ๊ฐ์ฒด)|
>   |**profile = Profile.objects.get(user = request.user)** : sqlite์์ ํ์ฌ ์ ์ํ User์ ๋ํ ์ ๋ณด๋ฅผ ์กฐํ|User DB Accessor|
>   |**menus = Menu.objects.filter(sale_date = date, cafeteria = profile.Cafeteria)** : sqlite์์ ํ์ฌ ์ ์ํ user์ ์๋น์ธ ์ง, ํ๋งค ๋ ์ง๊ฐ ์ผ์นํ๋ ์ง ํ์ธํ ๋ฉ๋ด ๋ฐ์ดํฐ๋ฅผ ์กฐํ |Menu DB Accessor|
>   |**return render(request,'manager/initialpage.html', data)** |interfacePage := render(menuList)|
>   |**return render(request,'manager/manage_read.html', data)** |savePage := saveRender()|
>   |**return render(request,'manager/manage_update.html', data)** |editPage := renderEdit()|
>   |**def menu_edit(request, date)** |updateStatus(status)|
>   |**status=request.POST.get('status['+str(i)+']')**<br>**quantity=request.POST.get('quantity['+str(i)+']')**<br>#DB์ ๋ฐ๊ฟ ๋ด์ฉ๋ค<br>**changeMenu.status=status**<br>**changeMenu.quantity=quantity**|setStatus, setAmount|
>   |**def menu_update(request, date)**|edit(), save()|
>   |views.py|Controller|
>   |**date**|today|
>   |**target**|target|
>   |**changeDate, changeMonth, changeYear**|Date calculator์ ํจ์|
>   |**place()**|makeCalendar|
>   |**getDate()**|getDay|
>   |**DatePicker**|Interface Button|
>   |**moveDay, moveMonth, moveYear**|checkButton|

<br/>

## ๐ป ์ฐธ๊ณ ์ฌํญ
- ์ฝ๋์์์ organization ๋ด yumyumgood_subgroup2์์ ์งํ ํ์ต๋๋ค.
- DB ๋ด์ฉ(Profile(User), Menu, Cafeteria)์ ์๋ฒ๊ฐ ์คํ ๋ ๋ก์ปฌ์์ http://127.0.0.1:8000/admin/ ์ฌ์ดํธ๋ฅผ ํตํด ์ผ๊ด์ ์ผ๋ก ์์ฑ ๋ฐ ๊ด๋ฆฌํ์ฌ ๋ฐ๋ชจ๋ฅผ ์งํํ์ต๋๋ค. ๊ด๋ จํ์ฌ ๊ถ๊ธํ์  ์ ์ Issues ๋ถํ๋๋ฆฝ๋๋ค.
- Subgroup2๋ Github์ Issues๋ฅผ ์ ๊ทน ํ์ฉํ์ฌ ๊ตฌํ(๊ฐ๋ฐ)์ ์งํํ์ต๋๋ค.
<p align="center">
<img src="https://user-images.githubusercontent.com/52988414/120179634-cf37ba80-c245-11eb-9ed9-c7c713337a43.png" width=600/>
</p>



