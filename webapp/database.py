from sqlalchemy import create_engine, orm
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
import contextlib


Base = declarative_base()


class Database:
    def __init__(self, db_url: str):
        self.db_url = db_url
        self.engine = create_engine(self.db_url, connect_args={
            "check_same_thread": False})
        self.session_factory = orm.scoped_session(
            orm.sessionmaker(autocommit=False,
                             autoflush=False, bind=self.engine))

    @contextlib.contextmanager
    def session(self):
        session: Session = self.session_factory()
        try:
            yield session
        except Exception as e:
            print('Session rollback because of exception: %s', e,
                  exc_info=True)
            session.rollback()
        finally:
            session.close()

    @staticmethod
    def session_factory(db):
        return db.session
