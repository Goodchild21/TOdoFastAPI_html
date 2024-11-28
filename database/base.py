import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from todo.config import settings



BASE_DIR = os.path.dirname(os.path.abspath(__name__)) #константа с путем до папки database
db_path = os.path.join(BASE_DIR, 'todo', 'database', 'DB') #Путь до папки DB в которой будет создаваться база данных
if not os.path.exists(db_path):  #Если вышестоящего пути нет мы создаем этот путь
    os.makedirs(db_path)


Base = declarative_base()

#Функция для генерирования сессии
def get_db():
    db_session_local = SessionLocal()
    try:
        yield db_session_local
    finally:
        db_session_local.close()


engine = create_engine(settings.db_sqlite_url, connect_args={'check_same_thread': False}, echo=True) #echo для логов в консоль

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) #autocommit -автосохранение в ДБ, autoflush -доступ к еще не сохраненным данным
#bind объединяет сессии в ДБ