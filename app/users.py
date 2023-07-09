from fastapi import Depends
from fastapi_users import BaseUserManager, FastAPIUsers, UUIDIDMixin
from fastapi_users.authentication import AuthenticationBackend, CookieTransport, JWTStrategy
from fastapi_users.db import SQLAlchemyUserDatabase

from app.db import get_user_db


JWT_TOKEN_SECRET = 'JWT_creation_secret.123'
JWT_TOKEN_VERIFICATION_SECRET = 'JWT_verification_secret.123'
JWT_STRATEGY_SECRET = 'JWT_strategy_secret.123'
JWT_LIFETIME_SECONDS = 300

class UserManager(UUIDIDMixin, BaseUserManager):
    reset_password_token_secret = JWT_TOKEN_SECRET
    verification_token_secret = JWT_TOKEN_VERIFICATION_SECRET

async def get_user_manager(user_db: SQLAlchemyUserDatabase = Depends(get_user_db)):
    yield UserManager(user_db=user_db)

# cookie_secure allows the reading of a cookie only if the connection is secure
# cookie_httponly prevents js to read the cookie
cookie_transport = CookieTransport(cookie_httponly=True, cookie_secure=False)

def get_jwt_strategy():
    return JWTStrategy(secret=JWT_STRATEGY_SECRET, lifetime_seconds=JWT_LIFETIME_SECONDS)

auth_backend = AuthenticationBackend(name='jwt', transport=cookie_transport, get_strategy=get_jwt_strategy)

fastapi_user = FastAPIUsers(get_user_manager=get_user_manager, auth_backends=[auth_backend])

active_user = fastapi_user.current_user(active=True)