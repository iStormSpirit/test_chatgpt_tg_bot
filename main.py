import os

import openai
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from dotenv import load_dotenv

messages = [
    {"role": "system",
     "content": "You testing chatgpt3.5 bot in telegram"},
]


def update(messages, role, content):
    messages.append({"role": role, "content": content})
    return messages


class Settings:
    load_dotenv()
    telegram_token = os.environ['TELEGRAM_BOT_TOKEN']
    openai.api_key = os.environ['OPENAI_API_KEY']
    bot = Bot(telegram_token)
    dp = Dispatcher(bot)


@Settings.dp.message_handler()
async def send(message: types.Message):
    update(messages, "user", message.text)
    await message.answer('Обрабатываю сообщение', parse_mode="markdown")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
    )
    await message.answer(response['choices'][0]['message']['content'], parse_mode="markdown")


if __name__ == '__main__':
    executor.start_polling(Settings.dp, skip_updates=True)
