from .models import User
# from sqlalchemy.orm import Session


class UserRepository:

    def __init__(self, session_factory):
        self.session_factory = session_factory

    def get_by_id(self, id):
        with self.session_factory() as s:
            return s.query(User).filter(User.id == id).first()

    def get_user(self):
        with self.session_factory() as session:
            return session.query(User).first()

    def get_all_users(self):
        with self.session_factory() as session:
            return session.query(User).all()

    def add_user(self,  email: str, pwd: str, is_active: bool = True):
        with self.session_factory() as session:
            user = User(email=email, hashed_password=pwd, is_active=is_active)
            session.add(user)
            session.commit()

    def delete_by_id(self, id: int):
        with self.session_factory() as sess:
            rec: User = sess.query(User).filter(User.id == id).first()
            if not rec:
                raise Exception(f"Запись с id:{id} не найдена")
            sess.delete(rec)
            sess.commit()
