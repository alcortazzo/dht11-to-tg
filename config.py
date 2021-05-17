sensor = 11  # index of dht sensor (11 = DHT11, 22 = DHT22, 2302 = AM2302)
pin = 4  # gpio number used for data transfer

tgBotToken = "123456789:Token"  # telegram bot token
timeSleep = 60 * 5  # time (seconds) to sleep between sending data to tg users
tgDomen = ['@durov', 123456789]  # list of tg channels LINKs (str) or users IDs (int) where bot will post data