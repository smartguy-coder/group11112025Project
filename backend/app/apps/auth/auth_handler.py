from apps.users.models import User
from settings import settings
from datetime import datetime, timedelta
import jwt


class AuthHandler:
    def __init__(self):
        self.secret = settings.JWT_SECRET
        self.algorithm = settings.JWT_ALGORITHM

    async def get_access_token(self, user: User) -> dict:
        now = datetime.now()
        payload = {
            "iat": now,
            "exp": now + timedelta(minutes=15),
            "sub": user.email
        }
        access_token = jwt.encode(
            payload,
            self.secret,
            algorithm=self.algorithm
        )
        return {
            "access_token": access_token
        }


auth_handler = AuthHandler()
