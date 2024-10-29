import datetime
from src.config.config import jwt_key
import jwt


async def create_jwt(userid: int):
    payload = {"id": userid,"exp_time":str(datetime.datetime.now().date() + datetime.timedelta(days=1))}
    jwttoken = jwt.encode(payload=payload, secret_key=jwt_key, algorithm="HS256")
    return jwttoken

async def check_jwt(token_to_check: str):
    token_check = jwt.decode(token_to_check)
    time_from_token = datetime.datetime.strptime(token_check.get("exp_time"),"%Y-%m-%d")
    if datetime.datetime.now() > time_from_token:
        return False
    else:
        return True
