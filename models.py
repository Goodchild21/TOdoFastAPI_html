from todo.database.base import Base, engine
from sqlalchemy import Column, Integer, String, Boolean


class ToDo(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    is_complete = Column(Boolean, default=False)

#Создать таблицу
Base.metadata.create_all(bind=engine)