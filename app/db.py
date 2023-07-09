from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase
from sqlalchemy import Column, String, TIMESTAMP
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus
import uuid


def create_db_url(protocol:str, pw:str, user:str, port:int|str, host:str, db:str, trailing_slash:bool=False) -> str:
    parsed_pw = quote_plus(pw)
    parsed_user = quote_plus(user)
    if trailing_slash:
        return f'{protocol}://{parsed_user}:{parsed_pw}@{host}:{port}/{db}/'
    return f'{protocol}://{parsed_user}:{parsed_pw}@{host}:{port}/{db}'

DATABASEURL = create_db_url(protocol='postgresql+asyncpg',
                            host='localhost',
                            port=5433,
                            user='admin',
                            pw='admin',
                            db='user_db')

Base = declarative_base()

class User(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = 'user_table'
    username = Column(String)

async_engine = create_async_engine(DATABASEURL)
async_session_maker = sessionmaker(bind=async_engine, class_=AsyncSession, expire_on_commit=False)

async def get_async_session():
    async with async_session_maker() as session:
        yield session

async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session=session, user_table=User)