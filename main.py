#!/usr/bin/env python

import time, config
import Adafruit_DHT as dht
from telebot import TeleBot

bot = TeleBot(config.tgBotToken)


def sendDataToTG(humidity, temperature):
    for id in config.tgDomen:
        bot.send_message(
            id,
            f"Temperature: <code>{temperature}°C</code>\n"
            f"Humidity: <code>{humidity}%</code>",
            parse_mode="HTML",
            disable_notification=True,
        )


def sendErrorToTG(textError):
    for id in config.tgDomen:
        bot.send_message(id, textError)


if __name__ == "__main__":
    while True:
        try:
            humidity, temperature = dht.read_retry(config.sensor, config.pin)
            if (humidity is not None) and (temperature is not None):
                sendDataToTG(humidity, temperature)
                time.sleep(config.timeSleep)
            else:
                time.sleep(1)
        except Exception as ex:
            sendErrorToTG(
                f"[{type(ex).__name__}] went wrong when bot tryed to get data(): {str(ex)}"
            )
