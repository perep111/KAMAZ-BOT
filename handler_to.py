from config import dp, bot
from aiogram import types
from func import kb_to, kb_main, kb_hubs, write_to_db_user, kb_china, kb_kamaz


@dp.message_handler(text="Просмотр ТО")
async def read_to(message: types.Message):
    await write_to_db_user(message.from_user.id, message.from_user.username)
    await message.answer('На какие тачки смотрим ТО?',reply_markup=kb_to)


@dp.message_handler(text="KAMAZ")
async def read_to(message: types.Message):
    await write_to_db_user(message.from_user.id, message.from_user.username)
    await message.answer('На какой KAMAZ?',reply_markup=kb_kamaz)


@dp.message_handler(text="китайцы")
async def read_to(message: types.Message):
    await write_to_db_user(message.from_user.id, message.from_user.username)
    await message.answer('На какого китайца?',reply_markup=kb_china)


@dp.message_handler(text="Ступицы")
async def read_to(message: types.Message):
    await message.answer('Ступицы бывают разные',reply_markup=kb_hubs)


@dp.message_handler(text="КОМПАС")
async def read_to(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo="https://img-reis.zr.ru/storage/2022/02/1645365485-zast-2-1024x659.jpg")
    await message.answer('1) Фильтр масляный\n'
                         '<a href="https://d7g69anyp3s9e.cloudfront.net/highlight/LF17535.jpg">'
                         'LF17535</a>  1шт\n'
                         '--------------------------------\n'
                         '2) Фильтр топливный грубый\n'
                         '<a href="https://www.ttm-part.ru/cgi-bin/main.cgi?what=pic&id=937bb267-a8eb-11eb-86c3-382c4ac531f5">'
                         'FS20217</a>  1шт\n'
                         '--------------------------------\n'
                         '3) Фильтр топливный тонкой очистки\n'
                         '<a href="https://www.filter64.ru/images/stories/virtuemart/product/00-00000230_0.jpg">'
                         'FF5706</a>  1шт\n'
                         '--------------------------------\n'
                         '4) Фильтр мочевины\n'
                         '<a href="https://www.maxiparts.com.au/Images/ProductImages/FAS2474.jpg">'
                         'AS2474</a>  1шт\n'
                         '--------------------------------\n'
                         '5) Фильтр салона\n'
                         '<a href="https://agsolco.com/content/images/11/1346x1800l80br70/filtr_konditsionera_n-56-61528891738918.jpg">'
                         '8104116LE010</a>  1шт\n'
                         '--------------------------------\n'
                         '6) Фильтр воздушный со вставкой\n'
                         '<a href="https://www.avtoall.ru/product_pictures/big/481/553753.jpg">'
                         '1109100E898-2</a>  1шт\n'
                         '--------------------------------\n'
                         '7) Фильтр патрон осушителя\n'
                         ' <a href="https://disk.yandex.ru/i/Kix4QJexAUg-Vw">'
                         '204205</a> 1шт\n'
                         ' <u>аналоги: 227-3511010, ii40100F</u>',
                         reply_markup=kb_main, disable_web_page_preview=True)


@dp.message_handler(text="ГБЦ")
async def read_to(message: types.Message):
    await message.answer('1) Головка цилиндра с клапанами 90\n'
                         '<a href="https://zapkamautocentr.ru/a/kamavto/files/multifile/2353/740.90_1003010.JPG">'
                         '740.90-1003010</a>  8шт\n'
                         '1.1) либо головка 30\n'
                         '<a href="https://zapkamautocentr.ru/a/kamavto/files/multifile/2353/740.90_1003010.JPG">'
                         '740.30-1003010</a>  8шт\n'
                         '---------------------------------\n'
                         '2) Прокладка головки блока\n'
                         ' <a href="https://www.avtoall.ru/product_pictures/big/6f1/994620.jpg">'
                         '740.30-1003213-01СБ</a>  8шт\n'
                         '---------------------------------\n'
                         '3) Прокладка выпускного коллектора\n'
                         '<a href="https://www.avtoall.ru/product_pictures/big/a0c/840072.jpg">'
                         '7403.1008050</a>  8шт\n'
                         '----------------------------------\n'
                         '4)Прокладка впускного коллектора\n'
                         ' <a href="https://st24.stpulscen.ru/images/product/219/288/083_original.jpg">'
                         '740.1115026-01 (домик)</a>  8шт\n'
                         '----------------------------------\n'
                         '5) Кольцо уплотнительное ГБЦ\n'
                         ' <a href="https://www.avtoall.ru/product_pictures/big/bb3/616806.jpg">'
                         '740.1003040</a>  8шт\n'
                         '----------------------------------\n'
                         '6) Кольцо водяных труб\n'
                         '<a href="https://www.avtoall.ru/product_pictures/medium/822/616819.jpg">'
                         '740.30-1303118</a>  2шт\n'
                         '----------------------------------\n'
                         '7) Пластина коллектора выпускного\n'
                         ' <a href="https://www.avtoall.ru/product_pictures/big/8dc/947548.jpg">'
                         '7403.1008078</a>  8шт\n'
                         'опционально) не всегда выдается',reply_markup=kb_main, disable_web_page_preview=True)


