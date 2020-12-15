from fastapi import APIRouter
from fastapi import Depends
from dependency_injector.wiring import inject, Provide
from .containers import Container
from .services import UserService
from .repositories import UserRepository

router = APIRouter()


@router.get("/users")
@inject
def root(
        user_service: UserService = Depends(Provide[Container.user_service])
):
    return user_service.get_users()


@router.get("/no_di")
def test():
    return {"data": "test data"}


@router.get("/users/{id}")
@inject
def get_by_id(id: int,
              user_service: UserService =
              Depends(Provide[Container.user_service])):
    return user_service.user_by_id(id)


@router.get("/users/add")
@inject
def add(user_service: UserService = Depends(Provide[Container.user_service])):
    return user_service.create_user()


@router.get("/users/remove/{id}")
@inject
def remove(id: int,
           user_repository: UserRepository =
           Depends(Provide[Container.users_repository])):
    return user_repository.delete_by_id(id)
