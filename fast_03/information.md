# SqlAlchemy 3-dars

SQLAlchemy, Python uchun kuchli bir ORM (Object-Relational Mapping) kitobxonasi va SQL bazalari bilan ishlash uchun
kutilmagan bir foydalanuvchi interfeysi (API) tashkil etadi. SQLAlchemy, turli turdagi SQL bazalari bilan ishlashni
osonlashtirish, so'rovlarni yozishni va boshqa amallarni amalga oshirishni osonlashtiradi.

Quyidagi asosiy vazifalarni bajarish uchun ishlatiladi:

1. Baza bilan bog'lanish va bog'lovni yoqish: SQLAlchemy, turli turdagi SQL bazalariga bog'lanish uchun qo'llaniladi (
   masalan, SQLite, PostgreSQL, MySQL, Oracle va boshqalar).

2. Ma'lumot modellari yaratish: SQLAlchemy, deklarativ yoki klass ma'lumot modellari yaratishda osonlik ta'minlaydi. Bu,
   ma'lumot bazasidagi jadvalidan Python ob'ektlarini yaratishga imkon beradi.

3. Ma'lumotlarni so'ray olish va qaytarish: SQLAlchemy, so'rov yozish uchun SQL-analogiyasini taqdim etadi.
   Ma'lumotlarni
   olish va ma'lumotlar bazasiga yozish uchun bog'lovga mos ravishda so'rovlarni yuboradi.

4. Tranzaksiyalarni boshqarish: SQLAlchemy, tranzaksiyalarni boshqarish va so'rovlar orqali ma'lumotlarni qayta yozishni
   osonlashtiradi.

5. Mijoz so'rovlari bilan ishlash: SQLAlchemy, mijozlar tomonidan berilgan so'rovlarni ko'rib chiqishni, ularni ishga
   tushirishni va natijalarni qaytarishni osonlashtiradi.

SQLAlchemy, Pythonning ko'pgina foydalaniladigan ORM kitobxonasi hisoblanadi va turli korxonalar, loyihalar va ilovalar
uchun keng qo'llaniladi. Bu, SQL bilan ishlashda dastlabki ishlarni bajarishni osonlashtiradi va ma'lumotlar
tuzilmasining ob'ektlari bilan ishlashni yengillashtiradi.


```shell
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = 'sqlite:///books.db'

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

```
1. SQLALCHEMY_DATABASE_URL = 'sqlite:///books.db': Bu qator, SQL bazasining joylashuvi va nomini (books.db) belgilaydi. sqlite:/// protokoli, SQLite bilan ishlash uchun qo'llaniladi. Bu yerda "books.db" nomli SQLite fayli yaratiladi, agar u mavjud bo'lmasa, yangi fayl avtomatik ravishda yaratiladi.

2. engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}): Bu qator, SQLAlchemy engine'ini yaratadi. Engine, SQL bazasiga bog'lanish uchun kerakli bog'lovni ta'minlaydi. connect_args={"check_same_thread": False} to'g'ri solishtirish, SQLite bazasi bilan bog'lanishda "check_same_thread" xatosini bartaraf qiladi.

3. SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine): Bu qator, SQL bazasi bilan bog'lanish uchun Session ob'ektlarini yaratadi. autocommit=False va autoflush=False sozlamalari, avtomatik ravishda o'zgaruvchilarni o'zgartirishni saqlash uchun so'rovlar yuborishni o'z ichiga olmaydi. bind=engine deb belgilangan bog'lov, yaratilgan Session ob'ektlarining foydalanishini belgilaydi.

4. Base = declarative_base(): Bu qator, deklarativ ma'lumot modeli uchun bazaviy klass (Base)ni yaratadi. Base klassi, deklarativ tarzda ma'lumot modellari yaratish uchun asosiy sinovdan o'tkaziladi. Ma'lumot modelini yaratishda Base klassidan meros olish tavsiya etiladi.