@dp.message_handler(text="6520")
async def read_z_n(message: types.Message):
    await message.answer('1) Ступица перед 6520\n'
                         ' <a href="https://www.avtoall.ru/product_pictures/big/b75/096365.jpg">'
                         '6520-3103015</a> ------------1шт\n\n'
                         '1) Ступица зад 6520\n'
                         ' <a href="https://kamacenter.ru/netcat_files/multifile/121/76971/100'
                         '-59d103cb8a0e11ed81da0025905eba8c_0a57f5da8b3111ed81da0025905eba8c.jpg">'
                         '6520-3104015</a> ------------1шт\n\n'
                         '2) Кольцо уплотнительное\n'
                         ' <a href="https://disk.yandex.ru/i/lmEeBHUijd8JqQ">'
                         'А1-1788Б</a> --------------1шт\n\n'
                         '3) Прокладка крышки водила\n'
                         ' <a href="https://disk.yandex.ru/i/NEGrhSWHnRYRAw">'
                         '6520-2405081</a> --------------1шт\n\n'
                         '4) Сальник ступичный\n'
                         ' <a href="https://disk.yandex.ru/i/4qOWLRzRssa6Zw">'
                         '415219</a> ------------1шт\n\n'
                         '5) Подшипник внешний\n'
                         ' <a href="https://disk.yandex.ru/i/-xZMd6we700mCg">'
                         '2007121 A (32021Х)</a> ---------1шт\n\n'
                         '6) Подшипник внутренний\n'
                         ' <a href="https://disk.yandex.ru/i/5CehrMFf5UJcDA">'
                         '2007124 А (32024)</a> -----------1шт\n\n',
                         reply_markup=kb_main, disable_web_page_preview=True)


@dp.message_handler(text="43118")
async def read_z_n(message: types.Message):
    await message.answer('1) Подшипник внешний\n'
                         ' <a href="https://disk.yandex.ru/i/XYIvCJe8sRXSxw">'
                         '6-2007118 А (32018)</a>-------------1шт\n\n'
                         '2) Подшипник внутренний\n'
                         ' <a href="https://disk.yandex.ru/i/iN8AcWnt327jXw">'
                         '6-7518А (32218)</a> -------------1шт\n\n'
                         '3) Ступица колеса\n'
                         ' <a href="https://disk.yandex.ru/i/NsPsDmvLIGxF1w">'
                         '43114-3103015-20</a> -----------1шт\n\n'
                         '4) Шпилька полуоси М12х1,25х35\n'
                         ' <a href="https://disk.yandex.ru/i/LZ9gBqJnI1dMqA">'
                         '1/35302/31</a> -------------10шт\n\n'
                         '5) Прокладка полуоси\n'
                         ' <a href="https://disk.yandex.ru/i/TGUfjfNjWQAJ7Q">'
                         '4310-2304091</a> --------1шт\n\n'
                         '6) Сальник ступицы\n'
                         ' <a href="https://disk.yandex.ru/i/b4823Ccc9U8bLw">'
                         '415220</a> -----------1шт\n\n'
                         '7) Сальник полуоси\n'
                         ' <a href="https://disk.yandex.ru/i/8uhoKaFyAdetrg">'
                         '864185-10</a> ------------1шт',
                         reply_markup=kb_main, disable_web_page_preview=True)


