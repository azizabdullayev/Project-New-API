from aiogram import executor, types
from aiogram.types import Message, CallbackQuery
from config import dp
from buttons import start, courses, course_btn, malumotlar, end


@dp.message_handler(commands=['start'])
async def start1(msg: Message):
    text = f"O'QUV MARKAZIMIZGA XUSH KELIBSIZ!"
    image1 = open('foto/foto logo.jpg', 'rb')
    await msg.answer_photo(image1, caption=text, reply_markup=start)


@dp.message_handler(commands='help')
async def help(msg: Message):
    await msg.answer(f"Barcha muammo va batavsil malumotlarni olish uchun admin bilan bog'lanishingizni so'raymiz!")


@dp.message_handler(text='Biz haqimizda')
async def biz_haqimizda(msg: Message):
    image = open('foto/foto logo.jpg', 'rb')
    image2 = open('foto/video isystem.mp4', 'rb')
    text = f"Location (O'quv markaz joylashuvi): https://www.google.com/maps/place/iSystem+IT+academy/@41.3245749,69.3039896,14z/data=!4m10!1m2!2m1!1sToshkent+shahar,+Mirzo+Ulugbek+tumani,+Mirzo+Ulugbek+kuchasi+54A.!3m6!1s0x38aef572e5842f55:0xa87fc261e04f75ea!8m2!3d41.3245741!4d69.3250272!15sCkFUb3Noa2VudCBzaGFoYXIsIE1pcnpvIFVsdWdiZWsgdHVtYW5pLCBNaXJ6byBVbHVnYmVrIGt1Y2hhc2kgNTRBLpIBCnVuaXZlcnNpdHngAQA!16s%2Fg%2F11q2vn0m7k"
    await msg.answer_photo(image,
                           caption=f"O'quv markazimiz ‐ Toshkentdagi eng yirik IT o'quv markazlaridan biri. O'quv markazda IT va Roboto Texnika kurslari bo'yicha kuchli o'qituvchilar tomonidan ta'lim beriladi. 2021-yilda tadbirkor va Data Science kursi mentori Azamjon Nemadaliyev tomonidan asos solingan bo’lib,2 yil ichida eng oldi o’quv markaziga aylanishga ulgurdi. Bugungi kunda Toshkent shahrida 1 ta filialga ega va shu vaqtgacha o'quv markazda juda ko'p IT bo'yicha proffesional mentorlar tomonidan yuksak o'quvchilar yetishi chiqmoqda.\nOquv markazi missiyasi - Texnologiya va intiluvchan yoshlarni ilm ulashish va toxtovsiz rivojlanish orqali fikrlashini ozgartirib, dunyo miqyosida ornak boladigan darajaga olib chiqish.")
    await msg.answer_video(image2)
    await msg.answer(text)


@dp.message_handler(text='Kurslar')
async def course(msg: Message):
    text = f"Kurs tanlang:"
    await msg.answer(text, reply_markup=courses)


@dp.message_handler(text='Ortga')
async def ortga(msg: Message):
    text = 'Ortga qayttingiz'
    await msg.answer(text, reply_markup=start)


@dp.message_handler(text="Foundation")
async def foundation(msg: Message):
    text = f"Foundation kursimizda siz dasturlashning asoslarini o'rganishingiz mumkin bo'ladi"
    image = open('foto/foundation.jpg', 'rb')
    await msg.answer_photo(image, text, reply_markup=course_btn)


@dp.message_handler(text="BackEnd")
async def backend(msg: Message):
    text = f"Back End dasturchilariga ta’rif bersak, ular saytning bizga ko‘rinmas qismini “parda orti”da turib yaratishadi. Saytga ma’lumot uzatish va qabul qilish, serverlar bilan ishlash, Admin panelini tahrirlash, API lar bilan muomala qilishni aynan shu insonlar amalga oshirishadi."
    image = open('foto/backend.png', 'rb')
    await msg.answer_photo(image, caption=text, reply_markup=course_btn)


@dp.message_handler(text="FrontEnd")
async def frontend(msg: Message):
    text = f"Front-End’chi aslida nima ish bajaradi? Bizga saytning ustki tomoni, ya’ni biz ko‘rib turgan turgan qismi: rasm, matn, animatsiyalarni saytga joylashtirishni, ularning o‘lchamlarini to‘g‘rilab chiqishni aynan Front-End vakillari amalga oshiradi. Ular bir qancha texnologiyalar va freymvorklardan foydalanishadi."
    image = open('foto/frontend.png', 'rb')
    await msg.answer_photo(image, caption=text, reply_markup=course_btn)


