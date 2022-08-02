from typing import Union
from environs import Env

env = Env()

env.read_env(".env")

SENSOR: int = env.int("SENSOR", 0)
PIN: int = env.int("PIN", 0)

TELEGRAM_BOT_TOKEN: str = env.str("TELEGRAM_BOT_TOKEN", "")
temp = env.str("TELEGRAM_CHAT_ID", "")
TELEGRAM_CHAT_ID: Union[str, int] = int(temp) if temp.isdecimal() else temp

SEND_ERROR_MESSAGE: bool = env.bool("SEND_ERROR_MESSAGE", False)

TIME_TO_SLEEP: int = 300