@dp.message_handler(text="740 ДВС")
async def read_z_n(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo='https://kamaz-chel.ru/upload/resize_cache/iblock/'
                               '9f7/600_600_1/6rn6auadeh8237k0vk777j9gtmwy3gls.png')
    await message.answer('1) Фильтр масляный\n'
                         ' <a href="https://disk.yandex.ru/i/SzBK9eoLaJyjnQ">'
                         '6W.23.288.01</a> -------------------1шт\n\n'
                         '2) Фильтр масляный\n'
                         ' <a href="https://disk.yandex.ru/i/OLAh8GfZK8W7Xw">'
                         '6W.23.614.00</a> -------------------1шт\n\n'
                         '3) Фильтр топливный\n'
                         ' <a href="https://disk.yandex.ru/i/fn8kQgU2zj5CxQ">'
                         '6W.24.059.00</a> -------------------2шт\n'
                         ' <u>аналоги: WDK962/12</u>\n\n'
                         '4) Фильтр грубой очистки топлива\n'
                         ' <a href="https://disk.yandex.ru/i/Mtpysu92oF_qFw">'
                         'PL420</a> ---------------------------1шт\n'
                         '<u>аналоги: 65920-1105010-10, </u>\n\n'
                         '5) Фильтр патрон осушителя\n'
                         ' <a href="https://disk.yandex.ru/i/Kix4QJexAUg-Vw">'
                         '204205</a> --------------------------1шт\n'
                         ' <u>аналоги: 227-3511010, ii40100F</u>\n\n'
                         '6) Фильтр гур\n'
                         ' <a href="https://disk.yandex.ru/i/BFNyB2Hhb6nRuw">'
                         '4310-3407359-10</a> ----------------1шт\n\n'
                         '7) Фильтр воздушный внешний\n'
                         ' <a href="https://disk.yandex.ru/i/2OoJmuGCCPw56A">'
                         'ЭФВ725.1109560</a> -----------------1шт\n'
                         ' <u>аналоги: ЛНАЕ 1109660</u>\n\n'
                         '8) Фильтр воздушный внутренний\n'
                         ' <a href="https://disk.yandex.ru/i/nZ7J6mbhwLGlig">'
                         'ЭФВ725.1109560-10-01</a> -----------1шт\n'
                         ' <u>аналоги: ЛНАЕ 1109660-10</u>',
                         reply_markup=kb_main, disable_web_page_preview=True)


@dp.message_handler(text="740 старые")
async def read_z_n(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo='https://mail.nuravto.uz/uploads/ZDCICzPEYf.png')
    await message.answer('1) Фильтр масляный\n'
                         ' <a href="https://shop.kamaz.ru/upload/iblock/471/4713ca4a690e804a1deb0808182bb2da.jpeg">'
                         'МЭФ19.1022040</a> -------------------1шт\n'
                         ' <u>аналоги: 7405.1012040</u>\n\n'
                         '2) Фильтр масляный\n'
                         ' <a href="https://shop.kamaz.ru/upload/iblock/74a/74a3fe355f52fa7274fbae83f439f743.jpeg">'
                         '7405.1017040-02</a> -----------------1шт\n\n'
                         '3) Фильтр топливный\n'
                         ' <a href="https://avtokama.ru/img/prods/199/hhd/199.jpg?v1">'
                         '6W.24.064.00</a> ---------------------2шт\n'
                         ' <u>аналоги: ФТ060.1117040</u>\n\n'
                         '4) Фильтр патрон осушителя\n'
                         ' <a href="https://b2b.rumotors.com/imager/is/1/63A6DBA84756EDF9EDE1B761428005EF/'
                         'B8272619D40C963B0431FE72DF7DFF20.png">'
                         '204205</a> ----------------------------1шт\n'
                         ' <u>аналоги: 227-3511010, ii40100F</u>\n\n'
                         '5) Фильтр гур\n'
                         ' <a href="https://avtocomplekt.ru/a/avtocomplekt/files/userfiles/images/catalog/'
                         'f9fad2f54f9411ed8df5a8a159946dd7_291dfb38883711ed8df5a8a159946dd7.jpg">'
                         '4310-3407359-10</a> -----------------1шт\n\n'
                         '6) Фильтр воздушный внешний\n'
                         ' <a href="https://sxstatic.ru/images/b/000050485/000050485_2-900.jpg">'
                         'ЭФВ721.1109560-10</a> ---------------1шт\n'
                         ' <u>аналоги: ЛНАЕ 721-1109560</u>\n\n'
                         '7) Фильтр воздушный внутренний\n'
                         ' <a href="https://sxstatic.ru/images/b/V00008471/V00008471_2-900.jpg">'
                         'ЭФВ721.1109560-30</a> ---------------1шт\n'
                         ' <u>аналоги ЛНАЕ 1109660-10</u>\n\n'
                         '8) Ремкомплект масляного фильтра\n'
                         ' <a href="https://www.mi-parts.ru/file/catalog/pic/thumb1/'
                         'fb61425aec11b5ab36ec5ab49d13ae37.jpg">'
                         'СТР-7406-1012000РК</a> --------------1шт',
                         reply_markup=kb_main, disable_web_page_preview=True)