@dp.message_handler(text="DataScience")
async def datascience(msg: Message):
    text = f"Data Science o’zi nima? Bu savolga, quyidagicha javob bergan bo’lar edik. Data Science bu — ilmiy usullar, va algoritmlar yordamida malumot manbalaridan datalarni olish va uni qayta ishlash, biznesga tadbiq qilishdir. Har qanday biznes va tashkilotlar o’z qarorlarini aynan mavjud datalarga asoslanib qilishlari hechkimga sir emas, aynan shuni bajaruvchi, va o’rganuvchi soha bu Data Sciencedir."
    image = open('foto/datascience.jpg', 'rb')
    await msg.answer_photo(image, caption=text, reply_markup=course_btn)


@dp.message_handler(text="Android")
async def android(msg: Message):
    text = f"Android (yunoncha andro — „inson, erkak“, oid qoʻshimchasi — „robot“; „odamsimon robot“) — smartfonlar, planshetlar, elektron kitoblar, raqamli pleyerlar, qoʻl soatlari, fitnes bilakuzuklar, oʻyin pristavkalari, noutbuklar, netbuklar, smartbuklar, Google Glass koʻzoynaklari[2], televizorlar[3], proyektorlar hamda boshqa qurilmalar (2015-yilda avtomobil koʻngilochar tizimlari[4] va maishiy robotlarga ham oʻrnatildi) uchun operatsion tizim hisoblanadi."
    image = open('foto/android.png', 'rb')
    await msg.answer_photo(image, caption=text, reply_markup=course_btn)


@dp.message_handler(text="Desing")
async def desing(msg: Message):
    text = f"Dizayn (inglizcha: design — „loyiha“, „chizma“, „rasm“) — narsalar muhitini estetik va funksional sifatlarini shakllantirish maqsadiga qaratilgan loyihalash faoliyati turlarini ifodalovchi termin. Dizayn faoliyati tarkibiga keng isteʼmol buyumlari, mashina, dastgoh, kiyim, reklama va oʻrov materiallari, i. ch., jamoat va turar joy binolarini jihozlash, mebel va b. kiradi. Dizayn 20-asr boshlarida yuzaga kelib, 1930-yillarda maxsus faoliyat turi sifatida Gʻarbiy Yevropa va AQShda shakllandi. 1980-yil 2-yarmidan dizaynning faoliyat doirasi kengaydi. Dizaynerlar rassom sezgisi bilan birga ilmiy fanlar (masalan, materialshunoslik, rangshunoslik va boshqa)ga tayanadi, i. ch. jarayoni va sharoitlari, sotsiologiya va boshqa bilimlarga ega bulishi lozim. Dizayn sohasidagi mutaxassislar maxsus oliy oʻquv yurtlaridatayyorlanadi. Jumladan, Kamoliddin Behzod nomidagi Milliy rassomlik va dizayn institutida ham interyerlar va sanoat grafikasi, libos dizayn boʻyicha mutaxassislar tayyorlanadi."
    image = open('foto/desing.jpg', 'rb')
    await msg.answer_photo(image, caption=text, reply_markup=course_btn)


@dp.callback_query_handler(text='bolish')
async def boldi(call: CallbackQuery):
    text = f"Iltimos malumotlaringizni kiriting:"
    await call.message.answer(text, reply_markup=malumotlar)


@dp.message_handler(text="Kurslar ro'yhatiga qaytish")
async def ort(msg: Message):
    text = f"Kurs tanlang:"
    await msg.answer(text, reply_markup=courses)


@dp.message_handler(content_types=types.ContentType.CONTACT)
async def ttt(msg: Message):
    await msg.answer(f"Malumotlar qabul qilindi\nBiz siz bilan yaqin kunlarda bog'lanamiz! 😊", reply_markup=end)


@dp.message_handler(text="Bosh sahifaga qaytish")
async def end_1(msg: Message):
    await msg.answer(f"Bosh sahifaqa qayttingiz!", reply_markup=start)


if __name__ == '__main__':
    executor.start_polling(dp)
