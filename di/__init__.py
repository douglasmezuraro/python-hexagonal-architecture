from injector import Injector

from di.database import DatabaseModule
from di.repository import RepositoryModule
from di.usecase import UseCaseModule


injector = Injector([DatabaseModule, RepositoryModule, UseCaseModule])