@dp.message_handler(text='cummins')
async def read_z_n(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo='https://yourmotor.ru/wp-content/uploads/2021/11/6isbe.jpg')
    await message.answer('1) Фильтр топливный сепаратор Cummins\n'
                         ' <a href="https://inter-diesel.ru/components/com_jshopping/files/'
                         'img_products/full_img-toplivnye-filtry-filtry-fleetguard-filtr-toplivnyj-'
                         'fs1067-fleetguard-00-000009061641.jpeg">'
                         'FS1067</a>---------------------------1шт\n\n'
                         '2) Фильтр масляный дв. CUMMINS\n'
                         ' <a href="https://cdn1.ozone.ru/s3/multimedia-u/6700460034.jpg">'
                         'LF16015</a>--------------------------1шт\n'
                         ' <u>аналоги: WK 950/26</u>\n\n'
                         '3) Фильтр топливный Cummins\n'
                         ' <a href="https://hm.avtotex.ru/images/2/17866.jpg">'
                         'FF185</a>-----------------------------1шт\n'
                         ' <u>аналоги: FS36253 C5310808</u>\n\n'
                         '4) Фильтр топливный Cummins\n'
                         ' <a href="https://inter-diesel.ru/components/com_jshopping/files/img_products/'
                         'full_img-toplivnye-filtry-filtry-fleetguard-filtr-toplivnyj-ff5421-fleetguard-00-'
                         '000000971603.jpeg">'
                         'FF5421</a> ---------------------------1шт\n'
                         ' <u>аналоги: 5421-1117010</u>\n\n'
                         '5) Фильтр гур\n'
                         ' <a href="https://disk.yandex.ru/i/d2p53VWmWdu39Q">'
                         'Н601/4</a> ---------------------------1шт\n'
                         ' <u>аналоги: 6014-3400075</u>\n\n'
                         '6) Фильтр воздушный внешний\n'
                         ' <a href="https://avtoalfa.com/netcat_files/multifile/2288/'
                         'original_1663031114_1_ae591499-d1a0-11ea-8937-a4bf01020853.jpg">'
                         'С25710/3</a> -------------------------1шт\n'
                         ' <u>аналоги: ЛНАЕ 1109560</u>\n\n'
                         '7) Фильтр воздушный внутренний\n'
                         ' <a href="https://www.kamazik.ru/upload/iblock/cde/ro3qyo4apyctkhkbu9x31ca8qgpx35x6.jpeg">'
                         'CF710 MHRU</a> -----------------------1шт\n'
                         ' <u>аналоги: ЛНАЕ 1109560-10</u>\n\n'
                         '8) Фильтр патрон осушителя\n'
                         ' <a href="https://disk.yandex.ru/i/Kix4QJexAUg-Vw">'
                         '204205</a> ----------------------------1шт\n'
                         ' <u>аналоги: 227-3511010, ii40100F</u>', reply_markup=kb_main, disable_web_page_preview=True)


