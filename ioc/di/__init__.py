from injector import Injector

from ioc.di.database import DatabaseModule
from ioc.di.options import OptionsModule
from ioc.di.repository import RepositoryModule
from ioc.di.usecase import UseCaseModule


injector = Injector([DatabaseModule, OptionsModule, RepositoryModule, UseCaseModule])
