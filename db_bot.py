import requests
from aiogram import Bot, Dispatcher, types, executor
API_TOKEN = '7076058873:AAHHMksEX5f2ZUhQBnbki3V2Z0H126EoW3k'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.reply('Привет, я нейроконсультант, который может помочь тебе с подбором спортивных упрожнений, что вас интересует?')
async def get_response(message_text):
  prompt = {
    "modelUri": "gpt://b1go1t8vie998tqjdjhu/yandexgpt-lite",
    "completionOptions": {
      "stream": False,
      "temperature": 0,
      "maxTokens": "2000"
    },
    "messages": [
      {
        "role": "system",
        "text": "Ты — Мастер по всем видам спотра, рекомендуй упрожнения по запросу, твоя задача - расписать комплекс упрожнений, количество подходов и примерное время, нагрузка, отдых между подходами"
      },
      {
        "role": "user",
        "text": message_text
      }
    ]
  }
  url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
  headers = {
      "Content-Type": "application/json",
      "Authorization": "Api-Key AQVN2JvfAWyMdNLf1b04PcAkGoRikWJgT2o2mcq1"
  }
  response = requests.post(url, headers=headers, json=prompt)
  result = response.json()
  print(result)
  return result['result']['alternatives'][0]['message']['text']
@dp.message_handler()
async def analize_message(message:types.Message):
  response_text = await get_response((message.text))
  await message.answer(response_text)
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates= True)