@dp.message_handler(text="5490")
async def read_z_n(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo='https://kamaz-chel.ru/upload/iblock/0b4/0b48331fbdf08d5651d015fda5ed670e.png')
    await message.answer('1) Фильтр масляный\n'
                         ' <a href="https://m.avtoall.ru/product_pictures/big/394/909812.jpg">'
                         'A0001802909</a> --------------------1шт\n'
                         ' <u>аналоги: 1802909-1012010</u>\n\n'
                         '2) Фильтр топливный грубый\n'
                         ' <a href="https://disk.yandex.ru/i/7MajqcDMWcmCFg">'
                         '6W.26.068.00</a> --------------------1шт\n\n'
                         '3) Фильтр топливный тонкой очистки\n'
                         ' <a href="https://disk.yandex.ru/i/W5kW8F-qvt0c-A">'
                         'A5410900151</a> ---------------------1шт\n'
                         ' <u>аналоги: 151-1117010 PU999/1</u>\n\n'
                         '4) Фильтр патрон осушителя\n'
                         ' <a href="https://disk.yandex.ru/i/Kix4QJexAUg-Vw">'
                         '204205</a> ----------------------------1шт\n'
                         ' <u>аналоги: 227-3511010, ii40100F</u>\n\n'
                         '5) Фильтр гур\n'
                         ' <a href="https://disk.yandex.ru/i/d2p53VWmWdu39Q">'
                         'H601/4</a> -----------------------------1шт\n'
                         ' <u>аналоги: 6014-3400075</u>\n\n'
                         '6) Фильтр воздушный внешний\n'
                         ' <a href="https://disk.yandex.ru/i/h6T_8EFgZ4kWKA">'
                         'C30 1330</a> -------------------------1шт\n'
                         ' <s>аналоги: ЛНАЕ 1109760</s>\n\n'
                         '7) Фильтр воздушный внутренний\n'
                         ' <a href="https://disk.yandex.ru/i/l8SYQvNFsnNdog">'
                         'CF 1820</a> ---------------------------1шт\n'
                         ' <s>аналоги: ЛНАЕ 1109760-10</s>\n\n'
                         '8) Фильтр салона\n'
                         ' <a href="https://disk.yandex.ru/i/PNxF-Nk9A6XZFw">'
                         'A9408350047</a> ----------------------1шт\n'
                         ' <u>аналоги: MAHLE LA358, AF26174</u>',
                         reply_markup=kb_main, disable_web_page_preview=True)


@dp.message_handler(text="54901")
async def read_z_n(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo='https://kamaz-chel.ru/upload/iblock/b91/b91834d441f8c24a9911d5cf7a61233a.png')
    await message.answer('1) Фильтр масляный\n'
                         ' <a href="https://disk.yandex.ru/i/Cj80WB1AYndZaA">'
                         '6W.25.169.00</a> ----------------------1шт\n\n'
                         '2) Фильтр топливный грубый\n'
                         ' <a href="https://disk.yandex.ru/i/7MajqcDMWcmCFg">'
                         '6W.26.068.00</a> ----------------------1шт\n\n'
                         '3) Фильтр топливный тонкой очистки\n'
                         ' <a href="https://disk.yandex.ru/i/j_gj43XKaVGsSA">'
                         '6W.26.084.00</a> ----------------------1шт\n\n'
                         '4) Фильтр патрон осушителя\n'
                         ' <a href="https://disk.yandex.ru/i/Kix4QJexAUg-Vw">'
                         '204205</a> -----------------------------1шт\n'
                         ' <u>аналоги: 227-3511010, ii40100F</u>\n\n'
                         '5) Фильтр гур\n'
                         ' <a href="https://disk.yandex.ru/i/d2p53VWmWdu39Q">'
                         'H601/4</a> ------------------------------1шт\n'
                         ' <u>аналоги: 6014-3400075</u>\n\n'
                         '6) Фильтр воздушный внешний\n'
                         ' <a href="https://disk.yandex.ru/i/lrD1mwjiNzJ0ZQ">'
                         '54901-1109560</a> --------------------1ком\n'
                         ' <s>аналоги: </s>\n\n'
                         '7) Фильтр воздушный внутренний\n'
                         ' <a href="https://disk.yandex.ru/i/mZfSoNoItznTug">'
                         '54901-1109560-10</a> ----------------1ком\n'
                         ' <s>аналоги: </s>\n\n'
                         '8) Фильтр салона\n'
                         ' <a href="https://disk.yandex.ru/i/UspQaizPT7lgLw">'
                         'A9608300618</a> ----------------------1шт\n'
                         ' <s>аналоги: </s>',
                         reply_markup=kb_main, disable_web_page_preview=True)


