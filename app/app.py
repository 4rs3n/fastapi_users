from fastapi import FastAPI, Depends

from app.db import User
from app.schemas import UserCreate, UserRead, UserUpdate
from app.users import auth_backend, active_user, fastapi_user

VERSION = "1.4.0"
TITLE = 'UsermanagementAPI'
DESCRIPTION = '''Api for managing accounts and users in csm.'''
BASE_ROUTE = '/api/v1/usermanagement'

app = FastAPI(openapi_url=f"{BASE_ROUTE}/openapi.json",
    docs_url=f"{BASE_ROUTE}/docs",
    redoc_url=f'{BASE_ROUTE}/redoc',
    version=VERSION,
    title=TITLE,
    description=DESCRIPTION
    )

app.include_router(fastapi_user.get_auth_router(auth_backend), tags=['auth'], prefix=BASE_ROUTE)
app.include_router(fastapi_user.get_register_router(UserRead, UserCreate), tags=['auth'], prefix=BASE_ROUTE)
app.include_router(fastapi_user.get_reset_password_router(), tags=['auth'], prefix=BASE_ROUTE)
app.include_router(fastapi_user.get_verify_router(UserRead), tags=['auth'], prefix=BASE_ROUTE)
app.include_router(fastapi_user.get_users_router(UserRead, UserUpdate), tags=['users'], prefix=f'{BASE_ROUTE}/users')

@app.get('/authenticated')
async def authenticated(user: User = Depends(active_user)):
    return {'message':f'hallo von {user.username} mit der mail {user.email}'}

# not needed
# @app.on_event('startup')
# async def on_startup():
#     pass