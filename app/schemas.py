from fastapi_users.schemas import BaseUser, BaseUserCreate, BaseUserUpdate, BaseOAuthAccountMixin

class UserRead(BaseUser):
    username: str
    class Config:
        from_attributes=True

class UserCreate(BaseUserCreate):
    username: str
    class Config:
        from_attributes=True

class UserUpdate(BaseUserUpdate):
    username: str
    class Config:
        from_attributes=True