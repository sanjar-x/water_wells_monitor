data = {
    "code": 860389053632341,
    "data": {"level": 554.67, "meneral": 1.456, "temperatyra": 14.5, "vaqt": 20250113},
}
from datetime import datetime, timedelta
from requests import post


async def send_data(code: int, level: float, meneral: float, temperature: float):
    now = datetime.today() + timedelta(hours=5)
    today = int(now.strftime("%Y%m%d%H%M"))
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
