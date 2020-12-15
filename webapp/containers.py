from dependency_injector import containers, providers

from .database import Database
from .repositories import UserRepository
from .services import UserService


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    db = providers.Singleton(Database, db_url=config.db.url)
    session_factory = providers.Factory(Database.session_factory, db=db)

    users_repository = providers.Factory(
        UserRepository,
        session_factory=session_factory)

    user_service = providers.Factory(
        UserService,
        users_repository=users_repository)