@dp.message_handler(text="SITRAK")
async def read_z_n(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo='https://sinotruk74.ru/upload/iblock/83f/877kyjcj4d33uakius3ah0ml3cae2fv8/tyagach-belyy.jpg')
    await message.answer('1) Фильтр масляный\n'
                         ' <a href="https://disk.yandex.ru/i/neCK5G_azkQy2g">'
                         '200V05504-0122</a> ----------1шт\n'
                         ' <s>аналоги:</s>\n\n'
                         '2) Фильтр топливный грубый\n'
                         ' <a href="https://disk.yandex.ru/i/VDNZqTK54OysGg">'
                         'WG9925550966</a> --------------------1шт\n'
                         ' <s>аналоги:</s>\n\n'
                         '3) Фильтр топливный тонкой очистки\n'
                         ' <a href="https://disk.yandex.ru/i/yDOHTxJ-QIhBMA">'
                         '201V12503-0062</a> ---------------------1шт\n'
                         ' <s>аналоги:</s>\n\n'
                         '4) Фильтр патрон осушителя\n'
                         ' <a href="https://disk.yandex.ru/i/Kix4QJexAUg-Vw">'
                         '204205</a> ----------------------------1шт\n'
                         ' <u>аналоги: 227-3511010, ii40100F</u>\n\n'
                         '5) Фильтр гур\n'
                         ' <a href="https://disk.yandex.ru/i/DWFKjoKfVGRP5g">'
                         '712W47301-0133+001</a> -----------------------------1шт\n'
                         ' <u>аналоги: 4.63645</u>\n\n'
                         '6) Фильтр воздушный внешний\n'
                         ' <a href="https://disk.yandex.ru/i/l7xYJVpJM8xW7g">'
                         '710W08405-0032</a> -------------------------1шт\n'
                         ' <s>аналоги:</s>\n\n'
                         '7) Фильтр воздушный внутренний\n'
                         ' <a href="https://disk.yandex.ru/i/Sj-sX2e7HmnLRQ">'
                         '710W08405-0017</a> ---------------------------1шт\n'
                         ' <s>аналоги:</s>\n\n'
                         '8) Фильтр салона\n'
                         ' <a href="https://truckdrive.ru/i/foto-cnhtc-711w619000051-'
                         'filtr-kabiny-dlya-gruzovikov-sitrak-c7h-i-howo-t5g.jpg">'
                         '711W61900-0051</a> ----------------------1шт\n'
                         '8/1) Фильтр салона другой\n'
                         ' <a href="https://disk.yandex.ru/i/9Kb2GfRG_rOKjA">'
                         '711W61900-0050</a> ----------------------1шт\n'
                         ' <s>аналоги:</s>', reply_markup=kb_main, disable_web_page_preview=True)


@dp.message_handler(text="HOWO")
async def read_z_n(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo='https://howo-rus.com/img/model/model-2-2.jpg')
    await message.answer('1) Фильтр масляный\n'
                         ' <a href="https://disk.yandex.ru/i/neCK5G_azkQy2g">'
                         '200V05504-0122</a> ----------1шт\n'
                         ' <s>аналоги:</s>\n\n'
                         '2) Фильтр топливный грубый\n'
                         ' <a href="https://disk.yandex.ru/i/VDNZqTK54OysGg">'
                         'WG9925550966</a> --------------------1шт\n'
                         ' <s>аналоги:</s>\n\n'
                         '3) Фильтр топливный тонкой очистки\n'
                         ' <a href="https://disk.yandex.ru/i/yDOHTxJ-QIhBMA">'
                         '201V12503-0062</a> ---------------------1шт\n'
                         ' <s>аналоги:</s>\n\n'
                         '4) Фильтр патрон осушителя\n'
                         ' <a href="https://disk.yandex.ru/i/Kix4QJexAUg-Vw">'
                         '204205</a> ----------------------------1шт\n'
                         ' <u>аналоги: 227-3511010, ii40100F</u>\n\n'
                         '5) Фильтр гур\n'
                         ' <a href="https://disk.yandex.ru/i/DWFKjoKfVGRP5g"'
                         '>712W47301-0133+001</a> -----------------------------1шт\n'
                         ' <u>аналоги: 4.63645</u>\n\n'
                         '6) Фильтр воздушный внешний\n'
                         ' <a href="https://disk.yandex.ru/i/l7xYJVpJM8xW7g">'
                         '710W08405-0032</a> -------------------------1шт\n'
                         ' <s>аналоги:</s>\n\n'
                         '7) Фильтр воздушный внутренний\n'
                         ' <a href="https://disk.yandex.ru/i/Sj-sX2e7HmnLRQ">'
                         '710W08405-0017</a> ---------------------------1шт\n'
                         ' <s>аналоги:</s>\n\n'
                         '8) Фильтр салона\n'
                         ' <a href="https://truckdrive.ru/i/foto-cnhtc-711w619000051-'
                         'filtr-kabiny-dlya-gruzovikov-sitrak-c7h-i-howo-t5g.jpg">'
                         '711W61900-0051</a> ----------------------1шт\n'
                         '8/1) Фильтр салона другой\n'
                         ' <a href="https://disk.yandex.ru/i/9Kb2GfRG_rOKjA">'
                         '711W61900-0050</a> ----------------------1шт\n'
                         ' <s>аналоги:</s>', reply_markup=kb_main, disable_web_page_preview=True)
