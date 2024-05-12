# FastAPI
FastAPI Tutorial

# FastAPI 1-dars
### FastAPI nima?

FastAPI, sodda va tezkor RESTful API-lar yaratish uchun Python asoslangan kuchli, yagona va samarali bir frameworkdir. FastAPI, modern Python sintaksisini qo'llab-quvvatlash uchun ASGI (Asynchronous Server Gateway Interface) standartiga moslangan va asinxron tushunchali dasturlash uchun oid bir framework hisoblanadi. FastAPI ga quyidagi afzalliklari xos:

Tezkor: FastAPI, Python sinaturlarining ishlatilishi va Pydantic moduli bilan integratsiya qilinishi sababli yuqori darajada tezkor operatsiyalarni taqdim etadi.

Sodda: FastAPI, Swagger UI yordamida avtomatik dokumentatsiyani yaratish va OpenAPI standartlariga moslashtirilgan RESTful API-lar yaratishga imkon beradi. Bu, API-ni o'rganish va foydalanish uchun sodda interfeysni taqdim etadi.

Ajoyib validatsiya: Pydantic moduli ishlatilishi sababli, FastAPI ma'lumotlarni qabul qilish, validatsiya qilish va shakllantirish jarayonlarini avtomatik tarzda boshqaradi. Bu, dasturchilar uchun ma'lumotlarni qo'llab-quvvatlash va sinovdan o'tkazishni osonlashtiradi.

Asinxronlik: FastAPI, asinxron operatsiyalarni qo'llab-quvvatlash uchun Pydantic va Starlette bilan birgalikda ishlatiladi. Bu, kodni tiz va hamda juda tezkor qiladi.

O'zaro integrlash: FastAPI, boshqa Python modullari bilan yaxshi integratsiya ta'minlaydi, shuningdek, dasturchilar uchun SQL alifbo tili bo'yicha populyar modullar (masalan, SQLAlchemy) bilan ham integratsiya qilish imkonini beradi.

Xavfsizlik: FastAPI, ma'lumotlar ulashish bo'yicha xavfsizlikni ta'minlash uchun standart JWT (JSON Web Tokens) autentifikatsiyasini va HTTPS protokolini qo'llab-quvvatlaydi.

Kichik resurslarda ishlaydi: FastAPI, kichik resurslarda ishlaydi va yuqori yukni qabul qiladi. Bu, dasturchilar uchun yuqori darajadagi kodni yozish va ishlab chiqish imkonini beradi.

O'tilganlik: FastAPI, asosan foydalanish uchun Python sintaksisini qo'llab-quvvatlaydi, shuningdek, avtomatik dokumetatsiya va testlar yaratishni osonlashtiradi. Bu, dasturchilar uchun tezlik va yuqori sifatli kod yozishni ta'minlaydi.

FastAPI, Python jamoasi tomonidan keng qo'llaniladi va sodda va kompleks dasturlarni yaratish uchun yaxshi variant hisoblanadi.

## FastAPIni ishga tushirish
1. Virtual muhit yaratish
```shell
virtualenv venv  # linux va macos uchun
source venv/bin/activate

py -m venv venv  # window uchun
venv\Scripts\activate

```
2. Kerakli packagelarni o'rnatish
```shell
pip install fastapi
pip install "uvicorn[standart]"
```
3. main.py nomli fayl yaratib ichida kodlarni yozishimiz mumkin bo'ladi
```shell
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def hello():
return {"message": "Hello Developer", "author": "Alimardon"}
```
4. dasturni ishga tushirish uchun quyidagi komandani terminal yoki shellda yozing
```shell
uvicorn main:app --reload
```
5. 127.0.0.1:800 port ishga tushadi. quyidagi komandani yozib api dokumentatsiyani ko'rish mumkin
```shell
127.0.0.1:8000/docs
127.0.0.1:8000/redoc
```