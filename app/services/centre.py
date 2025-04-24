from datetime import datetime, timedelta
from requests import post


async def send_data(code: int, level: float, meneral: float, temperature: float):
    now = datetime.today() + timedelta(hours=5)
    current_hour = now.hour
    current_minute = now.minute
    rand_hour = random.randint(0, current_hour)
    if rand_hour == current_hour:
        rand_minute = random.randint(0, current_minute)
    else:
        rand_minute = random.randint(0, 59)
    rand_time = now.replace(hour=rand_hour, minute=rand_minute, second=0, microsecond=0)

    today = int(rand_time.strftime("%Y%m%d%H%M"))

    post(
        url="http://89.236.195.198:3010",
        json={
            "code": code,
            "data": {
                "level": level,
                "meneral": meneral,
                "temperatyra": temperature,
                "vaqt": today,
            },
        },
    )
