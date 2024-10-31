import datetime
from src.config.config import jwt_key
import jwt


async def create_jwt(userid: int) -> str:
    payload = {"id": userid,
               "exp_time": str(datetime.datetime.now().date() +
                               datetime.timedelta(days=1)
                               )
               }
    jwttoken = jwt.encode(payload=payload, key=jwt_key)
    return jwttoken


async def auth_jwt(token_to_check: str) -> bool | str:
    token_check = jwt.decode(token_to_check, key=jwt_key, algorithms="HS256")
    time_from_token = (datetime.datetime.strptime
                       (token_check.get("exp_time"), "%Y-%m-%d")
                       )
    if datetime.datetime.now() > time_from_token:
        return False
    else:
        return token_check.get("id")
