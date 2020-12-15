from .repositories import UserRepository
from uuid import uuid4


class UserService:
    def __init__(self, users_repository: UserRepository):
        self.users_repo: UserRepository = users_repository

    def get_users(self):
        return self.users_repo.get_all_users()

    def user_by_id(self, id):
        print("in service by id", id)
        return self.users_repo.get_by_id(id)

    def create_user(self):
        uid = uuid4()
        self.users_repo.add_user(f"{uid}@email.com", "pwd")
