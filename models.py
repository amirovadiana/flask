import os
import datetime
from datetime import date
import atexit
from sqlalchemy import create_engine, Integer, String, DateTime, func
from sqlalchemy.orm import sessionmaker, DeclarativeBase, mapped_column, Mapped


POSTGRES_USER = os.getenv('POSTGRES_USER', 'user')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', '1234')
POSTGRES_DB = os.getenv('POSTGRES_DB', 'flask')
POSTGRES_HOST = os.getenv('POSTGRES_HOST', 'localhost')
POSTGRES_PORT = os.getenv('POSTGRES_PORT', '5431')

PG_DSN =(
    f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@'
    f'{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'
)

engine = create_engine(PG_DSN)
Session = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass


class Advertisement(Base):
    __tablename__ = 'advertisements'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String)
    date_create: Mapped[datetime.datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
    )
    author: Mapped[str] = mapped_column(String)


    @property
    def id_json(self):
        return{
            'id': self.id,
        }

    @property
    def convert_json(self):
        return{
            'id': self.id,
            'title': self.title,
            'date_create': self.date_create.isoformat(),
            'author': self.author,
        }


Base.metadata.create_all(engine)

atexit.register(engine.dispose)