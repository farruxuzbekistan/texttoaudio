#! ctrl + p
# 7773005244:AAF15-Y4bgIAEG2HuUdgrqjFHRGeSLZR1DQ

import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import ParseMode
from gtts import gTTS


API_TOKEN = "7773005244:AAF15-Y4bgIAEG2HuUdgrqjFHRGeSLZR1DQ"


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


# start message
@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):

    await message.reply(
        "Assalom alaykum,bizga text yuboring,, va biz uni audioga aylantirib beramiz!"
    )


# handle any text message
@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def text_to_speech(message: types.Message):

    text = message.text
    language = "en"

    obj = gTTS(text=text, lang=language, slow=False)
    obj.save("output.mp3")

    await message.reply("Mana sizning audio faylingiz: ")
    await message.answer_audio(open("output.mp3", "rb"))

    os.remove("output.mp3")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)


# farruhdeveloper
