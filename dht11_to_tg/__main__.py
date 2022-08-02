import time
from typing import Optional

import Adafruit_DHT as dht
from telebot import TeleBot

from dht11_to_tg import PIN, SEND_ERROR_MESSAGE, SENSOR, TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, TIME_TO_SLEEP


def make_measurement() -> tuple[Optional[float], Optional[float]]:
    humidity, temperature = dht.read_retry(SENSOR, PIN)
    return humidity, temperature


def send_message_to_tg(message):
    bot.send_message(TELEGRAM_CHAT_ID, message, parse_mode="HTML")


if __name__ == "__main__":
    bot = TeleBot(TELEGRAM_BOT_TOKEN)

    while True:
        message: str = ""
        try:
            humidity, temperature = make_measurement()
            if humidity is not None and temperature is not None:
                print(f"Temperature: {temperature}°C Humidity: {humidity}%")
                message = f"<b>Temperature:</b> {temperature}°C\n<b>Humidity:</b> {humidity}%"
                send_message_to_tg(message)
                time.sleep(TIME_TO_SLEEP)
            else:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nExiting...")
        except Exception as e:
            if SEND_ERROR_MESSAGE:
                send_message_to_tg(str(e))
            print(e)
