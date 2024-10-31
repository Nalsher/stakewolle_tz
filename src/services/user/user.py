import json
import datetime
from http.client import responses
from types import NoneType
from starlette.responses import Response
from src.repositories.redis.redis import RedisRepository
from src.repositories.referals.referal import ReferalRepository
from src.repositories.user.user import UserRepository
from src.schemas.schemas import CreateUserRequestSchema, AuthRequestSchema

from src.utils.jwt.jwt import create_jwt, auth_jwt


class UserService():
    def __init__(
            self,
            UserRepository: UserRepository,
            ReferalRepository: ReferalRepository,
            RedisRepository: RedisRepository
            ):
        self.UserRepository = UserRepository
        self.ReferalRepository = ReferalRepository
        self.RedisRepository = RedisRepository

    async def create_user(self, model: CreateUserRequestSchema) -> Response:
        try:
            if isinstance(model.referals, str):
                date_now = datetime.datetime.now()
                check_if_expires = await self.RedisRepository.check_if_expires(code=model.referals)
                if date_now > check_if_expires:
                    Create_User_Returning_id = await (self.UserRepository.
                                                      create_user(model)
                                                      )
                    Update_referals_User = await (self.RedisRepository.
                                                  get_id_by_code
                                                  (code=model.referals)
                                                  )
                    if Update_referals_User:
                        await (self.ReferalRepository.create_referal
                               (referr_id=Update_referals_User,
                                reffered_id=Create_User_Returning_id)
                               )

                    else:
                        return Response(status_code=200,
                                        content="User created, "
                                                "but reff code wasn't working"
                                        )
                else:
                    return Response(status_code=500,
                                    content="Your code is expired"
                                    )
            if isinstance(model.referals, NoneType):
                await self.UserRepository.create_user(model)
            response = Response(status_code=200,
                                content="User successfully created"
                                )
            return response
        finally:
            response = Response(status_code=500,
                                content="Error,user not created"
                                )
            return response

    async def delete_referal_code(self, token: str | None) -> Response:
        user_id = await auth_jwt(token)
        if not await user_id:
            response = Response(status_code=401,
                                content="Non authorized"
                                )
            return response
        await self.RedisRepository.delete_code(user_id=user_id)
        response = Response(status_code=200,
                            content="Your code successfully deleted"
                            )
        return response

    async def create_referal_code(self, code: str,
                                  token: str | None
                                  ) -> Response:
        user_id = await auth_jwt(token)
        if not user_id:
            response = Response(status_code=401, content="Non authorized")
            return response
        if await self.RedisRepository.check_if_user_have_code(user_id):
            await self.RedisRepository.create_code(user_id=user_id, code=code)
            response = Response(status_code=200,
                                content="Your code successfully created"
                                )
            return response
        else:
            return Response(status_code=500,
                            content="User already have a code"
                            )

    async def login(self, authmodel: AuthRequestSchema) -> Response:
        User = await (self.UserRepository.
                      get_user_by_username(authmodel.username)
                      )
        if User.password == authmodel.password:
            response = Response("You loggin in successfully")
            response.set_cookie(key="token", value=await create_jwt(User.id))
            return response
        else:
            return responses(status_code=401, content="Non authorized")

    async def get_code_by_mail(self, email: str) -> Response:
        user_id = await self.UserRepository.get_user_id_by_email(email)
        if user_id:
            try:
                code = await self.RedisRepository.get_code(user_id=user_id)
                response = Response(status_code=200,
                                    content={"Your code": code}
                                    )
            finally:
                response = Response(status_code=404,
                                    content={"Error,server not found code"}
                                    )
            return response
        else:
            return Response(status_code=500,
                            content=f"User by {email} not found")

    async def get_all_refers(self, id: int) -> Response:
        get_reffers_id = await self.ReferalRepository.get_referals(id)
        if get_reffers_id:
            try:
                users = await self.UserRepository.get_users(get_reffers_id)
                users_info = {}
                for i in users:
                    users_info[i.id] = i.username
                response = Response(status_code=200,
                                    content=json.dumps(users_info)
                                    )
                return response
            finally:
                response = Response(status_code=500,
                                    content=f"Users with {get_reffers_id}"
                                            f"-referal_id not found"
                                    )
                return response
        else:
            response = Response(status_code=500,
                                content=f"User with {get_reffers_id} not found"
                                )
            return response
